import pyautogui
from talk import talk

print("\n\nTaking Screenshot")
talk("Taking screenshot")
img = pyautogui.screenshot()
img.save(r"C:/Users/Maaz/Desktop/Jarvis_capture.png")
print("Done.")
talk("screenshot successfully saved to desktop Sir.")