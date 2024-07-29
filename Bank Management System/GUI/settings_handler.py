def update_settings(current_user):
    if current_user:
        with open("settings.py", "w") as file:
            file.write(f"current_user = '{current_user}'")
    else:
        with open("settings.py", "w") as file:
            file.write(f"current_user = {current_user}")