from tkinter import *
import customtkinter as maaz

maaz.set_appearance_mode('System')
maaz.set_default_color_theme('green')


# Translates a string into an M language.
def translate():
    global entry
    text = str(entry.get())

    # Replaces all occurrences of vovals in the text.
    result = text.replace("e", "m").replace("u", "m").replace(
        "i", "m").replace("o", "m").replace("a", "m")

    # Deletes the entry and inserts the result.
    entry.delete(0, END)
    entry.insert(0, result)


# Creates a new Tk object with the customized configuration.
root = maaz.CTk()
root.title("(Maaz) Translator")
root.geometry("300x300")

label = maaz.CTkLabel(text="Enter text down ↓", text_font=("Microsoft YaHei UI Light", 15)).pack()

entry = maaz.CTkEntry(text_font=("Microsoft YaHei UI Dark", 15), width=280)
entry.pack(pady=20)

button = maaz.CTkButton(text_font=("Microsoft YaHei UI Light", 15), text="Go", command=translate).pack(pady=10)

root.mainloop()
