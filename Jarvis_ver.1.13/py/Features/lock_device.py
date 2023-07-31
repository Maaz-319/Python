from talk import talk
import ctypes

talk("locking the device")
ctypes.windll.user32.LockWorkStation()
talk("locked")
input("Enter to continue.")