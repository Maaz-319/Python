from tkinter import *
from random import choice
from tkinter import messagebox

secret_word = None
turns_count = 8
bg_color = 'Light Green'
fg_color = 'Black'
guessed_characters = []
indicating_text = ""
user_guess = None
rules_text = "─────────────────────\nRules:\n• Guess the Word Challenge •\n\n• You have to Enter your Guessed letter of the word in the box saying 'Your Guess.'\n• Only one letter is allowed at a time and you lose a turn on the wrong guess.         \n• After entering your guess, click on the 'Go' button or simply press the Enter key.  \n• The number of dashes at the bottom represents the length of the word to guess.   \n\nAre you up for the challenge? Let's play!\n─────────────────────"
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
    temp_indicating_text = list(indicating_text)

    if not user_guess:
        messagebox.showerror("Guess the Word", "Please Enter a guess")
        return
    if user_guess in secret_word:
        for x in range(len(secret_word)):
            if user_guess == secret_word[x]:
                temp_indicating_text[x] = user_guess
            indicating_text = str(temp_indicating_text).replace('[', '').replace(']', '').replace(',',
                                                                                                  '').replace(
                "'", '').replace(" ", '')
            indicating_label['text'] = indicating_text
    else:
        turns_count -= 1
        turns_label['text'] = "Turns Left: " + str(turns_count)
        if turns_count == 0:
            turns_label['text'] = "Turns Left: " + str(turns_count)
            choice = messagebox.askyesno("Guess the Word", str("You have lost!\nThe Word was " + secret_word + ". Better luck next time\nPlay Again?"))
            if choice:
                choose_secret_word()
            else:
                exit()
    if str(indicating_text) == secret_word:
        choice = messagebox.askyesno("Guess the Word",
                                     str("Congratulations! You have won!!!!\nThe Word was " + secret_word + ". Play Again?"))
        if choice:
            choose_secret_word()
        else:
            exit()


def choose_secret_word():
    global secret_word, indicating_text, indicating_label, turns_count
    secret_word = choice(word_list)
    turns_count = 8
    turns_label['text'] = 'Turns Left: ' + str(turns_count)
    input_box.delete(0, END)
    indicating_text = ""
    for n in secret_word:
        indicating_text = str(indicating_text) + '-'
    indicating_label.configure(text=str(indicating_text))


root = Tk()
root.title("Guess the Word | by Maaz")
# root.state('zoomed')
root.geometry("500x500")
root.configure(bg="light green")
root.resizable(False, False)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.bind("<Return>", check_guess)

# Defining Objects
indicating_label = Label(root, bg=bg_color, fg='Purple', font=("Times", 40))
rules_label = Label(root, text=rules_text, bg=bg_color, fg='#0000d0', font=("Ariel", 10))
Label(root, font=("Constancia", 25), text='Your Guess →  ', bg=bg_color, fg='Blue').place(x=50,
                                                                                          y=100)
input_box = Entry(root, font=('Ariel', 25), bg=bg_color, fg=fg_color, width=2, border=0.5)
turns_label = Label(root, bg=bg_color, fg='Red', font=("Constancia", 20))
turns_label.place(x=20, y=20)
play_again_button = Button(root, text='Play Again', font=('Ariel', 15), borderwidth=1, bg='Light Blue', fg=fg_color,
                           width=20)
go_button = Button(root, text="GO", font=("Constancia", 15), bg='#3c3f41', fg=bg_color, activebackground='#2b2b2b',
                   activeforeground="white", command=lambda: check_guess(0))

choose_secret_word()

# Placing Objects
indicating_label.place(x=160, y=screen_height - 340)
rules_label.place(x=10, y=200)
go_button.place(x=380, y=100)
go_button.configure(relief='ridge')

input_box.place(x=300, y=100)
input_box.configure(relief='solid')
input_box.bind("<KeyRelease>", entry_focused)

root.mainloop()
