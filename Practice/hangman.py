from tkinter import *
from random import choice
from tkinter import messagebox

secret_word = None
turns_count = 5
bg_color = 'Light Green'
fg_color = 'Black'
guessed_characters = []
indicating_text = ""
user_guess = None
word_list = [
    "apple", "banana", "chocolate", "umbrella", "elephant",
    "guitar", "hamburger", "jazz", "kangaroo", "lighthouse",
    "mountain", "ocean", "piano", "rainbow", "sunflower",
    "television", "vampire", "watermelon", "xylophone", "zebra",
    "butterfly", "candle", "dragon", "fireworks", "giraffe",
    "honeybee", "icecream", "jigsaw", "kite", "lemonade",
    "magnolia", "nightmare", "octopus", "penguin", "quicksand",
    "raccoon", "strawberry", "toucan", "unicorn", "volcano",
    "whale", "xylophone", "yacht", "zucchini", "acrobatic",
    "boulevard", "carousel", "dandelion", "elevator", "fountain",
    "gorilla", "hedgehog", "igloo", "jackal", "koala", "llama",
    "marmalade", "narwhal", "opera", "pancake", "quokka", "rhinoceros",
    "sunrise", "tornado", "umbrella", "vibrant", "waterfall", "xylophone",
    "yogurt", "zeppelin", "avocado", "blueberry", "caterpillar", "dolphin",
    "elephant", "flamingo", "gazelle", "hibiscus", "iguana", "jellyfish",
    "kangaroo", "lemur", "macaw", "nightingale", "ostrich", "panda",
    "quail", "rhinoceros", "seagull", "tiger", "unicorn", "vulture",
    "walrus", "x-ray", "yak", "zebra"
]


def entry_focused(_):
    temp = input_box.get()
    if len(temp) > 1:
        temp = temp[-1]
    input_box.delete(0, END)
    input_box.insert(0, temp)


def check_guess(_):
    global user_guess, secret_word, indicating_text, turns_count, guessed_characters
    user_guess = input_box.get().lower()

    if not user_guess:
        messagebox.showerror("Hangman", "Please Enter a guess")
        return
    if user_guess in secret_word:
        if str(indicating_text) == secret_word:
            messagebox.showinfo("Hangman", "Congratulations! You have won!!!!")
            return
        guessed_characters.append(user_guess)
        indicating_text = list(indicating_text)
        index = list(secret_word).index(user_guess)
        indicating_text[index] = user_guess
        indicating_label['text'] = str(indicating_text).replace('[', '').replace(']', '').replace(',', '').replace("'",
                                                                                                                   '')
    else:
        turns_count -= 1
        if turns_count == 0:
            turns_label['text'] = "Turns Left: " + str(turns_count)
            messagebox.showerror("Hangman", "You have lost!\nBetter luck next time")
            return
        turns_label['text'] = "Turns Left: " + str(turns_count)


def choose_secret_word():
    global secret_word, indicating_text, indicating_label
    secret_word = choice(word_list)
    print(secret_word)
    for n in secret_word:
        indicating_text = str(indicating_text) + '-'
    indicating_label.configure(text=str(indicating_text))


root = Tk()
root.title("Hangman Game | by Maaz")
root.state('zoomed')
root.configure(bg="light green")
root.resizable(False, False)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.bind("<Return>", check_guess)

# Defining Objects
indicating_label = Label(root, text="TESTING", bg=bg_color, fg='Purple', font=("Ariel", 35))
indicating_label.place(x=520, y=250)
Label(root, font=("Constancia", 25), text='Your Guess →  ', bg=bg_color, fg='Blue').place(x=(screen_width - 480) / 2,
                                                                                          y=50)
input_box = Entry(root, font=('Ariel', 25), bg=bg_color, fg=fg_color, width=2, border=0.5)
turns_label = Label(root, text='Turns Left: ' + str(turns_count), bg=bg_color, fg='Red', font=("Constancia", 20))
turns_label.place(x=20, y=20)
play_again_button = Button(root, text='Play Again', font=('Ariel', 15), borderwidth=1, bg='Light Blue', fg=fg_color,
                           width=20)
go_button = Button(root, text="GO", font=("Constancia", 15), bg='#3c3f41', fg=bg_color, activebackground='#2b2b2b',
                   activeforeground="white", command=lambda: check_guess(0))

choose_secret_word()

# Placing Objects
indicating_label.place(x=(screen_width - 300) / 2, y=screen_height - 200)
go_button.place(x=(screen_width + 130) / 2, y=50)
go_button.configure(relief='ridge')

input_box.place(x=screen_width / 2, y=50)
input_box.configure(relief='solid')
input_box.bind("<KeyRelease>", entry_focused)

root.mainloop()
