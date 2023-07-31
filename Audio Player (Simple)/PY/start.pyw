"""import threading
from tkinter import *
import pyautogui
from PIL import Image, ImageTk
from tkinter import filedialog
from pygame import mixer
from tkinter import ttk

length = 0
file = None
mixer.init()


def volume_up(_):
    pyautogui.press('volumeup')


def volume_down(_):
    pyautogui.press('volumedown')


def progress_forward():
    current_pos = mixer.music.get_pos()
    mixer.music.pause()
    mixer.music.set_pos((current_pos + 10000) / 1000)
    mixer.music.unpause()
    progress()


def progress_backwards(_):
    current = mixer.music.get_pos() / 1000
    print(current)
    mixer.music.play(start=current - 20)
    progress()


def menu_command():
    temp = Toplevel()
    temp.resizable(False, False)
    temp.title('Shortcuts')

    Label(temp, text='Play : L\nPause : P\nLoad Music : SpaceBar\nVolume Up : Arrow Up\nVolume Down : Arrow Down',
          font=('Times', 20)).pack(pady=10)

    temp.mainloop()


def audio_info_process():
    global length, file
    name = str(file).split("/")
    duration_label['text'] = 'Duration:  ' + "%.2f" % (length / 60) + ' min'
    name_label['text'] = 'Now Playing:  ' + name[-1]
    path_label['text'] = 'Path:  ' + '"' + str(file) + '"'
    progress_bar['maximum'] = length
    progress()


def progress():
    global length
    music_progress = int((mixer.music.get_pos() / 1000) / length * 100)
    progress_bar['value'] = music_progress
    root.after(1000, progress)


def select_file():
    global length, file
    # file = mixer.Sound(filedialog.askopenfilename())
    file = filedialog.askopenfilename()
    mixer.music.load(file)
    filed = mixer.Sound(file)
    mixer.music.play()
    length = filed.get_length()
    audio_info_process()


def play_music():
    mixer.music.unpause()


def pause_music():
    mixer.music.pause()


def stop_music():
    mixer.music.stop()
    name_label['text'] = ''
    duration_label['text'] = ''
    path_label['text'] = ''


# functions for binding keys
def p_f_thread(_):
    t2 = threading.Thread(target=pause_music)
    t2.start()


def se_f_thread(_):
    t2 = threading.Thread(target=select_file)
    t2.start()


def pl_f_thread(_):
    t2 = threading.Thread(target=play_music)
    t2.start()


# bg_color = '#007e7d'

root = Tk()
# root.configure(bg=bg_color)
# root.geometry('600x500')
root.title("M|Player")
root.state('zoomed')
root.resizable(False, False)
root.bind('<KeyPress-space>', se_f_thread)
root.bind('<KeyPress-l>', pl_f_thread)
root.bind('<KeyPress-p>', p_f_thread)
# root.bind('<Right>', progress_forward)
# root.bind('<Left>', progress_backwards)
root.bind('<Up>', volume_up)
root.bind('<Down>', volume_down)

bg_img = PhotoImage(file='files/bg_img.png')
Label(image=bg_img).place(x=0, y=0, relheight=1, relwidth=1)
# # play button
temp_play = Image.open("files/play.png")
temp_play = temp_play.resize((100, 100))
play_image = ImageTk.PhotoImage(temp_play)
play_button = Button(root, image=play_image, borderwidth=0, background="#110b17", activebackground="#110b17",
                     command=play_music)
play_button.place(x=600, y=610)

# pause button
temp_pause = Image.open("files/pause.png")
temp_pause = temp_pause.resize((100, 100))
pause_image = ImageTk.PhotoImage(temp_pause)
pause_button = Button(root, image=pause_image, borderwidth=0, background="#110b17", activebackground="#110b17",
                      command=pause_music)
pause_button.place(x=450, y=610)

# stop button
temp_stop = Image.open("files/stop.png")
temp_stop = temp_stop.resize((100, 100))
stop_image = ImageTk.PhotoImage(temp_stop)
stop_button = Button(root, image=stop_image, borderwidth=0, background="#110b17", activebackground="#110b17",
                     command=stop_music)
stop_button.place(x=750, y=610)

select_button = Button(root, text='Select file', fg="Black", activebackground="#3775be", activeforeground='#3775be',
                       bg='Light green', borderwidth=1, command=select_file)
select_button.place(x=1300, y=680)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=1340, mode="determinate")
progress_bar.place(x=13, y=570)

# audio-info display
name_label = Label(font=('Comic Sans MS', 15), fg='white', bg='#1e243a')
name_label.place(x=50, y=100)
duration_label = Label(font=('Comic Sans MS', 15), fg='white', bg='#1b2034')
duration_label.place(x=50, y=180)
path_label = Label(font=('Comic Sans MS', 15), fg='white', bg='#1a1d30')
path_label.place(x=50, y=260)

# icon = Image.open('files/icon.png')
# icon = icon.resize((200, 200))
# icon1 = ImageTk.PhotoImage(icon)
# Label(image=icon1, bg='#1b2033').place(x=1100, y=50)

# top menu
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Shortcuts", command=menu_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

playback_speed = DoubleVar(value=1.0)
# Label(text='Playback Speed:', font=('Comic Sans MS', 10), background='#14121d', foreground='white').place(x=10, y=500)
# speed_scale = Scale(root, from_=0.5, to=2.0, resolution=0.1, orient=HORIZONTAL, variable=playback_speed,
#                     background='#14121d', foreground='White', activebackground='#14121d', highlightbackground='#14121d',
#                     borderwidth=0)
# speed_scale.place(x=126, y=484)

root.mainloop()
"""


