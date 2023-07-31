import time
from tkinter import *
from tkinter import messagebox

# Check if data file is not absent or corrupted
try:
    from data import names
    from data import phones
    from data import f_names
    from data import roll_ns
except ImportError:
    file = open('data.py', 'w')
    file.write('names=[]')
    file.write('\nphones=[]')
    file.write('\nf_names=[]')
    file.write('\nroll_ns=[]')
    file.close()
    from data import names
    from data import phones
    from data import f_names
    from data import roll_ns


def create_new_student():
    # Check if any of entry is empty
    global student_roll
    if not new_student_name_entry.get() or not new_student_F_name_entry.get() or not new_student_phone_entry.get() or not new_student_Roll_entry.get():
        messagebox.showerror("System", "Please fill all fields")
    else:
        student_name = str(new_student_name_entry.get())
        student_f_name = str(new_student_F_name_entry.get())
        student_name = student_name.upper()
        student_f_name = student_f_name.upper()

        # Check if Roll Number is integer
        try:
            student_roll = int(new_student_Roll_entry.get())
        except ValueError:
            messagebox.showerror("System", "Your Roll Number is incorrect")
        if student_roll == 0:
            messagebox.showerror("System", "Roll Number can not be '0'")
        else:
            if student_roll in roll_ns:
                messagebox.showerror("System", "This Roll Number is already in Use")
            else:
                # Check if phone number is correct
                student_phone = str(new_student_phone_entry.get())
                if len(str(student_phone)) != 11:
                    messagebox.showerror('System', 'Please Enter Correct Phone Number')
                    messagebox.showerror("System", "Your Phone Number is incorrect")
                else:
                    data_file = open('data.py', 'w')
                    names.append(student_name)
                    f_names.append(student_f_name)
                    phones.append(student_phone)
                    roll_ns.append(student_roll)
                    data_file.write('names=' + str(names))
                    data_file.write('\nf_names=' + str(f_names))
                    data_file.write('\nphones=' + str(phones))
                    data_file.write('\nroll_ns=' + str(roll_ns))
                    data_file.close()
                    new_student_name_entry.delete(0, END)
                    new_student_F_name_entry.delete(0, END)
                    new_student_Roll_entry.delete(0, END)
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
    roll_n = int(enter_roll_number_entry.get())
    if roll_n in roll_ns:
        index = roll_ns.index(roll_n)
        result = "Student Name: " + str(names[index]) + "\n\nFather Name: " + str(
            f_names[index]) + "\n\nRoll Number: " + str(roll_n) + "\n\nPhone Number: " + str(phones[index])
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
    # Find and display student if found
    s_name = str(enter_name_entry.get())
    s_name = s_name.upper()
    if s_name in names:
        index = names.index(s_name)
        result = "Student Name: " + str(names[index]) + "\n\nFather Name: " + str(
            f_names[index]) + "\n\nRoll Number: " + str(roll_ns[index]) + "\n\nPhone Number: " + str(phones[index])
        text_area.delete('1.0', END)
        text_area.insert(INSERT, result)
        messagebox.showinfo("System", "The Information is Sent to main Page")
    else:
        messagebox.showerror("System", "There is no Student with that Name")


def list_of_all_students():
    recreate_main_page()
    result = str(names)
    result = result.replace('\'', '').replace(',', '\n•').replace('[', '• ').replace(']', '')
    text_area.delete('1.0', END)
    text_area.insert(INSERT, result)


def recreate_main_page():
    global main_page, new_student_name_entry, new_student_F_name_entry, new_student_Roll_entry, new_student_phone_entry
    global text_area

    main_page = Frame(root, width=1100, height=500, bg='Pink')
    main_page.place(x=0, y=0)
    Label(main_page, text="Add new student", background="pink", foreground="Red",
          font=("Microsoft YaHei UI Dark", 20, 'underline')).place(x=5, y=0)

    Label(main_page, text="Student Name:", background="pink",
          font=("Microsoft YaHei UI Dark", 10)).place(x=5, y=40)

    Label(main_page, text="Father Name:", background="pink",
          font=("Microsoft YaHei UI Dark", 10)).place(x=5, y=65)

    Label(main_page, text="Roll Number:", background="pink",
          font=("Microsoft YaHei UI Dark", 10)).place(x=5, y=90)

    Label(main_page, text="Phone Number:", background="pink",
          font=("Microsoft YaHei UI Dark", 10)).place(x=5, y=115)

    Label(main_page, text="Find Student", background="pink", foreground="Red",
          font=("Microsoft YaHei UI Dark", 20, 'underline')).place(x=5, y=250)

    Label(main_page, text="To See the list of all\nregistered Students\nClick on the Button\nbelow",
          background="pink", foreground="Red", font=("Microsoft YaHei UI Dark", 18, 'underline')).place(x=870, y=100)

    new_student_name_entry = Entry(main_page, font=("Microsoft YaHei UI Light", 10))
    new_student_name_entry.place(x=100, y=40)
    new_student_name_entry.place(x=100, y=40)
    new_student_F_name_entry = Entry(main_page, font=("Microsoft YaHei UI Light", 10))
    new_student_F_name_entry.place(x=100, y=65)
    new_student_Roll_entry = Entry(main_page, font=("Microsoft YaHei UI Light", 10))
    new_student_Roll_entry.place(x=100, y=90)
    new_student_phone_entry = Entry(main_page, font=("Microsoft YaHei UI Light", 10))
    new_student_phone_entry.place(x=100, y=115)
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


def sort_a_to_z():
    sorting_root.destroy()
    recreate_main_page()
    names.sort()
    list_of_all_students()


def sort_z_to_a():
    sorting_root.destroy()
    recreate_main_page()
    names.sort(reverse=True)
    list_of_all_students()


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
                                       borderwidth=1, background="pink", command=sort_a_to_z, width=20)
    sort_via_names_a_z_button.place(x=450, y=200)

    sort_via_names_z_a_button = Button(sorting_root, text="Sort z to a", font=("Microsoft YaHei UI Dark", 13, 'bold'),
                                       borderwidth=1, background="pink", command=sort_z_to_a, width=20)
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

# New Student Roll No
Label(main_page, text="Roll Number:", background="pink",
      font=("Microsoft YaHei UI Dark", 10)).place(x=5, y=90)

new_student_Roll_entry = Entry(main_page, font=("Microsoft YaHei UI Light", 10))
new_student_Roll_entry.place(x=100, y=90)

# New Phone No
Label(main_page, text="Phone Number:", background="pink",
      font=("Microsoft YaHei UI Dark", 10)).place(x=5, y=115)

new_student_phone_entry = Entry(main_page, font=("Microsoft YaHei UI Light", 10))
new_student_phone_entry.place(x=100, y=115)

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
