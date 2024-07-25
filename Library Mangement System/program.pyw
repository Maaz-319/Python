import os
import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from class_book import Book
from class_user import User
from class_issued_book import IssuedBook
import database_handler_book as db_books
import database_handler_user as db_users
import database_handler_issued_book as db_issued_books
import database_handler_librarian as db_librarian
import webbrowser
from settings import current_librarian, theme
import settings_editor as se
from random import randint


class LibraryManagementSystem(tk.Tk):
    def __init__(self):
        super().__init__()

        self.cursors = "hand2"
        tb.Style().theme_use(theme)
        self.label_font = ('calibri', 12)
        self.styish_font = ('calibri', 11, 'bold')
        self.bootstrap_style = ("success", "outline")

        self.options = ["Student", "General", "Premium"]

        self.title("Library Management System | By Maaz")
        self.state('zoomed')

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Styling
        self.style = ttk.Style(self)
        self.style.configure('TLabel', font=self.label_font, background="white", foreground="Black")
        self.style.configure('TButton', font=self.label_font, background="#007BFF", foreground="black")
        self.style.map('TButton', background=[('active', '#0056b3')])
        self.style.configure('Treeview', font=self.label_font)
        self.style.configure('Treeview.Heading', font=self.label_font, background="#f0f0f0", foreground="#333")

        # Create frames
        self.create_frames()

        # Initialize the UI
        self.create_widgets()

    def create_frames(self):
        # self.menu_frame = ttk.Frame(self, padding="10")
        # self.menu_frame.pack(side=tk.TOP, fill=tk.X)

        self.content_frame = ttk.Frame(self, padding="10")
        self.content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.book_list_frame = ttk.LabelFrame(self.content_frame, text="Book List", padding="10")
        self.book_list_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.form_frame = ttk.LabelFrame(self.content_frame, text="Book Form", padding="10")
        self.form_frame.pack(side=tk.BOTTOM, fill=tk.X)

    def create_widgets(self):
        # Book list
        self.book_tree = ttk.Treeview(self.book_list_frame, columns=("Title", "Author", "Genre"), show='headings',
                                      cursor=self.cursors, style='success.Treeview')
        self.book_tree.heading("Title", text="Title")
        self.book_tree.heading("Author", text="Author")
        self.book_tree.heading("Genre", text="Genre")
        self.book_tree.pack(fill=tk.BOTH, expand=True)
        self.book_tree.bind("<<TreeviewSelect>>", self.on_book_select)

        # Form fields
        ttk.Label(self.form_frame, text="Title:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.title_entry = ttk.Entry(self.form_frame, bootstyle="success")
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.form_frame, text="Author:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.author_entry = ttk.Entry(self.form_frame, bootstyle="success")
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.form_frame, text="Genre:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.genre_entry = ttk.Entry(self.form_frame, bootstyle="success")
        self.genre_entry.grid(row=2, column=1, padx=5, pady=5)

        # Menu buttons
        ttk.Button(self.form_frame, text="Add Book", command=self.add_book, cursor=self.cursors,
                   bootstyle=self.bootstrap_style).grid(row=0, column=2, padx=5)
        ttk.Button(self.form_frame, text="Search Book", command=self.search_book, cursor=self.cursors,
                   bootstyle=self.bootstrap_style).grid(row=1, column=2, padx=5)
        ttk.Button(self.form_frame, text="Show All Books", command=self.show_all_books, cursor=self.cursors,
                   bootstyle=self.bootstrap_style).grid(row=2, column=2, padx=5)
        ttk.Button(self.form_frame, text="Check Books Issued", command=lambda: os.system("report_generator.pyw"),
                   cursor=self.cursors, bootstyle=self.bootstrap_style).grid(row=1, column=5, padx=50)
        ttk.Button(self.form_frame, text="Create New User", command=self.show_create_new_user,
                   cursor=self.cursors, bootstyle=self.bootstrap_style).grid(row=0, column=5, padx=50)

        # ttk.Button(self.form_frame, text="Add Book", command=self.add_book).grid(row=3, column=0, columnspan=2, pady=10)

        # Menu bar
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        self.theme_value = tk.IntVar()
        file_menu.add_command(label="Themes", command=self.show_change_theme)
        file_menu.add_command(label="Feedback",
                              command=lambda: webbrowser.open_new_tab("https://forms.gle/PPwtdPAD4t975ZLD8"))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_closing)

        self.show_all_books()

    # ======================================================================================================================================
    def show_change_theme(self):
        theme_window = tk.Toplevel(self)
        theme_window.title("Themes")
        theme_window.geometry("250x300")

        ttk.Button(theme_window, text="Default", command=lambda: self.change_theme("united")).pack(pady=5, padx=5,
                                                                                                   fill=tk.X)
        ttk.Button(theme_window, text="Dark", command=lambda: self.change_theme("darkly")).pack(pady=5, padx=5,
                                                                                                fill=tk.X)
        ttk.Button(theme_window, text="Solar", command=lambda: self.change_theme("solar")).pack(pady=5, padx=5,
                                                                                                fill=tk.X)
        ttk.Button(theme_window, text="Cyborg", command=lambda: self.change_theme("cyborg")).pack(pady=5, padx=5,
                                                                                                  fill=tk.X)
        ttk.Button(theme_window, text="Yeti", command=lambda: self.change_theme("yeti")).pack(pady=5, padx=5,
                                                                                              fill=tk.X)
        ttk.Button(theme_window, text="vapor", command=lambda: self.change_theme("vapor")).pack(pady=5, padx=5,
                                                                                                fill=tk.X)
        ttk.Button(theme_window, text="superhero", command=lambda: self.change_theme("superhero")).pack(pady=5,
                                                                                                        padx=5,
                                                                                                        fill=tk.X)

    @staticmethod
    def change_theme(name):
        tb.Style().theme_use(name)
        se.update_settings(current_librarian, name)

    def show_all_books(self):
        self.clear_tree()
        all_books = Book.show_all_books()
        for book in all_books:
            self.book_tree.insert("", "end", values=(book[0].capitalize(), book[1].capitalize(), book[2].capitalize()))

    def add_book(self):
        title = self.title_entry.get().lower()
        author = self.author_entry.get().lower()
        genre = self.genre_entry.get().lower()

        if title == "" or author == "" or genre == "":
            messagebox.showerror("Error", "Fill All Fields")
        elif db_books.search_book_by_mode(title, 0):
            messagebox.showerror("Error", "Book Already Exists")
        else:
            new_book = Book(title, author, genre)
            if not new_book.save_new_book():
                messagebox.showerror("Error", "Failed to Add Book: Internal Error")
            else:
                messagebox.showinfo("Book Added Successfully",
                                    f"'{new_book.name.capitalize()}' \n '{new_book.author.capitalize()}' \n '{new_book.genre.capitalize()}'")
                self.book_tree.insert("", "end", values=(title, author, genre))

    def search_book(self):
        title = self.title_entry.get().lower()
        author = self.author_entry.get().lower()
        genre = self.genre_entry.get().lower()

        titles = db_books.get_all_book_names()
        authors = db_books.get_all_book_authors()
        genres = db_books.get_all_book_genres()

        self.clear_tree()

        if title:
            for name in titles:
                if title in name:
                    results = db_books.search_book_by_mode(name, 0)
                    for book in results:
                        self.book_tree.insert("", "end",
                                              values=(book[0].capitalize(), book[1].capitalize(), book[2].capitalize()))
        elif author:
            for name in authors:
                if author in name:
                    results = db_books.search_book_by_mode(name, 1)
                    for book in results:
                        self.book_tree.insert("", "end",
                                              values=(book[0].capitalize(), book[1].capitalize(), book[2].capitalize()))
        else:
            for name in genres:
                if genre in name:
                    results = db_books.search_book_by_mode(name, 2)
                    for book in results:
                        self.book_tree.insert("", "end",
                                              values=(book[0].capitalize(), book[1].capitalize(), book[2].capitalize()))

    def clear_tree(self):
        for item in self.book_tree.get_children():
            self.book_tree.delete(item)

        ttk.Label(self.form_frame, text="Title:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(self.form_frame, text="Author:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(self.form_frame, text="Genre:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.genre_entry.grid(row=2, column=1, padx=5, pady=5)

    def on_book_select(self, event):
        selected_item = self.book_tree.selection()
        if selected_item:
            item = self.book_tree.item(selected_item)
            book_selected = item['values']
            self.show_book_options(book_selected)

    def show_book_options(self, book_selected):
        options_window = tk.Toplevel(self)
        options_window.title("Book Options")
        options_window.geometry("400x150")

        ttk.Label(options_window, text=f"{book_selected[0]}").pack(pady=10)
        ttk.Button(options_window, text="Issue Book", command=lambda: self.issue_book(book_selected),
                   bootstyle=self.bootstrap_style, cursor=self.cursors).pack(pady=5)
        ttk.Button(options_window, text="Delete Book", command=lambda: self.delete_book(book_selected, options_window),
                   bootstyle=self.bootstrap_style, cursor=self.cursors).pack(pady=5)

    def issue_book(self, book_selected):
        issue_window = tk.Toplevel(self)
        issue_window.title("Issue Book")

        ttk.Label(issue_window, text="User ID:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        user_id_entry = ttk.Entry(issue_window, bootstyle="success")
        user_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(issue_window, text="Issue",
                   command=lambda: self.issue_book_to_user(book_selected, user_id_entry.get(), issue_window),
                   cursor=self.cursors, bootstyle=self.bootstrap_style).grid(row=1, column=0, columnspan=2, pady=10)

    def issue_book_to_user(self, book_selected, user_id, issue_window):
        global new_book, new_user, new_issued_book

        results = db_users.search(user_id, 1)
        if not results:
            messagebox.showerror("Error", "User ID not found.")
            return

        issue_date = datetime.now()

        new_user = User(results[0][0], results[0][1], results[0][2], results[0][3], results[0][4])
        new_book = Book(book_selected[0].strip().lower(), book_selected[1].strip().lower(),
                        book_selected[2].strip().lower())

        if new_user.membership == "General":
            days_to_return = 7
        elif new_user.membership == "Student":
            days_to_return = 14
        else:
            days_to_return = 30

        return_date = (issue_date + timedelta(days=days_to_return)).strftime("%Y-%m-%d")
        issue_date = issue_date.strftime("%Y-%m-%d")

        new_issued_book = IssuedBook(new_book.name, new_user.i_d, issue_date, new_user.membership, return_date)
        new_issued_book.save_new_issued_book()

        messagebox.showinfo("Success",
                            f"Book '{new_issued_book.book_name}' issued to User ID: {new_issued_book.user_id}")

        issue_window.destroy()

    def delete_book(self, book_selected, options_window):
        global new_book
        results = db_books.search_book_by_mode(book_selected[0].lower(), 0)
        if results:
            new_book = Book(book_selected[0].lower(), book_selected[1].lower(), book_selected[2].lower())
            new_book.delete_book()
            print(new_book)
            self.clear_tree()
            self.show_all_books()
            messagebox.showinfo("Success", f"Book '{new_book.name}' deleted.")
            options_window.destroy()
        return

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            current_librarian = None

            se.update_settings(current_librarian, tb.Style().theme.name)

            db_books.end_connection()  # close database connection from books database
            db_issued_books.end_connection()  # close database connection from issuedbooks database
            db_users.end_connection()  # close database connection from user database
            db_librarian.end_connection()  # close database connection from librarian database

            self.destroy()  # destroy the root window

    def show_create_new_user(self):
        options_window = tk.Toplevel(self)
        options_window.title("Create User")
        options_window.geometry("300x300")

        ttk.Label(options_window, text="Name").grid(pady=10, padx=20, row=0, column=0)
        username_entry = tb.Entry(options_window, bootstyle='success')
        username_entry.grid(row=0, column=1)

        ttk.Label(options_window, text="Phone").grid(pady=10, padx=20, row=1, column=0)
        userph_entry = tb.Entry(options_window, bootstyle='success')
        userph_entry.grid(row=1, column=1)

        ttk.Label(options_window, text="Email").grid(pady=10, padx=20, row=2, column=0)
        userem_entry = tb.Entry(options_window, bootstyle='success')
        userem_entry.grid(row=2, column=1)

        selected_membership = tk.StringVar()
        selected_membership.set(self.options[0])
        ttk.Label(options_window, text="Membership").grid(pady=10, padx=5, row=3, column=0)
        membership_menu = tb.OptionMenu(options_window, selected_membership, *self.options, bootstyle='success').grid(row=3, column=1, pady=5)

        ttk.Button(options_window, text="Create User", bootstyle=self.bootstrap_style, cursor=self.cursors, command=lambda: self.create_user(username_entry.get(), userph_entry.get(), userem_entry.get(), selected_membership.get(), options_window)).grid(row=5, column=0, pady=10, padx=30)

    def create_user(self, name, phone, email, membership, options_window):
        if name == "" or phone == "" or email == "" or membership not in self.options:
            messagebox.showerror("Error", "Fill All Fields")
        elif len(phone) != 11 or "03" not in phone:
            messagebox.showerror("Error", "Invalid Phone Number")
        elif "@" not in email or "." not in email:
            messagebox.showerror("Error", "Invalid Email")
        elif db_users.search(name, 0):
            messagebox.showerror("Error", "User Already Exists")
        elif db_users.search(phone, 2):
            messagebox.showerror("Error", "Phone Number Already In Use")
        elif db_users.search(email, 3):
            messagebox.showerror("Error", "Email Already In Use")
        else:
            random_user_id = randint(1000, 9999)
            while db_users.search(random_user_id, 1):
                random_user_id = randint(1000, 9999)
            new_user = User(random_user_id, name.lower(), phone, email, membership.lower())
            new_user.save_new_user()
            options_window.destroy()
            messagebox.showinfo("New User Saved", f"User Added Successfully\n\nID: {new_user.i_d}\nName: '{new_user.name}'\nPhone: '{new_user.phone}'\nEmail: '{new_user.email}'\nMembership: '{new_user.membership}'\n\nPlease Remember your User_ID")
        return


def authorize():
    if not current_librarian:
        messagebox.showerror("Error", "Please   login to continue")
    else:
        app = LibraryManagementSystem()
        new_book = None
        new_user = None
        new_issued_book = None
        app.mainloop()


if __name__ == "__main__":
    authorize()
