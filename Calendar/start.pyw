from tkinter import *
import calendar
from tkinter import messagebox

root = Tk()
root.title("Calendar | By Maaz")
root.configure(background="Light Green")
root.resizable(False, False)
root.geometry("300x300")

# new root

def all_months_calendar():
	try:
		global year
		year = int(entry.get())
	except:
		messagebox.showerror("Calendar", "Enter Correct Year")

	if year < 1500:
		messagebox.showerror("Calendar", "Minimum year you can see is 1500")
	elif year >= 1500:

		# give labels a month

		calendara1 = calendar.month(year, 1)
		calendara2 = calendar.month(year, 2)
		calendara3 = calendar.month(year, 3)
		calendara4 = calendar.month(year, 4)
		calendara5 = calendar.month(year, 5)
		calendara6 = calendar.month(year, 6)
		calendara7 = calendar.month(year, 7)
		calendara8 = calendar.month(year, 8)
		calendara9 = calendar.month(year, 9)
		calendara10 = calendar.month(year, 10)
		calendara11 = calendar.month(year, 11)
		calendara12 = calendar.month(year, 12)
		
		# new window

		new_root = Toplevel()
		new_root.state("zoomed")
		title = "Calendar of year " + str(year)
		new_root.title(title)

		# Defining Labels

		l1 = Label(new_root,text=calendara1, background="Pink", font=("Consolas", 14), borderwidth=1, relief="solid", foreground="black")
		l2 = Label(new_root,text=calendara2, background="Pink", font=("Consolas", 14), borderwidth=1, relief="solid", foreground="black")
		l3 = Label(new_root,text=calendara3, background="Pink", font=("Consolas", 14), borderwidth=1, relief="solid", foreground="black")
		l4 = Label(new_root,text=calendara4, background="Pink", font=("Consolas", 14), borderwidth=1, relief="solid", foreground="black")
		l5 = Label(new_root,text=calendara5, background="Pink", font=("Consolas", 14), borderwidth=1, relief="solid", foreground="black")
		l6 = Label(new_root,text=calendara6, background="Pink", font=("Consolas", 14), borderwidth=1, relief="solid", foreground="black")
		l7 = Label(new_root,text=calendara7, background="Pink", font=("Consolas", 14), borderwidth=1, relief="solid", foreground="black")
		l8 = Label(new_root,text=calendara8, background="Pink", font=("Consolas", 14), borderwidth=1, relief="solid", foreground="black")
		l9 = Label(new_root,text=calendara9, background="Pink", font=("Consolas", 14), borderwidth=1, relief="solid", foreground="black")
		l10 = Label(new_root,text=calendara10, background="Pink", font=("Consolas", 14), borderwidth=1, relief="solid", foreground="black")
		l11 = Label(new_root,text=calendara11, background="Pink", font=("Consolas", 14), borderwidth=1, relief="solid", foreground="black")
		l12 = Label(new_root,text=calendara12, background="Pink", font=("Consolas", 14), borderwidth=1, relief="solid", foreground="black")

		# Positioning Labels

		l1.grid(row=0,column=0, pady=30, padx=10)
		l2.grid(row=0,column=1, pady=30, padx=10)
		l3.grid(row=0,column=2, pady=30, padx=10)
		l4.grid(row=0,column=3, pady=30, padx=10)
		l5.grid(row=0,column=4, pady=30, padx=10)
		l6.grid(row=0,column=5, pady=30, padx=10)
		l7.grid(row=1,column=0, pady=30, padx=10)
		l8.grid(row=1,column=1, pady=30, padx=10)
		l9.grid(row=1,column=2, pady=30, padx=10)
		l10.grid(row=1,column=3, pady=30, padx=10)
		l11.grid(row=1,column=4, pady=30, padx=10)
		l12.grid(row=1,column=5, pady=30, padx=10)

	else:
		messagebox.showerror("Calendar", "There was an error while getting calendar")

# root

label  = Label(root,text="Enter Year", background="Light Green", font=("Ariel", 20, "underline"))
label.pack(pady=10)

entry = Entry(font=("Ariel", 19), foreground="Green")
entry.pack()

button = Button(text="Show Calendar", foreground="Red", font=("Ariel", 20), command = all_months_calendar, background="Pink")
button.pack(pady=30)

root.mainloop()