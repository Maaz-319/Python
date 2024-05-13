from tkinter import *
import os
from utilities import settings as st

os.chdir('utilities')
cars = ["images/cars/1.png", "images/cars/2.png", "images/cars/3.png", "images/cars/4.png", "images/cars/5.png",
        "images/cars/6.png", "images/cars/7.png"]


def start_game():  # This function will start the game and also tell the game which mode to start in
    st.values[0] = 60
    st.values[1] = game_mode.get()
    st.values[3] = selected_car.get()
    if game_mode.get() == 30:
        st.values[2] = 50
    elif game_mode.get() == 40:
        st.values[2] = 70
    elif game_mode.get() == 60:
        st.values[2] = 90
    with open("settings.py", "w") as f:
        f.write("values = " + str(st.values) + "\n# setting fps, mode, lane_speed, car\n")
        f.close()
    os.system("Joystick.pyw")


def exit_game():
    root.quit()


def preview_car():
    global photo
    os.chdir("../utilities/")
    photo = PhotoImage(file=selected_car.get())
    car_preview.configure(image=photo)


# --------------------------------------Initialize Root------------------------------
root = Tk()
root.title("Made by Maaz")
root.state("zoomed")
root.resizable(False, False)
root.configure(bg="black")
# -----------------------------------------------------------------------------------

# --------------------------------------Game Mode--------------------------------------
Label(root, text="Select Game Mode", bg='black', fg='white', font=("consolas", 30, "bold underline")).grid(row=0,
                                                                                                           column=0,
                                                                                                           pady=20,
                                                                                                           padx=10)

game_mode = IntVar()
game_mode.set(30)
easy_mode_button = Radiobutton(root, text="Easy", value=30, variable=game_mode, bg='black', fg='light Green',
                               font=("consolas", 20), activebackground='light green', bd=0, selectcolor='black')
easy_mode_button.grid(row=1, column=0)
medium_mode_button = Radiobutton(root, text="Medium", value=40, variable=game_mode, bg='black', fg='Yellow',
                                 font=("consolas", 20), activebackground='yellow', bd=0, selectcolor='black')
medium_mode_button.grid(row=2, column=0)
hard_mode_button = Radiobutton(root, text="Hard", value=60, variable=game_mode, bg='black', fg='Red',
                               font=("consolas", 20), activebackground='red', bd=0, selectcolor='black')
hard_mode_button.grid(row=3, column=0)
# --------------------------------------Game Mode--------------------------------------

# =========================================================================================================


# --------------------------------------Cars----------------------------------------
selected_car = StringVar()
selected_car.set(cars[0])
Label(root, text="Select Car", bg='black', fg='white', font=("consolas", 30, "bold underline")).grid(pady=20, row=0,
                                                                                                     column=2)
Radiobutton(root, text="1", value=cars[0], variable=selected_car, bg='black', fg='Red',
            font=("consolas", 15), activebackground='red', bd=0, selectcolor='black', command=preview_car).grid(row=1,
                                                                                                                column=2)
Radiobutton(root, text="2", value=cars[1], variable=selected_car, bg='black', fg='Red',
            font=("consolas", 15), activebackground='red', bd=0, selectcolor='black', command=preview_car).grid(row=2,
                                                                                                                column=2)
Radiobutton(root, text="3", value=cars[2], variable=selected_car, bg='black', fg='Red',
            font=("consolas", 15), activebackground='red', bd=0, selectcolor='black', command=preview_car).grid(row=3,
                                                                                                                column=2)
Radiobutton(root, text="4", value=cars[3], variable=selected_car, bg='black', fg='Red',
            font=("consolas", 15), activebackground='red', bd=0, selectcolor='black', command=preview_car).grid(row=4,
                                                                                                                column=2)
Radiobutton(root, text="5", value=cars[4], variable=selected_car, bg='black', fg='Red',
            font=("consolas", 15), activebackground='red', bd=0, selectcolor='black', command=preview_car).grid(row=5,
                                                                                                                column=2)

Radiobutton(root, text="6", value=cars[5], variable=selected_car, bg='black', fg='Red',
            font=("consolas", 15), activebackground='red', bd=0, selectcolor='black', command=preview_car).grid(row=6,
                                                                                                                column=2)
Radiobutton(root, text="7", value=cars[6], variable=selected_car, bg='black', fg='Red',
            font=("consolas", 15), activebackground='red', bd=0, selectcolor='black', command=preview_car).grid(row=7,
                                                                                                                column=2)

photo = PhotoImage(file=cars[0])
frame = Frame(root, width=200, height=200, bg='black')
frame.grid(row=15, column=3, pady=10)
frame.grid_propagate(False)
car_preview = Label(frame, image=photo, bg='black')
car_preview.grid(row=0, column=0, sticky='ew', padx=20, pady=20)

# --------------------------------------Cars----------------------------------------

# --------------------------------------Button-----------------------------------------
Label(root, text="Press Start to Play", bg='black', fg='white', font=("consolas", 30, "bold underline")).grid(row=10,
                                                                                                              column=1)
start_button = Button(root, text="Start", command=start_game, bg='Green', fg='White', font=("consolas", 20), border=0,
                      width=20)
start_button.grid(row=11, column=1, pady=5)

exit_button = Button(root, text="Exit", command=exit_game, bg='Red', fg='White', font=("consolas", 20), border=0,
                     width=20)
exit_button.grid(row=12, column=1, pady=5)
# --------------------------------------Button-----------------------------------------

root.mainloop()
