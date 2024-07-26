import time
from tkinter import *
from functools import partial
from tkinter import messagebox
import database_handler as db


def create_new_student():
    if not new_student_name_entry.get() or not new_student_F_name_entry.get() or not new_student_phone_entry.get():
        messagebox.showerror("System", "Please fill all fields")
    else:
        student_name = str(new_student_name_entry.get())
        student_f_name = str(new_student_F_name_entry.get())
        student_name = student_name.upper()
        student_f_name = student_f_name.upper()

        # Check if phone number is correct
        student_phone = str(new_student_phone_entry.get())
        if len(str(student_phone)) != 11:
            messagebox.showerror("System", "Your Phone Number is incorrect")
        else:
            db.add_record(student_name, student_f_name, student_phone)
            new_student_name_entry.delete(0, END)
            new_student_F_name_entry.delete(0, END)
            new_student_phone_entry.delete(0, END)
            messagebox.showinfo("System", "Student Record Saved Successfully")


def create_find_students_via_roll_n():
    global enter_roll_number_entry
    main_page.destroy()
    roll_no_frame = Frame(root, width=1100, height=500, bg='Light Green')
    roll_no_frame.place(x=0, y=0)

    # animate
    roll_no_frame.place(x=1100, y=0)
    time.sleep(0.011)
    root.update()
    roll_no_frame.place(x=1000, y=0)
    time.sleep(0.011)
    root.update()
    roll_no_frame.place(x=900, y=0)
    time.sleep(0.011)
    root.update()
    roll_no_frame.place(x=800, y=0)
    time.sleep(0.011)
    root.update()
    roll_no_frame.place(x=700, y=0)
    time.sleep(0.011)
    root.update()
    roll_no_frame.place(x=600, y=0)
    time.sleep(0.011)
    root.update()
    roll_no_frame.place(x=500, y=0)
    time.sleep(0.011)
    root.update()
    roll_no_frame.place(x=400, y=0)
    time.sleep(0.011)
    root.update()
    roll_no_frame.place(x=300, y=0)
    time.sleep(0.011)
    root.update()
    roll_no_frame.place(x=200, y=0)
    time.sleep(0.011)
    root.update()
    roll_no_frame.place(x=100, y=0)
    time.sleep(0.011)
    root.update()
    roll_no_frame.place(x=0, y=0)
    root.update()

    # enter roll number label
    Label(roll_no_frame, text="Enter Roll Number", background="light green",
          font=("Microsoft YaHei UI Dark", 15)).place(x=350, y=100)

    # enter roll number entry
    enter_roll_number_entry = Entry(roll_no_frame, background="#fff", font=("Microsoft YaHei UI Dark", 10), width=30)
    enter_roll_number_entry.place(x=520, y=105)

    # enter roll number button
    Button(roll_no_frame, text="Find", background="pink",
           font=("Microsoft YaHei UI Dark", 15), width=10, borderwidth=1,
           command=find_students_via_roll_n).place(x=480, y=150)

    back_button = Button(roll_no_frame, text='←', bg='pink', fg='black', font=('Ariel', 12, 'bold'), width=10,
                         command=recreate_main_page)
    back_button.place(x=5, y=5)


def find_students_via_roll_n():
    recreate_main_page()
    # Find and display student if found
    fetch_data = int(enter_roll_number_entry.get())
    fetch_data = db.show_by_roll_no(fetch_data)
    if fetch_data:
        result = "Student Name: " + fetch_data[0][1] + "\n\nFather Name: " + fetch_data[0][2] + "\n\nRoll Number: " + str(fetch_data[0][0]) + "\n\nPhone Number: " + fetch_data[0][3]
        text_area.delete('1.0', END)
        text_area.insert(INSERT, result)
        messagebox.showinfo("System", "The Information is Sent to main Page")
    else:
        messagebox.showerror("System", "There is no Student with that Roll Number")


def create_find_students_via_name():
    global enter_name_entry
    main_page.destroy()
    name_find_frame = Frame(root, width=1100, height=500, bg='pink')
    name_find_frame.place(x=0, y=0)

    # animate
    name_find_frame.place(x=1100, y=0)
    time.sleep(0.011)
    root.update()
    name_find_frame.place(x=1000, y=0)
    time.sleep(0.011)
    root.update()
    name_find_frame.place(x=900, y=0)
    time.sleep(0.011)
    root.update()
    name_find_frame.place(x=800, y=0)
    time.sleep(0.011)
    root.update()
    name_find_frame.place(x=700, y=0)
    time.sleep(0.011)
    root.update()
    name_find_frame.place(x=600, y=0)
    time.sleep(0.011)
    root.update()
    name_find_frame.place(x=500, y=0)
    time.sleep(0.011)
    root.update()
    name_find_frame.place(x=400, y=0)
    time.sleep(0.011)
    root.update()
    name_find_frame.place(x=300, y=0)
    time.sleep(0.011)
    root.update()
    name_find_frame.place(x=200, y=0)
    time.sleep(0.011)
    root.update()
    name_find_frame.place(x=100, y=0)
    time.sleep(0.011)
    root.update()
    name_find_frame.place(x=0, y=0)
    root.update()

    # enter name label
    Label(name_find_frame, text="Enter Student Name", background="pink",
          font=("Microsoft YaHei UI Dark", 15, 'underline')).place(x=330, y=105)

    # enter name entry
    enter_name_entry = Entry(name_find_frame, background="#fff", font=("Microsoft YaHei UI Dark", 10), width=30)
    enter_name_entry.place(x=520, y=111)

    # enter name button
    Button(name_find_frame, text="Find", background="purple", fg='#fff', font=("Microsoft YaHei UI Dark", 15),
           width=10, borderwidth=1, command=find_students_name).place(x=480, y=150)

    back_button = Button(name_find_frame, text='←', bg='purple', fg='#fff', font=('Ariel', 12, 'bold'), width=10,
                         command=recreate_main_page)
    back_button.place(x=5, y=5)


