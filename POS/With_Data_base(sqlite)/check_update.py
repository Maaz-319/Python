import requests
from tkinter import messagebox


def download_files_from_github_folder(repo_owner, repo_name, folder_path, exclude_file):
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{folder_path}"
    response = requests.get(api_url)
    files = response.json()

    for file in files:
        if file['name'] in exclude_file:
            continue

        file_url = file['download_url']
        response = requests.get(file_url)
        with open(file['name'], 'wb') as f:
            f.write(response.content)


def get_file_content_from_github(url):
    raw_url = url.replace("github.com", "raw.githubusercontent.com").replace("/blob", "")
    response = requests.get(raw_url)
    if response.status_code == 200:
        return response.text
        messagebox.showerror("Error", "Error While Installing")
    else:
        return None


def install_new_version():
    print("\nInstalling new version...\n")
    try:
        download_files_from_github_folder('maaz-319', 'python', 'POS/With_Data_base(sqlite)',
                                          ['check_update.py', 'Orders.db', "Items.db", "Cashiers.db"])
    except:
        messagebox.showerror("Error", "Check Internet Connection")
    input("Installation completed. POS latest Installed")


# Usage
url = "https://github.com/Maaz-319/Python/blob/main/POS/With_Data_base(sqlite)/version.py"
file_content = get_file_content_from_github(url)
if file_content is not None:
    with open("version.py", "r+") as file:
        data = file.read()
    if file_content == data:
        input("POS is up-to-date.")
    else:
        a = input(f"New {file_content} Available. Current Version: {data}. Install? (y/n): ")
        if a == "y":
            install_new_version()
        else:
            input("Installation cancelled.")
else:
    input("Failed to fetch file content.")
