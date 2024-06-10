= SPEC-001: Modern Audio Player
:sectnums:
:toc:


== Background

The Modern Audio Player is a desktop application designed to play audio files (MP3 and WAV formats) with a graphical user interface (GUI). It is built using Python's Tkinter library for the GUI and Pygame for audio playback. The application allows users to load songs from a directory, display song information, control playback, and adjust the volume.

== Requirements

*Must Have:*
- Ability to load audio files from a specified directory.
- Display song information such as name, genre, album, artist, path, and length.
- Play, pause, and resume audio playback.
- Show playback progress and song duration.
- Adjust the volume.

*Should Have:*
- Save the last used directory for easy access on the next launch.
- Provide keyboard shortcuts for common actions.

*Could Have:*
- Display a modern and visually appealing interface.
- Show shortcut keys information.

== Method

The application is structured into several key components and functions, detailed as follows:

=== Global Variables

The global variables include `new_song` to store the current song instance and `directory` to store the path of the loaded audio files.

[source,python]
----
new_song = None
directory = None
----

=== Pygame Initialization

Pygame's mixer is initialized to handle audio playback.

[source,python]
----
pygame.mixer.init()
----

=== Song Class

The `song` class encapsulates the properties of a song and includes methods to update song information, update the progress bar, and play the song.

[source,python]
----
class song:
    def __init__(self, name, genre, album, artist, path, length):
        self.name = name
        self.genre = genre
        self.album = album
        self.artist = artist
        self.path = path
        self.length = length

    def update_song_info(self):
        milliseconds = self.length * 1000
        seconds = milliseconds // 1000
        minutes = seconds // 60
        seconds %= 60

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
        seconds = milliseconds // 1000
        minutes = seconds // 60
        seconds %= 60
        current_progress_label['text'] = f"{minutes:02d}:{seconds:02d}"
        if pygame.mixer.music.get_busy():
            root.after(1000, self.update_progress_bar)
            progress['value'] = pygame.mixer.music.get_pos() / 1000
            if progress['value'] >= self.length or self.length - progress['value'] < 1:
                progress['value'] = 0
                current_progress_label['text'] = "--:--"

    def play_song(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load(self.path)
        pygame.mixer.music.play()
        self.update_song_info()
----

=== Functions

The application includes several functions to handle different aspects of its operation.

==== Resume Song

The `resume_song` function toggles between pausing and unpausing the song.

[source,python]
----
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
----

==== Load Files

The `load_files` function allows the user to select a directory and load audio files from it.

[source,python]
----
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
----

==== Preload

The `preload` function loads the previously used directory when the application starts.

[source,python]
----
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
----

==== On Closing

The `on_closing` function handles the closing event of the application, stopping and unloading the music.

[source,python]
----
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        root.destroy()
----

==== Create Instance

The `create_instance` function creates a new song instance based on the selected file and plays the song.

[source,python]
----
def create_instance():
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
----

==== Volume Slider Handle

The `volume_slide_handle` function adjusts the volume based on the slider's position.

[source,python]
----
def volume_slide_handle(vol):
    pygame.mixer.music.set_volume(float(vol) / 100)
    volume_scale_label['text'] = f"{str(round(float(vol), 0)).replace('.0', '')}%"
----

==== Show Shortcut Info

The `show_shortcut_info` function displays a message box with information about keyboard shortcuts.

[source,python]
----
def show_shortcut_info():
    messagebox.showinfo("Shortcut Keys", "Space: Play/Pause\n\nCtrl + O: Load Files\n\nP: Start Song")
----

=== GUI Setup

The GUI is created using Tkinter, with elements placed on the window using relative positioning.

[source,python]
----
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
----

==== Styles and Widgets

The application uses a modern color scheme and custom styles for widgets.

[source,python]
----
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
    font=("Helvetica", 14, "bold"),
    foreground="black",
    background="light green",
    borderwidth=0,
    focusthickness=1,
    focuscolor="#14ffec",
    padding=2,
    relief="flat",
    anchor="center",
)
style.map(
    "TButton",
    foreground=[("active", "black"), ("disabled", "#888888")],
    background=[("active", "light green"), ("disabled", "#444444")],
    relief=[("pressed", "sunken"), ("!pressed", "flat")]
)
# ========================= Title Bar ============================
tk.Label(root, text="Music Player | By Maaz", font=("Comic Sans MS", 12, 'bold underline'), foreground="light green",
         background="#3d3f42", width=int(screen_width * 0.0999)).place(relx=0, rely=0.001, anchor="nw")