def find_students_name():
    recreate_main_page()
    fetch_data = str(enter_name_entry.get())
    fetch_data = fetch_data.upper()
    fetch_data = db.show_by_Stud_name(fetch_data)
    if fetch_data:
        result = "Student Name: " + fetch_data[0][1] + "\n\nFather Name: " + fetch_data[0][2] + "\n\nRoll Number: " + str(fetch_data[0][0]) + "\n\nPhone Number: " + fetch_data[0][3]
        text_area.delete('1.0', END)
        text_area.insert(INSERT, result)
        messagebox.showinfo("System", "The Information is Sent to main Page")
    else:
        messagebox.showerror("System", "There is no Student with that Name")


def list_of_all_students(direction):
    recreate_main_page()
    result = db.show_all(direction)
    results = ""
    for i in result:
        results += "\n• "+i[0]
    text_area.delete('1.0', END)
    text_area.insert(INSERT, results)


def recreate_main_page():
    global main_page, new_student_name_entry, new_student_F_name_entry, new_student_phone_entry
    global text_area

    main_page = Frame(root, width=1100, height=500, bg='Pink')
    main_page.place(x=0, y=0)
    Label(main_page, text="Add new student", background="pink", foreground="Red",
          font=("Microsoft YaHei UI Dark", 20, 'underline')).place(x=5, y=0)

    Label(main_page, text="Student Name:", background="pink",
          font=("Microsoft YaHei UI Dark", 10)).place(x=5, y=40)

    Label(main_page, text="Father Name:", background="pink",
          font=("Microsoft YaHei UI Dark", 10)).place(x=5, y=65)

    Label(main_page, text="Phone Number:", background="pink",
          font=("Microsoft YaHei UI Dark", 10)).place(x=5, y=90)

    Label(main_page, text="Find Student", background="pink", foreground="Red",
          font=("Microsoft YaHei UI Dark", 20, 'underline')).place(x=5, y=250)

    Label(main_page, text="To See the list of all\nregistered Students\nClick on the Button\nbelow",
          background="pink", foreground="Red", font=("Microsoft YaHei UI Dark", 18, 'underline')).place(x=870, y=100)

    new_student_name_entry = Entry(main_page, font=("Microsoft YaHei UI Light", 10))
    new_student_name_entry.place(x=100, y=40)
    new_student_name_entry.place(x=100, y=40)
    new_student_F_name_entry = Entry(main_page, font=("Microsoft YaHei UI Light", 10))
    new_student_F_name_entry.place(x=100, y=65)
    new_student_phone_entry = Entry(main_page, font=("Microsoft YaHei UI Light", 10))
    new_student_phone_entry.place(x=100, y=90)
    Button(main_page, text="Add Student", font=("Microsoft YaHei UI Light", 10, 'bold'), borderwidth=1,
           background="Light Green", command=create_new_student).place(x=80, y=150)
    text_area = Text(main_page, background="#fff", font=("Ariel", 10))
    text_area.place(x=300, y=5)
    find_student_via_roll_button = Button(main_page, text="Find With Roll Number",
                                          font=("Microsoft YaHei UI Dark", 13, 'bold'),
                                          borderwidth=1, background="light green",
                                          command=create_find_students_via_roll_n)
    find_student_via_roll_button.place(x=5, y=300)
    find_student_via_name_button = Button(main_page, text="Find With Student Name",
                                          font=("Microsoft YaHei UI Dark", 13, 'bold'), borderwidth=1,
                                          background="light green", command=create_find_students_via_name)
    find_student_via_name_button.place(x=5, y=350)
    list_of_all_students_button = Button(main_page, text="Get Lists", font=("Microsoft YaHei UI Dark", 13, 'bold'),
                                         borderwidth=1, background="light green", width=20, command=create_sort)
    list_of_all_students_button.place(x=880, y=250)


