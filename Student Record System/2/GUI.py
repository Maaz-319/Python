import tkinter as tk
import ttkbootstrap as tb
from tkinter import ttk, messagebox


class Student:
    def __init__(self, stud_name, fath_name, roll_no, class_, section, age, phone, address):
        self.stud_name = stud_name
        self.fath_name = fath_name
        self.roll_no = roll_no
        self.class_ = class_
        self.section = section
        self.age = age
        self.phone = phone
        self.address = address


class StudentManagementSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Management System")
        tb.Style().theme_use('united')
        self.geometry("800x600")
        self.state('zoomed')

        self.students = []

        self.create_frames()
        self.create_widgets()

    def create_frames(self):
        self.tree_frame = ttk.Frame(self)
        self.tree_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.form_frame = ttk.LabelFrame(self, text="Student Form")
        self.form_frame.pack(side=tk.BOTTOM, padx=5, pady=5, fill=tk.X, expand=False)

    def create_widgets(self):
        ttk.Label(self.form_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.name_entry = ttk.Entry(self.form_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.form_frame, text="Father's Name:").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        self.fath_name_entry = ttk.Entry(self.form_frame)
        self.fath_name_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(self.form_frame, text="Roll No:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.roll_no_entry = ttk.Entry(self.form_frame)
        self.roll_no_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.form_frame, text="Class:").grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
        self.class_entry = ttk.Entry(self.form_frame)
        self.class_entry.grid(row=1, column=3, padx=5, pady=5)

        ttk.Label(self.form_frame, text="Section:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.section_entry = ttk.Entry(self.form_frame)
        self.section_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.form_frame, text="Age:").grid(row=2, column=2, padx=5, pady=5, sticky=tk.W)
        self.age_entry = ttk.Entry(self.form_frame)
        self.age_entry.grid(row=2, column=3, padx=5, pady=5)

        ttk.Label(self.form_frame, text="Phone:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.phone_entry = ttk.Entry(self.form_frame)
        self.phone_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(self.form_frame, text="Address:").grid(row=3, column=2, padx=5, pady=5, sticky=tk.W)
        self.address_entry = ttk.Entry(self.form_frame)
        self.address_entry.grid(row=3, column=3, padx=5, pady=5)

        ttk.Button(self.form_frame, text="Add Student", command=self.add_student).grid(row=4, column=0, columnspan=2,
                                                                                       pady=5)
        ttk.Button(self.form_frame, text="Search Student", command=self.search_student).grid(row=4, column=2,
                                                                                             columnspan=2, pady=5)

        self.student_tree = ttk.Treeview(self.tree_frame, columns=(
            "Name", "Father's Name", "Roll No", "Class", "Section", "Age", "Phone", "Address"), show='headings')

        # Set the width of the columns
        self.student_tree.column("Name", width=1, anchor='w')
        self.student_tree.column("Father's Name", width=1, anchor='w')
        self.student_tree.column("Roll No", width=1, anchor='w')
        self.student_tree.column("Class", width=1, anchor='w')
        self.student_tree.column("Section", width=1, anchor='w')
        self.student_tree.column("Age", width=1, anchor='w')
        self.student_tree.column("Phone", width=1, anchor='w')
        self.student_tree.column("Address", width=1, anchor='w')

        self.student_tree.heading("Name", text="Name")
        self.student_tree.heading("Father's Name", text="Father's Name")
        self.student_tree.heading("Roll No", text="Roll No")
        self.student_tree.heading("Class", text="Class")
        self.student_tree.heading("Section", text="Section")
        self.student_tree.heading("Age", text="Age")
        self.student_tree.heading("Phone", text="Phone")
        self.student_tree.heading("Address", text="Address")

        self.student_tree.pack(fill=tk.BOTH, expand=True)
        self.student_tree.bind("<<TreeviewSelect>>", self.on_student_select)
        self.student_tree.insert("", "end", values=("John Doe", "John Doe", "1", "fifth", "A", "15", "1234567890",
                                                    "123, Main Street, City"))

    def add_student(self):
        stud_name = self.name_entry.get()
        fath_name = self.fath_name_entry.get()
        roll_no = self.roll_no_entry.get()
        class_ = self.class_entry.get()
        section = self.section_entry.get()
        age = self.age_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()

        if stud_name and fath_name and roll_no and class_ and section and age and phone and address:
            student = Student(stud_name, fath_name, roll_no, class_, section, age, phone, address)
            self.students.append(student)
            self.student_tree.insert("", "end",
                                     values=(stud_name, fath_name, roll_no, class_, section, age, phone, address))
            self.clear_form()
        else:
            messagebox.showwarning("Warning", "Please fill out all fields")

    def search_student(self):
        search_name = self.name_entry.get()
        search_roll_no = self.roll_no_entry.get()
        search_class = self.class_entry.get()
        search_section = self.section_entry.get()
        search_age = self.age_entry.get()
        search_phone = self.phone_entry.get()
        search_address = self.address_entry.get()

        for item in self.student_tree.get_children():
            self.student_tree.delete(item)

        for student in self.students:
            if (not search_name or search_name == student.stud_name) and \
                    (not search_roll_no or search_roll_no == student.roll_no) and \
                    (not search_class or search_class == student.class_) and \
                    (not search_section or search_section == student.section) and \
                    (not search_age or search_age == student.age) and \
                    (not search_phone or search_phone == student.phone) and \
                    (not search_address or search_address == student.address):
                self.student_tree.insert("", "end", values=(
                    student.stud_name, student.fath_name, student.roll_no, student.class_, student.section, student.age,
                    student.phone, student.address))

    def on_student_select(self, event):
        selected_item = self.student_tree.selection()
        if selected_item:
            item = self.student_tree.item(selected_item)
            stud_name = item['values'][0]
            response = messagebox.askyesnocancel("Edit or Delete", f"Do you want to edit or delete {stud_name}?",
                                                 icon='question')
            if response == True:
                self.edit_student(selected_item)
            elif response == False:
                self.delete_student(selected_item)

    def edit_student(self, item):
        student = self.student_tree.item(item, "values")
        self.name_entry.insert(0, student[0])
        self.fath_name_entry.insert(0, student[1])
        self.roll_no_entry.insert(0, student[2])
        self.class_entry.insert(0, student[3])
        self.section_entry.insert(0, student[4])
        self.age_entry.insert(0, student[5])
        self.phone_entry.insert(0, student[6])
        self.address_entry.insert(0, student[7])

        self.student_tree.delete(item)
        self.students = [s for s in self.students if s.roll_no != student[2]]

    def delete_student(self, item):
        student = self.student_tree.item(item, "values")
        self.student_tree.delete(item)
        self.students = [s for s in self.students if s.roll_no != student[2]]

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.fath_name_entry.delete(0, tk.END)
        self.roll_no_entry.delete(0, tk.END)
        self.class_entry.delete(0, tk.END)
        self.section_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


if __name__ == "__main__":
    app = StudentManagementSystem()
    app.mainloop()