"""import threading
from tkinter import *
import pyautogui
from PIL import Image, ImageTk
from tkinter import filedialog
from pygame import mixer
from tkinter import ttk

length = 0
file = None
mixer.init()


def volume_up(_):
    pyautogui.press('volumeup')


def volume_down(_):
    pyautogui.press('volumedown')


def progress_forward():
    current_pos = mixer.music.get_pos()
    mixer.music.pause()
    mixer.music.set_pos((current_pos + 10000) / 1000)
    mixer.music.unpause()
    progress(length)


def progress_backwards(_):
    current = mixer.music.get_pos() / 1000
    print(current)
    mixer.music.play(start=current - 20)
    progress(length)


def menu_command():
    temp = Toplevel()
    temp.resizable(False, False)
    temp.title('Shortcuts')

    Label(temp, text='Play : L\nPause : P\nLoad Music : SpaceBar\nVolume Up : Arrow Up\nVolume Down : Arrow Down',
          font=('Times', 20)).pack(pady=10)

    temp.mainloop()


def audio_info_process():
    global length, file
    name = file.split("/")[-1]
    duration_label['text'] = 'Duration:  ' + "%.2f" % (length / 60) + ' min'
    name_label['text'] = 'Now Playing:  ' + name
    path_label['text'] = 'Path:  ' + '"' + file + '"'
    progress_bar['maximum'] = length * 1000  # Multiply the length by 1000 to match the progress bar range
    progress(length)


def progress(length):
    current_pos = mixer.music.get_pos() // 1000  # Get the current position in seconds
    music_progress = int((current_pos / length) * 100)  # Calculate the progress percentage
    progress_bar['value'] = music_progress
    if current_pos < length:
        root.after(1000, progress, length)  # Call the function again after 1 second


def select_file():
    global length, file
    file = filedialog.askopenfilename()
    mixer.music.load(file)
    filed = mixer.Sound(file)
    mixer.music.play()
    length = filed.get_length()
    audio_info_process()


def play_music():
    mixer.music.unpause()


def pause_music():
    mixer.music.pause()


def stop_music():
    mixer.music.stop()
    name_label['text'] = ''
    duration_label['text'] = ''
    path_label['text'] = ''


# functions for binding keys
def p_f_thread(_):
    t2 = threading.Thread(target=pause_music)
    t2.start()


def se_f_thread(_):
    t2 = threading.Thread(target=select_file)
    t2.start()


def pl_f_thread(_):
    t2 = threading.Thread(target=play_music)
    t2.start()


root = Tk()
root.title("M|Player")
root.state('zoomed')
root.resizable(False, False)
root.bind('<KeyPress-space>', se_f_thread)
root.bind('<KeyPress-l>', pl_f_thread)
root.bind('<KeyPress-p>', p_f_thread)
root.bind('<Up>', volume_up)
root.bind('<Down>', volume_down)

bg_img = PhotoImage(file='files/bg_img.png')
Label(image=bg_img).place(x=0, y=0, relheight=1, relwidth=1)

temp_play = Image.open("files/play.png")
temp_play = temp_play.resize((100, 100))
play_image = ImageTk.PhotoImage(temp_play)
play_button = Button(root, image=play_image, borderwidth=0, background="#110b17", activebackground="#110b17",
                     command=play_music)
play_button.place(x=600, y=610)

temp_pause = Image.open("files/pause.png")
temp_pause = temp_pause.resize((100, 100))
pause_image = ImageTk.PhotoImage(temp_pause)
pause_button = Button(root, image=pause_image, borderwidth=0, background="#110b17", activebackground="#110b17",
                      command=pause_music)
pause_button.place(x=450, y=610)

temp_stop = Image.open("files/stop.png")
temp_stop = temp_stop.resize((100, 100))
stop_image = ImageTk.PhotoImage(temp_stop)
stop_button = Button(root, image=stop_image, borderwidth=0, background="#110b17", activebackground="#110b17",
                     command=stop_music)
stop_button.place(x=750, y=610)

select_button = Button(root, text='Select file', fg="Black", activebackground="#3775be", activeforeground='#3775be',
                       bg='Light green', borderwidth=1, command=select_file)
select_button.place(x=1300, y=680)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=1340, mode="determinate")
progress_bar.place(x=13, y=570)

name_label = Label(font=('Comic Sans MS', 15), fg='white', bg='#1e243a')
name_label.place(x=50, y=100)
duration_label = Label(font=('Comic Sans MS', 15), fg='white', bg='#1b2034')
duration_label.place(x=50, y=180)
path_label = Label(font=('Comic Sans MS', 15), fg='white', bg='#1a1d30')
path_label.place(x=50, y=260)

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Shortcuts", command=menu_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

root.mainloop()
"""
import threading
from tkinter import *
import pyautogui
from PIL import Image, ImageTk
from tkinter import filedialog
from pygame import mixer
from tkinter import ttk

