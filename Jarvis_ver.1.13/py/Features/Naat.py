import os
from talk import talk

talk("Here you go Sir!")
Naat_dir = "C:\\Users\\Maaz\\Music\\Naat"
file = os.listdir(Naat_dir)
os.startfile(os.path.join(Naat_dir, file[1]))
input('Enter to continue')