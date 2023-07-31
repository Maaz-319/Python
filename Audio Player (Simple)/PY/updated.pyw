from mutagen import File
import threading
from tkinter import *
import pyautogui
from PIL import Image, ImageTk
from tkinter import filedialog
from pygame import mixer
from tkinter import ttk
import os

length = 0
file_dir = None
music_list = []
mixer.init()
filed = None
file = None


def preload(listbox):
    global file_dir, music_list, file
    mixer.music.set_volume(0.5)
    volume = int(mixer.music.get_volume() * 100)
    volume_scale.set(volume)
    file = open('files/data/selected_folder.txt', 'r')
    file_dir = file.readline()
    file.close()
    if file_dir:
        try:
            files = os.listdir(file_dir)
        except FileNotFoundError:
            file = open('files/data/selected_folder.txt', 'w')
            exit()
        music_list = [file for file in files if file.endswith((".mp3", ".wav"))]
        for file in music_list:
            listbox.insert(END, file)
        listbox.config(height=20)
        listbox.place(x=1100, y=50)


def volume_slide_handle(vol):
    mixer.music.set_volume(float(vol) / 100)


def volume_up(_):
    mixer.music.set_volume((mixer.music.get_volume() + 0.1))
    volume = int(mixer.music.get_volume() * 100)
    volume_scale.set(volume)


def volume_down(_):
    mixer.music.set_volume((mixer.music.get_volume() - 0.1))
    volume = int(mixer.music.get_volume() * 100)
    volume_scale.set(volume)
    # volume_label['text'] = mixer.music.get_volume()


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

    Label(temp, text='Play/Pause : P\nLoad Music : SpaceBar\nVolume Up : Arrow Up\nVolume Down : Arrow Down',
          font=('Times', 20)).pack(pady=10)

    temp.mainloop()


def audio_info_process():
    global length, filed, file
    length = filed.get_length()
    audio = File(file)
    artist = audio.get('TPE1', 'Unknown')
    album = audio.get('TALB', 'Unknown')
    genre = audio.get('TCON', 'Unknown')
    name = os.path.basename(file)
    length_min = length // 60
    length_sec = length % 60
    duration_label['text'] = "Duration: {:2d}.{:02d} min".format(int(length_min), int(length_sec))
    ending_label['text'] = "{:02d}:{:02d}".format(int(length_min), int(length_sec))
    name_label['text'] = 'Now Playing:  ' + name.replace(".mp3", "").replace(".wav", "")
    path_label['text'] = 'Path:  ' + '"' + file_dir + '"'
    album_label['text'] = "Album: " + str(album)
    artist_label['text'] = "Artist: " + str(artist)
    genre_label['text'] = "Genre: " + str(genre)
    progress()


def progress():
    global length
    music_progress = abs((mixer.music.get_pos() / 1000) / length * 100)
    current_position = (abs(mixer.music.get_pos()) / 1000)
    sec = current_position % 60
    minu = current_position // 60
    current_position = "{:02d}:{:02d}".format(int(minu), int(sec))
    current_progress_label['text'] = current_position
    progress_bar['value'] = int(music_progress)
    root.after(100, progress)


def select_file():
    # volume_label['text'] = mixer.music.get_volume()
    global file_dir, music_list
    new_file_dir = filedialog.askdirectory()
    if new_file_dir:
        file_dir = new_file_dir
        file = open('files/data/selected_folder.txt', 'w')
        file.write(file_dir)
        file.close()
        files = os.listdir(file_dir)
        music_list = [file for file in files if file.endswith((".mp3", ".wav"))]
        listbox.delete(0, 'end')
        for file in music_list:
            listbox.insert(END, file)
        listbox.config(height=20)
        listbox.place(x=1100, y=50)


def play_list_mus(_):
    global filed, file
    selected_entry = listbox.curselection()
    if selected_entry:
        file = os.path.join(file_dir, music_list[selected_entry[0]])
        mixer.music.load(file)
        filed = mixer.Sound(file)
        audio_info_process()
        mixer.music.play()


def pause_music():
    if mixer.music.get_busy():
        mixer.music.pause()
    else:
        mixer.music.unpause()