length = 0
file = None
mixer.init()


def volume_up(_):
    pyautogui.press('volumeup')


def volume_down(_):
    pyautogui.press('volumedown')


def progress_forward():
    current_pos = mixer.music.get_pos()
    mixer.music.pause()
    mixer.music.set_pos((current_pos + 10000) / 1000)
    mixer.music.unpause()
    progress()


def progress_backwards(_):
    current = mixer.music.get_pos() / 1000
    print(current)
    mixer.music.play(start=current - 20)
    progress()


def menu_command():
    temp = Toplevel()
    temp.resizable(False, False)
    temp.title('Shortcuts')

    Label(temp, text='Play : L\nPause : P\nLoad Music : SpaceBar\nVolume Up : Arrow Up\nVolume Down : Arrow Down',
          font=('Times', 20)).pack(pady=10)

    temp.mainloop()


def audio_info_process():
    global length, file
    name = str(file).split("/")
    duration_label['text'] = 'Duration:  ' + "%.2f" % (length / 60) + ' min'
    name_label['text'] = 'Now Playing:  ' + name[-1]
    path_label['text'] = 'Path:  ' + '"' + str(file) + '"'
    # progress_bar['maximum'] = length
    progress()


def progress():
    global length
    music_progress = int((mixer.music.get_pos() / 1000) / length * 100)
    progress_bar['value'] = music_progress
    root.after(1000, progress)