def create_sort():
    sorting_root = Frame(root, width=1100, height=500, bg='Light Green')
    main_page.destroy()
    sorting_root.place(x=1100, y=0)
    time.sleep(0.011)
    root.update()
    sorting_root.place(x=1000, y=0)
    time.sleep(0.011)
    root.update()
    sorting_root.place(x=900, y=0)
    time.sleep(0.011)
    root.update()
    sorting_root.place(x=800, y=0)
    time.sleep(0.011)
    root.update()
    sorting_root.place(x=700, y=0)
    time.sleep(0.011)
    root.update()
    sorting_root.place(x=600, y=0)
    time.sleep(0.011)
    root.update()
    sorting_root.place(x=500, y=0)
    time.sleep(0.011)
    root.update()
    sorting_root.place(x=400, y=0)
    time.sleep(0.011)
    root.update()
    sorting_root.place(x=300, y=0)
    time.sleep(0.011)
    root.update()
    sorting_root.place(x=200, y=0)
    time.sleep(0.011)
    root.update()
    sorting_root.place(x=100, y=0)
    time.sleep(0.011)
    root.update()
    sorting_root.place(x=0, y=0)
    root.update()

    back_button = Button(sorting_root, text='←', bg='pink', fg='black', font=('Ariel', 12, 'bold'), width=10,
                         command=recreate_main_page)
    back_button.place(x=5, y=5)

    sort_via_names_a_z_button = Button(sorting_root, text="Sort a to z", font=("Microsoft YaHei UI Dark", 13, 'bold'),
                                       borderwidth=1, background="pink", command=partial(list_of_all_students, "ASC"), width=20)
    sort_via_names_a_z_button.place(x=450, y=200)

    sort_via_names_z_a_button = Button(sorting_root, text="Sort z to a", font=("Microsoft YaHei UI Dark", 13, 'bold'),
                                       borderwidth=1, background="pink", command=partial(list_of_all_students, "DESC"), width=20)
    sort_via_names_z_a_button.place(x=450, y=250)


root = Tk()
root.title("Student record System | by Maaz")
root.geometry("1100x500")
root.resizable(False, False)
main_page = Frame(root, width=1100, height=500, bg='Pink')
main_page.place(x=0, y=0)
sorting_root = Frame(root, width=1100, height=500, bg='#fff')

# New Student Name
Label(main_page, text="Add new student", background="pink", foreground="Red",
      font=("Microsoft YaHei UI Dark", 20, 'underline')).place(x=5, y=0)

Label(main_page, text="Student Name:", background="pink",
      font=("Microsoft YaHei UI Dark", 10)).place(x=5, y=40)

new_student_name_entry = Entry(main_page, font=("Microsoft YaHei UI Light", 10))
new_student_name_entry.place(x=100, y=40)

# New Student F.Name
Label(main_page, text="Father Name:", background="pink",
      font=("Microsoft YaHei UI Dark", 10)).place(x=5, y=65)

new_student_F_name_entry = Entry(main_page, font=("Microsoft YaHei UI Light", 10))
new_student_F_name_entry.place(x=100, y=65)

# New Phone No
Label(main_page, text="Phone Number:", background="pink",
      font=("Microsoft YaHei UI Dark", 10)).place(x=5, y=90)

new_student_phone_entry = Entry(main_page, font=("Microsoft YaHei UI Light", 10))
new_student_phone_entry.place(x=100, y=90)

# New data Button
Button(main_page, text="Add Student", font=("Microsoft YaHei UI Light", 10, 'bold'), borderwidth=1,
       background="Light Green", command=create_new_student).place(x=80, y=150)

# text area
text_area = Text(main_page, background="#fff", font=("Ariel", 10))
text_area.place(x=300, y=5)

# Find Student Label
Label(main_page, text="Find Student", background="pink", foreground="Red",
      font=("Microsoft YaHei UI Dark", 20, 'underline')).place(x=5, y=250)

# Find Student with Roll Number Button
find_student_via_roll_button = Button(main_page, text="Find With Roll Number",
                                      font=("Microsoft YaHei UI Dark", 13, 'bold'),
                                      borderwidth=1, background="light green", command=create_find_students_via_roll_n)
find_student_via_roll_button.place(x=5, y=300)

# Find Student with Name Button
find_student_via_name_button = Button(main_page, text="Find With Student Name",
                                      font=("Microsoft YaHei UI Dark", 13, 'bold'), borderwidth=1,
                                      background="light green", command=create_find_students_via_name)
find_student_via_name_button.place(x=5, y=350)

# All Student Lists Label
Label(main_page, text="To See the list of all\nregistered Students\nClick on the Button\nbelow",
      background="pink", foreground="Red", font=("Microsoft YaHei UI Dark", 18, 'underline')).place(x=870, y=100)

# All Student Lists Button
list_of_all_students_button = Button(main_page, text="Get Lists", font=("Microsoft YaHei UI Dark", 13, 'bold'),
                                     borderwidth=1, background="light green", width=20, command=create_sort)
list_of_all_students_button.place(x=880, y=250)

root.mainloop()
