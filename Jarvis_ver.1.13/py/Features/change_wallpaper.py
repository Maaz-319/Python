import ctypes, os, random, pyautogui
from talk import talk
files_dir = "C:\\Users\\Maaz\\Pictures\\Saved Pictures\\Wallpapers"
# files_dir = 'C:\\Users\\Maaz\\Documents\\Tempinstl\\empty'
files_list = os.listdir(files_dir)
try:
	file = random.choice(files_list)
	path = os.path.join(files_dir, file)
	# path = "your_wallpaper_path"
	SPI_SETDESKWALLPAPER = 20
	ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , 0)
	talk("How about this one.")
	pyautogui.keyDown('win')
	pyautogui.press('d')
	pyautogui.keyUp('win')
	print('\nIf you want to change it again say "Change Wallpaper"')
	input("Press Enter to continue....")
except IndexError:
	print('No Wallpapers found "C:/Users/Maaz/Pictures/Saved Pictures/Wallpapers"')
	talk('No Wallpapers found! download some wallpapers in this Folder.')