def select_file():
    global length, file
    # file = mixer.Sound(filedialog.askopenfilename())
    file = filedialog.askopenfilename()
    mixer.music.load(file)
    filed = mixer.Sound(file)
    mixer.music.play()
    length = filed.get_length()
    audio_info_process()


def play_music():
    mixer.music.unpause()


def pause_music():
    mixer.music.pause()


def stop_music():
    mixer.music.stop()
    name_label['text'] = ''
    duration_label['text'] = ''
    path_label['text'] = ''


# functions for binding keys
def p_f_thread(_):
    t2 = threading.Thread(target=pause_music)
    t2.start()


def se_f_thread(_):
    t2 = threading.Thread(target=select_file)
    t2.start()


def pl_f_thread(_):
    t2 = threading.Thread(target=play_music)
    t2.start()


# bg_color = '#007e7d'

root = Tk()
# root.configure(bg=bg_color)
# root.geometry('600x500')
root.title("M|Player")
root.state('zoomed')
root.resizable(False, False)
root.bind('<KeyPress-space>', se_f_thread)
root.bind('<KeyPress-l>', pl_f_thread)
root.bind('<KeyPress-p>', p_f_thread)
# root.bind('<Right>', progress_forward)
# root.bind('<Left>', progress_backwards)
root.bind('<Up>', volume_up)
root.bind('<Down>', volume_down)

bg_img = PhotoImage(file='files/bg_img.png')
Label(image=bg_img).place(x=0, y=0, relheight=1, relwidth=1)
# # play button
temp_play = Image.open("files/play.png")
temp_play = temp_play.resize((100, 100))
play_image = ImageTk.PhotoImage(temp_play)
play_button = Button(root, image=play_image, borderwidth=0, background="#110b17", activebackground="#110b17",
                     command=play_music)
play_button.place(x=600, y=610)

# pause button
temp_pause = Image.open("files/pause.png")
temp_pause = temp_pause.resize((100, 100))
pause_image = ImageTk.PhotoImage(temp_pause)
pause_button = Button(root, image=pause_image, borderwidth=0, background="#110b17", activebackground="#110b17",
                      command=pause_music)
pause_button.place(x=450, y=610)

# stop button
temp_stop = Image.open("files/stop.png")
temp_stop = temp_stop.resize((100, 100))
stop_image = ImageTk.PhotoImage(temp_stop)
stop_button = Button(root, image=stop_image, borderwidth=0, background="#110b17", activebackground="#110b17",
                     command=stop_music)
stop_button.place(x=750, y=610)

select_button = Button(root, text='Select file', fg="Black", activebackground="#3775be", activeforeground='#3775be',
                       bg='Light green', borderwidth=1, command=select_file)
select_button.place(x=1300, y=680)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=1000, mode="determinate")
progress_bar.place(x=170, y=570)

# audio-info display
name_label = Label(font=('Comic Sans MS', 15), fg='white', bg='#1e243a')
name_label.place(x=50, y=100)
duration_label = Label(font=('Comic Sans MS', 15), fg='white', bg='#1b2034')
duration_label.place(x=50, y=180)
path_label = Label(font=('Comic Sans MS', 15), fg='white', bg='#1a1d30')
path_label.place(x=50, y=260)

# icon = Image.open('files/icon.png')
# icon = icon.resize((200, 200))
# icon1 = ImageTk.PhotoImage(icon)
# Label(image=icon1, bg='#1b2033').place(x=1100, y=50)

# top menu
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Shortcuts", command=menu_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

playback_speed = DoubleVar(value=1.0)
# Label(text='Playback Speed:', font=('Comic Sans MS', 10), background='#14121d', foreground='white').place(x=10, y=500)
# speed_scale = Scale(root, from_=0.5, to=2.0, resolution=0.1, orient=HORIZONTAL, variable=playback_speed,
#                     background='#14121d', foreground='White', activebackground='#14121d', highlightbackground='#14121d',
#                     borderwidth=0)
# speed_scale.place(x=126, y=484)

root.mainloop()
