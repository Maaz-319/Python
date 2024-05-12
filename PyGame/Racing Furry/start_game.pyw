from tkinter import *
import os

os.chdir('utilities')


def start_game():  # This function will start the game and also tell the game which mode to start in
    with open("data.txt", "w") as f:
        f.write(str(game_mode.get()))
        f.close()
    os.system("Joystick.pyw")


def exit_game():
    root.quit()


# --------------------------------------Initialize Root------------------------------
root = Tk()
root.title("Made by Maaz")
root.geometry("600x530")
root.resizable(False, False)
root.configure(bg="black")
# -----------------------------------------------------------------------------------

# --------------------------------------Game Mode--------------------------------------
Label(root, text="Select Game Mode", bg='black', fg='white', font=("consolas", 30, "bold underline")).pack(pady=20)

game_mode = IntVar()
game_mode.set(30)
easy_mode_button = Radiobutton(root, text="Easy", value=30, variable=game_mode, bg='black', fg='light Green',
                               font=("consolas", 20), activebackground='light green', bd=0, selectcolor='black')
easy_mode_button.pack(anchor=CENTER)
medium_mode_button = Radiobutton(root, text="Medium", value=40, variable=game_mode, bg='black', fg='Yellow',
                                 font=("consolas", 20), activebackground='yellow', bd=0, selectcolor='black')
medium_mode_button.pack(anchor=CENTER)
hard_mode_button = Radiobutton(root, text="Hard", value=60, variable=game_mode, bg='black', fg='Red',
                               font=("consolas", 20), activebackground='red', bd=0, selectcolor='black')
hard_mode_button.pack(anchor=CENTER)
# --------------------------------------Game Mode--------------------------------------

# =========================================================================================================

# --------------------------------------Button-----------------------------------------
Label(root, text="Press Start to Play", bg='black', fg='white', font=("consolas", 30, "bold underline")).pack(pady=40)
start_button = Button(root, text="Start", command=start_game, bg='Green', fg='White', font=("consolas", 20), border=0,
                      width=20)
start_button.pack(pady=10)

exit_button = Button(root, text="Exit", command=exit_game, bg='Red', fg='White', font=("consolas", 20), border=0,
                     width=20)
exit_button.pack(pady=10)
# --------------------------------------Button-----------------------------------------
root.mainloop()
