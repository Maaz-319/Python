import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk, filedialog
import pygame
from mutagen.easyid3 import EasyID3

# Global Variables
new_song = None
directory = None

# Initialize Pygame mixer
pygame.mixer.init()


class song:
    def __init__(self, name, genre, album, artist, path, length):
        self.name = name
        self.genre = genre
        self.album = album
        self.artist = artist
        self.path = path
        self.length = length

        # Function to update song information

    def update_song_info(self):
        milliseconds = self.length * 1000
        seconds = milliseconds // 1000  # Convert to seconds
        minutes = seconds // 60  # Get the minutes part
        seconds %= 60  # Get the remaining seconds part

        song_name_label['text'] = self.name
        song_genre_label['text'] = self.genre
        song_album_label['text'] = self.album
        song_artist_label['text'] = self.artist
        song_path_label['text'] = self.path
        song_length_label['text'] = f"{int(minutes):02d}:{int(seconds):02d}"
        progress['maximum'] = self.length
        self.update_progress_bar()

    def update_progress_bar(self):
        milliseconds = pygame.mixer.music.get_pos()
        seconds = milliseconds // 1000  # Convert to seconds
        minutes = seconds // 60  # Get the minutes part
        seconds %= 60  # Get the remaining seconds part
        current_progress_label[
            'text'] = f"{minutes:02d}:{seconds:02d}"
        if pygame.mixer.music.get_busy():
            root.after(1000, self.update_progress_bar)
            progress['value'] = pygame.mixer.music.get_pos() / 1000
            if progress['value'] >= self.length or self.length - progress['value'] < 1:
                progress['value'] = 0
                current_progress_label['text'] = "--:--"

    # Function to play selected song
    def play_song(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load(self.path)
        pygame.mixer.music.play()
        self.update_song_info()


# Function to resume the song
def resume_song():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        resume_button['text'] = "▶️"
    else:
        pygame.mixer.music.unpause()
        try:
            new_song.update_progress_bar()
        except AttributeError:
            pass
        resume_button['text'] = "⏸️"


# Function to load audio files from a directory
def load_files():
    global directory
    directory = filedialog.askdirectory()
    if directory:
        with open('data.txt', 'w') as f:
            f.write(directory)
            f.close()
        listbox.delete(0, tk.END)
        for file in os.listdir(directory):
            if file.endswith(('.mp3', '.wav')):
                listbox.insert(tk.END, file)


def preload():
    global directory
    try:
        with open('data.txt', 'r') as f:
            directory = f.read()
            if directory:
                listbox.delete(0, tk.END)
                for file in os.listdir(directory):
                    if file.endswith(('.mp3', '.wav')):
                        listbox.insert(tk.END, file)
            f.close()
    except FileNotFoundError:
        pass


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        root.destroy()

#                               Author: Maaz Bin Asif
#                              instagram.com/maaz.binasif


def create_instance(_=None):
    global directory, new_song
    selected = listbox.curselection()
    if selected:
        selected = selected[0]
        selected = listbox.get(selected)
        try:
            audio = EasyID3(os.path.join(directory, selected))
        except:
            if messagebox.askokcancel("Error", "Error Playing the Song\nDo you want to reload the files?"):
                load_files()
            return
        new_song = song(str(selected).replace('.mp3', ''), audio.get("genre", ["Unknown"])[0],
                        audio.get("album", ["Unknown"])[0], audio.get("artist", ["Unknown"])[0],
                        os.path.join(directory, selected),
                        pygame.mixer.Sound(os.path.join(directory, selected)).get_length())

        new_song.play_song()


def volume_slide_handle(vol):
    pygame.mixer.music.set_volume(float(vol) / 100)
    volume_scale_label['text'] = f"{str(round(float(vol), 0)).replace('.0', '')}%"


def show_shortcut_info():
    messagebox.showinfo("Shortcut Keys", "Space: Play/Pause\n\nCtrl + O: Load Files\n\nP: Start Song")


# Create the main window
root = tk.Tk()
root.title("Modern Audio Player")
root.attributes('-fullscreen', True)  # Full screen mode
root.configure(bg="#1e1e1e")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.protocol("WM_DELETE_WINDOW", on_closing)

# Binding Shortcut Keys
root.bind("<space>", lambda event: resume_song())
root.bind("<Control-o>", lambda event: load_files())
root.bind("<p>", lambda event: create_instance())
# Author: Maaz Bin Asif
# instagram.com/maaz.binasif
# Apply a modern color scheme and fonts
font_large = ("Helvetica", 16, "bold")
font_medium = ("Helvetica", 14, 'italic')
font_small = ("Helvetica", 10)
color_primary = "#0d7377"
color_secondary = "#14ffec"
color_background = "#1e1e1e"
color_text = "#ffffff"
style = ttk.Style()
style.theme_use("default")
style.configure(
    "TButton",
    font=("Helvetica", 14, "bold"),  # Set the font
    foreground="black",  # Set the text color
    background="light green",  # Set the background color
    borderwidth=0,  # Set the border width
    focusthickness=1,  # Set the thickness of the focus indicator
    focuscolor="#14ffec",  # Set the focus indicator color
    padding=2,  # Set padding inside the button
    relief="flat",  # Set the relief style
    anchor="center",  # Set the anchor for the text within the button
)
style.map(
    "TButton",
    foreground=[("active", "black"), ("disabled", "#888888")],  # Set text color for active and disabled states
    background=[("active", "light green"), ("disabled", "#444444")],
    # Set background color for active and disabled states
    relief=[("pressed", "sunken"), ("!pressed", "flat")]  # Change relief based on pressed state
)
# ========================= Title Bar ============================
tk.Label(root, text="Music PLayer | By Maaz", font=("Comic Sans MS", 12, 'bold underline'), foreground="light green",
         background="#3d3f42", width=int(screen_width * 0.0999)).place(relx=0, rely=0.001, anchor="nw")
# ================================================================
# =============== Create the song information Preview ===============
# Song name label
ttk.Label(root, text="Song: ", font=font_large, foreground="light green",
          background=color_background).place(relx=0.01, rely=0.1, anchor="w")
song_name_label = ttk.Label(root, text="-", font=font_medium, foreground=color_text,
                            background=color_background)

ttk.Label(root, text="Genre: ", font=font_large, foreground="light green",
          background=color_background).place(relx=0.01, rely=0.2, anchor="w")
song_genre_label = ttk.Label(root, text="-", font=font_medium, foreground=color_text,
                             background=color_background)

ttk.Label(root, text="Album: ", font=font_large, foreground="light green",
          background=color_background).place(relx=0.01, rely=0.3, anchor="w")
song_album_label = ttk.Label(root, text="-", font=font_medium, foreground=color_text,
                             background=color_background)

ttk.Label(root, text="Artist: ", font=font_large, foreground="light green",
          background=color_background).place(relx=0.01, rely=0.4, anchor="w")
song_artist_label = ttk.Label(root, text="-", font=font_medium, foreground=color_text,
                              background=color_background)

ttk.Label(root, text="Path: ", font=font_large, foreground="light green",
          background=color_background).place(relx=0.01, rely=0.5, anchor="w")
song_path_label = ttk.Label(root, text="-", font=font_medium, foreground=color_text,
                            background=color_background)

# Placing the labels on the window
song_name_label.place(relx=0.1, rely=0.1, anchor="w")
song_genre_label.place(relx=0.1, rely=0.2, anchor="w")
song_album_label.place(relx=0.1, rely=0.3, anchor="w")
song_artist_label.place(relx=0.1, rely=0.4, anchor="w")
song_path_label.place(relx=0.1, rely=0.5, anchor="w")
# =================================================================

# =============== Create the song list Display ====================
# listbox
ttk.Label(root, text="Select a song to play", font=font_large, foreground=color_text,
          background=color_background).place(
    relx=0.85, rely=0.05, anchor="n")
listbox = tk.Listbox(root, width=50, height=20, font=font_small, selectmode=tk.SINGLE, foreground=color_text,
                     background=color_background, selectbackground="light green", selectforeground="black",
                     highlightcolor="#444444", highlightthickness=1)
listbox.place(relx=0.99, rely=0.1, anchor="ne", height=screen_height - 100, width=350)
listbox.bind("<Double-Button-1>", create_instance)
# ================================================================

# =============== Create the buttons ============================
# Load files button
play_button = tk.Button(root, text="▶", command=create_instance, font=("Helvetica", 10, 'bold'), bg="light green",
                        fg="black", relief="flat", activebackground="light green", activeforeground="black",
                        justify="center", borderwidth=0, width=2)
resume_button = ttk.Button(root, text="⏸️", command=resume_song, style="TButton", width=3)
load_button = ttk.Button(root, text=" 📂", command=load_files, style="TButton", width=3)
close_button = tk.Button(root, text="❌", command=on_closing, width=3, bg="red", fg="black", relief="flat",
                         activebackground="purple", activeforeground="black", justify="center", borderwidth=0,
                         font=("Helvetica", 12, "bold"))
shortcut_info_button = ttk.Button(root, text="🔍", command=show_shortcut_info, style="TButton", width=3)
minimize_window_button = tk.Button(root, text="➖", width=3, bg=color_background, fg="white", relief="flat",
                                   activebackground="grey", activeforeground="black", justify="center",
                                   borderwidth=0, font=("Helvetica", 12, "bold"), command=lambda: root.iconify())

# Place the buttons on the window
load_button.place(relx=0.005, rely=0.992, anchor="sw")
play_button.place(relx=0.95, rely=0.05)
resume_button.place(relx=0.35, rely=0.95, anchor="center")
close_button.place(relx=1, rely=0.001, anchor="ne")
shortcut_info_button.place(relx=0, rely=0.001, anchor="nw")
minimize_window_button.place(relx=0.969, rely=0.001, anchor='ne')
# ===============================================================

# ================== Progress Bar ===============================
style.configure("Cool.Horizontal.TProgressbar",
                background="light green",  # Color of the progress bar background
                troughcolor="#3d3f42",  # Color of the trough (empty part) of the progress bar
                thickness=0,
                borderwidth=0)
progress = ttk.Progressbar(root, orient="horizontal", length=screen_width - 420, mode="determinate", value=0,
                           maximum=100, style="Cool.Horizontal.TProgressbar")
current_progress_label = ttk.Label(root, text="--:--", font=font_small, foreground=color_text,
                                   background=color_background)
song_length_label = ttk.Label(root, text="--:--", font=font_small, foreground=color_text, background=color_background)

# Placing Items
current_progress_label.place(relx=0.02, rely=0.93, anchor="w")
progress.place(relx=0.02, rely=0.9, anchor="w", height=8)
song_length_label.place(relx=0.686, rely=0.93, anchor='w')
# ===============================================================

# ================= Volume Bar ================================
volume_scale_label = ttk.Label(root, font=font_small, foreground=color_text,
                               background=color_background)
style.configure("Cool.Horizontal.TScale",
                background=color_background,  # Color of the scale background
                troughcolor="grey",  # Color of the trough (empty part) of the scale
                sliderthickness=12,
                sliderlength=10,
                sliderrelief="flat")
volume_scale = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=volume_slide_handle,
                         style="Cool.Horizontal.TScale")
volume_scale.place(relx=0.67, rely=0.85, anchor="center")
volume_scale.set(50)
volume_scale_label.place(relx=0.72, rely=0.85, anchor="center")
# =============================================================

preload()

# Run the Tkinter main loop
root.mainloop()
