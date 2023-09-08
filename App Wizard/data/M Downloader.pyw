from tkinter import font
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import threading
from pytube import YouTube
import pyperclip
import subprocess
from urllib import request
import requests
import os
from random import randint
import re

# variables
black_bg_color = "#212325"
font_color = "#ffffff"
resolution = '360p'
resolutions = ['144p', '240p', '360p', '480p', '720p', '1080p']
download_path = "M-Downloads/"
video_stream = ""
link = ""
online = False
check_only_audio = False
title = ""
download_check_list = []
file_dir = "M-Downloads/"
rename = ""

def at_startup():
	global file_dir, rename
	files = os.listdir(file_dir)
	rename = 'download' + str(randint(0, 100000))
	for file in files:
		while rename == file:
			rename = 'download' + str(randint(0, 100000))


try:
    requests.post('https://www.google.com/')
    online = True
except:
    online = False


def paste_link():
	temp = pyperclip.paste()
	url_entry.delete(0, END)
	url_entry.insert(0, temp)


def show_download_folder():
	subprocess.Popen(r'explorer /open,"M-Downloads"')


def clean_filename(title):
    # Define a regex pattern to match unsupported characters
    unsupported_chars_pattern = r'[<>:"/\\|?*]'
    
    # Remove unsupported characters from the title using re.sub
    clean_title = re.sub(unsupported_chars_pattern, '', title)    
    return clean_title


def select_resolution(res):
	global resolution
	resolution = res


def on_progress(stream, chunk, bytes_remaining):
	global video_stream
	file_size = video_stream.filesize
	downloaded_size = file_size - bytes_remaining
	progress = (downloaded_size / file_size) * 100
	downloaded_size = round((downloaded_size/1000000), 1)
	percentage_complete_label['text'] = "Downloaded: " + str(int(progress)) + "%   (" + str(downloaded_size) + "Mb)"
	progress_bar['value'] = progress  # Update the progress bar
	root.update_idletasks()


def get_download_info():
	global resolution, link, video_stream, check_only_audio, title, resolutions
	download_button['state'] = 'disabled'
	audio_checkbox['state'] = 'disabled'
	link = str(url_entry.get())
	progress_label.configure(text="Fetching video info...")
	progress_label.place(x=190, y=235)
	try:
		yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
	except:
		messagebox.showerror("M | Downloader", "Wrong URL!")
		download_button['state'] = 'normal'
		audio_checkbox['state'] = 'normal'
		progress_label['text'] = ""
		download_button['text'] = "Fetch Info"
		download_button['command'] = lambda: download_set(0)
		return
	yt.register_on_progress_callback(on_progress)
	title = yt.streams[0].title
	title = clean_filename(title)
	vid_titl = title
	if len(vid_titl) > 30:
		vid_titl = vid_titl[:30]
	title_label['text'] = "Title: " + str(vid_titl) + '.....'
	if var.get() == 1:
		check_only_audio = True
		video_stream = yt.streams.filter(only_audio=check_only_audio).first()
	else:
		check_only_audio = False
		video_stream = yt.streams.filter(res=resolution, file_extension='mp4').first()
		
		# Check for available resolutions
		resolution =[int(i.split("p")[0]) for i in (list(dict.fromkeys([i.resolution for i in yt.streams if i.resolution])))]
		resolutions.sort(reverse=True)
		selected_option.set(resolutions[0])
		option_menu = OptionMenu(root, selected_option, *resolutions, command=select_resolution)
		option_menu.config(font=custom_font, bg=black_bg_color, fg=font_color, borderwidth=0, activebackground=black_bg_color, activeforeground=font_color)
		option_menu.place(x=215, y=130)
	download_button['state'] = 'normal'
	progress_label['text'] = ''
	progress_label.place(x=170, y=235)


