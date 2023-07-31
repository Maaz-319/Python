import win32gui, win32con
the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

from plyer import notification #for getting notification on your PC

notification.notify(
    #title of the notification,
    title = "Maaz",
    message = "Test of desktop Notification \nSent from Python".format(
    timeout  = 50)
)