# ================================================================
# =============== Create the song information Preview ===============
# Song name label
ttk.Label(root, text="Song: ", font=font_large, foreground="light green",
          background=color_background).place(relx=0.01, rely=0.1, anchor="w")
song_name_label = ttk.Label(root, text="-", font=font_medium, foreground=color_text,
                            background=color_background)
# Song genre label
ttk.Label(root, text="Genre: ", font=font_large, foreground="light green",
          background=color_background).place(relx=0.01, rely=0.2, anchor="w")
song_genre_label = ttk.Label(root, text="-", font=font_medium, foreground=color_text,
                             background=color_background)
# Song album label
ttk.Label(root, text="Album: ", font=font_large, foreground="light green",
          background=color_background).place(relx=0.01, rely=0.3, anchor="w")
song_album_label = ttk.Label(root, text="-", font=font_medium, foreground=color_text,
                             background=color_background)
# Song artist label
ttk.Label(root, text="Artist: ", font=font_large, foreground="light green",
          background=color_background).place(relx=0.01, rely=0.4, anchor="w")
song_artist_label = ttk.Label(root, text="-", font=font_medium, foreground=color_text,
                              background=color_background)
# Song path label
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
# ================================================================

# =============== Create the song list Display ====================
# listbox
ttk.Label(root, text="Select a song to play", font=font_large, foreground=color_text,
          background=color_background).place(
    relx=0.85, rely=0.05, anchor="n")
listbox = tk.Listbox(root, width=50, height=20, font=font_small, selectmode=tk.SINGLE, foreground=color_text,
                     background=color_background, selectbackground="light green", selectforeground="black",
                     highlightcolor="#444444", highlightthickness=1)
listbox.place(relx=0.99, rely=0.1, anchor="ne", height=screen_height - 100, width=350)
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
                background="light green",
                troughcolor="#3d3f42",
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
                background=color_background,
                troughcolor="grey",
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
----

== Implementation

The following steps outline the implementation process:

1. **Setup the Environment:**
   - Install necessary libraries: Tkinter, Pygame, and Mutagen.
   - Create a new Python file and add the provided code.

2. **Define the Global Variables:**
   - Initialize `new_song` and `directory`.

3. **Initialize Pygame Mixer:**
   - Add `pygame.mixer.init()` to initialize the mixer.

4. **Define the Song Class:**
   - Implement the `song` class with methods to update song info, update the progress bar, and play songs.

5. **Implement Functions:**
   - Define functions for resuming songs, loading files, preloading the directory, handling the window close event, creating song instances, handling volume slider, and showing shortcut info.

6. **Setup the GUI:**
   - Create the main window using Tkinter.
   - Apply styles and create necessary widgets such as labels, listbox, buttons, progress bar, and volume scale.

7. **Bind Shortcut Keys:**
   - Bind keys to corresponding functions for play/pause, load files, and start song.

8. **Run the Application:**
   - Call `root.mainloop()` to start the Tkinter main loop and run the application.

== Milestones

1. **Initial Setup:**
   - Install libraries and create the project structure.

2. **Basic Functionality:**
   - Implement loading, playing, pausing, and resuming songs.

3. **GUI Development:**
   - Design and implement the GUI with all necessary components.

4. **Testing and Debugging:**
   - Test the application thoroughly and fix any issues.

5. **Final Review:**
   - Perform a final review of the code and documentation.

== Gathering Results

To evaluate the performance and effectiveness of the application, consider the following criteria:

- The application should successfully load and play audio files.
- Song information should be correctly displayed.
- Playback controls (play, pause, resume) should work as expected.
- Volume adjustment should be smooth and responsive.
- The user interface should be intuitive and visually appealing.

Gather user feedback and monitor for any bugs or performance issues in real-world usage.