def download():
	global video_stream, check_only_audio, download_check_list, rename
	download_button['state'] = 'disabled'
	file_size = video_stream.filesize_kb
	if file_size >= 1000:
		file_size /= 1000
		size_label['text'] = "Size: " + str(round(file_size, 1)) + " MB"
	else:
		size_label['text'] = "Size: " + str(round(file_size, 1)) + " KB"

	progress_bar['value'] = 0
	progress_label['text'] = "Downloading! Please wait..."
	try:
		video_stream.download(output_path=download_path, filename=rename+'.mp4')
	except:
		messagebox.showerror("M | Downloader", "Error while download\nCheck Internet")
		download_button['state'] = 'normal'
		download_button['text'] = 'Fetch Info'
		audio_checkbox['state'] = 'normal'
		download_button['command'] = lambda: download_set(0)
		progress_label['text'] = ""
		title_label['text'] = ""
		size_label['text'] = ""
		return
	if check_only_audio:
		temp = rename + '.mp4'
		audio_title = temp.replace('.mp4', '.mp3').replace(rename, title)
		os.rename("M-Downloads/"+temp, "M-Downloads/"+audio_title)
	else:
		temp = rename + '.mp4'
		video_title = temp.replace(rename, title)
		os.rename("M-Downloads/"+temp, "M-Downloads/"+video_title)
	progress_label.place(x=190, y=235)
	progress_label['text'] = "Download Complete"
	audio_checkbox['state'] = 'normal'
	download_button['state'] = 'normal'
	download_button['text'] = 'Fetch Info'
	download_button['command'] = lambda: download_set(0)
	percentage_complete_label['text'] = ""
	progress_bar['value'] = 0

def download_set(instruction):
	if not online:
		messagebox.showerror("M | Downloader", "Check Internet Connection!")
		return
	if instruction == 0:
		t1 = threading.Thread(target=get_download_info)
		t1.start()	
		download_button.configure(text="Download")
		download_button.configure(command=lambda: download_set(1))
	else:
		t2 = threading.Thread(target=download)
		t2.start()


root = Tk()
root.configure(bg=black_bg_color)
root.geometry('500x300')
root.resizable(False, False)
root.title("YouTube Downloader | By Maaz")

style = ttk.Style()
style.theme_use("default")

at_startup()

# Url_Entry_box
Label(root, text='Url:-', font=('Ariel', 15), bg=black_bg_color, fg=font_color).place(x=10, y=30)
url_entry = Entry(root, font=('ariel', 10, 'bold'), width=60, bg=font_color, fg=black_bg_color)
url_entry.place(x=55, y=35)

# Select_Resolution(Label and Menu)
Label(root, text='Resolution:-', font=('Ariel', 15), bg=black_bg_color, fg=font_color).place(x=200, y=100)
selected_option = StringVar(root)
custom_font = font.Font(family="Arial", size=12)
# option_menu = OptionMenu(root, selected_option, *resolutions, command=select_resolution)

# Download_Button
download_button = Button(root, text="Fetch Info", font=("ariel", 20), bg="#006400", fg=font_color, borderwidth=0, activebackground="#023b02", activeforeground=font_color, command=lambda: download_set(0))
download_button.place(x=185, y=180)

# Progress_Bar
style.configure("Cool.Horizontal.TProgressbar",
                background="#39FF14",  # Color of the progress bar background
                troughcolor="#3d3f42",  # Color of the trough (empty part) of the progress bar
                thickness=10,
                borderwidth=0)
progress_bar = ttk.Progressbar(root, orient="horizontal", length=480, mode="determinate", style="Cool.Horizontal.TProgressbar")
progress_bar.place(x=10, y=280)

progress_label = Label(root, font=('Ariel', 10), bg=black_bg_color, fg=font_color)
progress_label.place(x=190, y=235)

# Video_Info_Labels
title_label = Label(root, font=('Ariel', 10), bg=black_bg_color, fg=font_color)
percentage_complete_label = Label(root, font=('Ariel', 10), bg=black_bg_color, fg=font_color)
size_label = Label(root, font=('Ariel', 10), bg=black_bg_color, fg=font_color)
title_label.place(x=10, y=60)
size_label.place(x=10, y=80)
percentage_complete_label.place(x=10, y=258)


# Show_download_folder
show_downloads_button = Button(root, text='Downloads', font=("ariel", 10), bg="#171626", fg=font_color, borderwidth=0, activebackground="#023b02", activeforeground=font_color, command=show_download_folder)
show_downloads_button.place(x=420, y=250)

# Paste_Button
paste_button = Button(root, text='Paste Link', font=("ariel", 10), bg="#171626", fg=font_color, borderwidth=0, activebackground="#023b02", activeforeground=font_color, command=paste_link)
paste_button.place(x=410, y=60)

# Only_Audio_checkbutton
var = IntVar()
var.set(0)
audio_checkbox = Checkbutton(root, text='Only Audio', variable=var, onvalue=1, offvalue=0, bg=black_bg_color, highlightbackground=black_bg_color, fg='green')
audio_checkbox.place(x=400, y=100)

root.mainloop()