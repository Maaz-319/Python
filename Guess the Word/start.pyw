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
category = None
rules_text = "─────────────────────\nRules:\n• Guess the Word Challenge •\n\n• You have to Enter your Guessed letter of the word in the box saying 'Your Guess.'\n• Only one letter is allowed at a time and you lose a turn on the wrong guess.         \n• After entering your guess, click on the 'Go' button or simply press the Enter key.  \n• The number of dashes at the bottom represents the length of the word to guess.   \n─────────────────────"
word_list = {
    'Vehicle': ['car', 'bus', 'bike', 'truck', 'train', 'motorcycle', 'scooter', 'helicopter', 'airplane', 'boat',
                'submarine', 'hovercraft', 'ambulance', 'bicycle', 'tractor', 'cruise', 'jeep', 'sailboat',
                'skateboard', 'yacht', 'firetruck', 'van', 'tank',
                'unicycle', 'spaceship', 'rickshaw', 'gondola', 'skis', 'rollerblades', 'jetski', 'forklift', 'sled',
                'golfcart', 'parachute', 'hangglider', 'bulldozer', 'snowmobile', 'rickshaw', 'zebra', 'tram', 'pogo',
                'trolley'],

    'Fruit': ['apple', 'banana', 'orange', 'strawberry', 'grape', 'watermelon', 'kiwi', 'pineapple', 'blueberry',
              'cherry', 'mango', 'papaya', 'pear', 'apricot', 'lemon', 'lime', 'peach', 'raspberry', 'coconut', 'guava',
              'date', 'blackberry', 'avocado', 'cantaloupe', 'currant', 'elderberry',
              'gooseberry', 'lychee', 'pomegranate', 'dragonfruit'],

    'Vegetable': ['carrot', 'broccoli', 'potato', 'tomato', 'cucumber', 'lettuce', 'zucchini', 'onion', 'pepper',
                  'mushroom', 'spinach', 'celery', 'asparagus', 'cauliflower', 'cabbage', 'eggplant', 'radish', 'okra',
                  'turnip', 'kale', 'artichoke', 'pea', 'squash', 'bean', 'sweetpotato', 'leek', 'brusselsprout',
                  'beet', 'corn', 'parsnip', 'garlic', 'rhubarb', 'pumpkin'],

    'Furniture': ['chair', 'table', 'sofa', 'bed', 'bookshelf', 'wardrobe', 'desk', 'cabinet', 'ottoman', 'diningtable',
                  'couch', 'stool', 'bench', 'couch', 'sectional', 'armchair', 'ottoman', 'sideboard', 'settee',
                  'hammock', 'tuffet', 'wardrobe', 'stool'],

    'Verb': ['run', 'jump', 'sing', 'dance', 'swim', 'read', 'write', 'talk', 'laugh', 'cry', 'eat', 'drink', 'sleep',
             'dream', 'think', 'climb', 'work', 'play', 'study', 'teach', 'drive', 'fly', 'ride', 'cook', 'bake',
             'draw', 'paint', 'ski', 'hike', 'skate', 'travel', 'build', 'clean', 'wash', 'listen', 'speak', 'shout',
             'whisper', 'buy', 'sell', 'meet', 'greet', 'help', 'smile', 'frown', 'apologize', 'forgive'],

    'Adjective': ['happy', 'sad', 'angry', 'excited', 'bored', 'tired', 'hungry', 'thirsty', 'scared', 'brave', 'shy',
                  'curious', 'proud', 'ashamed', 'surprised', 'confused', 'crazy', 'calm', 'energetic', 'lazy',
                  'friendly', 'lonely', 'lovely', 'ugly', 'handsome', 'beautiful', 'plain', 'smart', 'dumb', 'kind',
                  'mean', 'funny', 'serious', 'silly', 'quiet', 'loud', 'gentle', 'rough', 'soft', 'hard', 'smooth',
                  'sticky'],

    'Technology': ['computer', 'smartphone', 'tablet', 'laptop', 'keyboard', 'mouse', 'monitor', 'printer', 'router',
                   'modem', 'headphones', 'microphone', 'speaker', 'camera', 'console', 'smartwatch', 'drones',
                   'projector', 'harddrive', 'bluetooth', 'wearable', 'scanner',
                   'headset', 'flashdrive', 'chromecast', 'drone', 'hoverboard', 'robot', 'satellite',
                   'simcard', 'biometric', 'printer', 'joystick', 'motherboard',
                   'ethernet', 'touchscreen', 'videocard', 'webcam', 'microcontroller', 'teleportation'],
    'Animal': ['lion', 'tiger', 'elephant', 'giraffe', 'zebra', 'kangaroo', 'hippopotamus', 'cheetah', 'leopard',
               'panda', 'koala', 'wolf', 'fox', 'bear', 'gorilla', 'monkey', 'seal', 'jaguar'],
    'Bird': ['eagle', 'hawk', 'sparrow', 'robin', 'parrot', 'penguin', 'peacock', 'ostrich', 'flamingo', 'swan']
}


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
            choice = messagebox.askyesno("Guess the Word",
                                         str("You have lost!\nThe Word was " + secret_word + ". Better luck next time\nPlay Again?"))
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
    global secret_word, indicating_text, indicating_label, turns_count, category
    category = choice(list(word_list.keys()))
    secret_word = choice(word_list[category])
    category_label['text'] = category
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
Label(root, text="Category → ", bg=bg_color, fg='#3c3f41', font=("Times", 18)).place(x=120, y=270)
category_label = Label(root, bg=bg_color, fg='#3c3f41', font=("Times", 18, 'underline'))
rules_label = Label(root, text=rules_text, bg=bg_color, fg='#0000d0', font=("Ariel", 10))
Label(root, font=("Constancia", 25), text='Your Guess →  ', bg=bg_color, fg='Blue').place(x=50, y=100)
input_box = Entry(root, font=('Ariel', 25), bg=bg_color, fg=fg_color, width=2, border=0.5)
turns_label = Label(root, bg=bg_color, fg='Red', font=("Constancia", 20))
turns_label.place(x=20, y=20)
play_again_button = Button(root, text='Play Again', font=('Ariel', 15), borderwidth=1, bg='Light Blue', fg=fg_color,
                           width=20)
go_button = Button(root, text="GO", font=("Constancia", 15), bg='#3c3f41', fg=bg_color, activebackground='#2b2b2b',
                   activeforeground="white", command=lambda: check_guess(0))

choose_secret_word()

# Placing Objects
indicating_label.place(x=170, y=180)
category_label.place(x=250, y=270)
rules_label.place(x=10, y=350)
go_button.place(x=380, y=100)
go_button.configure(relief='ridge')

input_box.place(x=300, y=100)
input_box.configure(relief='solid')
input_box.bind("<KeyRelease>", entry_focused)

root.mainloop()
