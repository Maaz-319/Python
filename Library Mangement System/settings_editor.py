def update_settings(current_librarian, theme):
    if not current_librarian:
        with open('settings.py', 'w') as f:
            f.write(
                f'current_librarian = {current_librarian}\ntheme = "{theme}"\n')
            f.close()
    else:
        with open('settings.py', 'w') as f:
            f.write(
                f'current_librarian = "{current_librarian}"\ntheme = "{theme}"\n')
            f.close()