def stop_music():
    mixer.music.stop()
    name_label['text'] = ''
    duration_label['text'] = ''
    path_label['text'] = ''
    artist_label['text'] = ''
    genre_label['text'] = ''
    album_label['text'] = ''


def p_f_thread(_):
    t2 = threading.Thread(target=pause_music)
    t2.start()


def se_f_thread(_):
    t2 = threading.Thread(target=select_file)
    t2.start()


root = Tk()
root.title("M | Player")
root.state('zoomed')
root.resizable(False, False)
root.bind('<KeyPress-space>', se_f_thread)
root.bind('<KeyPress-p>', p_f_thread)
root.bind('<Up>', volume_up)
root.bind('<Down>', volume_down)
root.bind('<KeyPress-l>', play_list_mus)
# root.bind('<Right>', progress_forward)
# root.bind('<Left>', progress_backwards)

style = ttk.Style()
style.theme_use("default")

bg_img = PhotoImage(file='files/bg_img.png')
Label(image=bg_img).place(x=0, y=0, relheight=1, relwidth=1)

temp_play = Image.open("files/play.png")
temp_play = temp_play.resize((100, 100))
play_image = ImageTk.PhotoImage(temp_play)
play_button = Button(root, image=play_image, borderwidth=0, background="#110b17", activebackground="#110b17",
                     command=lambda:play_list_mus(0))
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

select_button = Button(root, text='Select Folder', fg="Black", activebackground="#3775be", activeforeground='#3775be',
                       bg='Light green', borderwidth=1, command=select_file)
select_button.place(x=1280, y=680)

style.configure("Cool.Horizontal.TProgressbar",
                background="#ffffff",  # Color of the progress bar background
                troughcolor="#3d3f42",  # Color of the trough (empty part) of the progress bar
                thickness=2,
                borderwidth=0)
progress_bar = ttk.Progressbar(root, orient="horizontal", length=1000, mode="determinate", style="Cool.Horizontal.TProgressbar")
progress_bar.place(x=170, y=580)

current_progress_label = Label(root, text='--:--', font=('Comic Sans MS', 14), fg='White', bg='#120f1a')
current_progress_label.place(x=100, y=565)

ending_label = Label(root, text='--:--', font=('Comic Sans MS', 14), fg='White', bg='#110e19')
ending_label.place(x=1180, y=565)

# volume_label = Label(root, font=('Comic Sans MS', 14), fg='white', bg='#110e19')
# volume_label.place(x=50, y=530)

name_label = Label(font=('Comic Sans MS', 15), fg='#39FF14', bg='#1e243a')
name_label.place(x=50, y=50)
duration_label = Label(root, font=('Comic Sans MS', 15), fg='#39FF14', bg='#1d2236')
duration_label.place(x=50, y=130)
path_label = Label(font=('Comic Sans MS', 15), fg='#39FF14', bg='#1b1e31')
path_label.place(x=50, y=210)
album_label = Label(font=('Comic Sans MS', 15), fg='#39FF14', bg='#191a2c')
album_label.place(x=50, y=290)
artist_label = Label(font=('Comic Sans MS', 15), fg='#39FF14', bg='#171626')
artist_label.place(x=50, y=370)
genre_label = Label(font=('Comic Sans MS', 15), fg='#39FF14', bg='#151321')
genre_label.place(x=50, y=450)

style.configure("Cool.Horizontal.TScale", background="#0e0b16", troughcolor="#3d3f59", sliderthickness=12, sliderlength=40, sliderrelief="groove")
# volume_scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, font=('Comic Sans MS',20), bg="#0e0b16", border=0, fg="white", sliderrelief='ridge', troughcolor='white', activebackground='#100d18', highlightbackground='#100d18', width=10, command=volume_slide_handle)
volume_scale = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=volume_slide_handle, style="Cool.Horizontal.TScale")
volume_scale.place(x=1200, y=620)

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Shortcuts", command=menu_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

Label(root, font=('Comic Sans MS', 15), text='-:Audio List:-', bg="#1d2238", fg='White').place(x=1150, y=10)
listbox = Listbox(root, selectmode=SINGLE, font=("Constancia", 15), bg='#1a1f32', border=0, fg='#FFFFFF', selectbackground='#2E7D32')
listbox.place(x=1100, y=50)
preload(listbox)

root.mainloop()
