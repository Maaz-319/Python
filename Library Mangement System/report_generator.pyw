import tkinter as tk
import ttkbootstrap as tb
import database_handler_user as db_user
import database_handler_issued_book as db_issue
from settings import current_librarian, theme
from tkinter import messagebox


class SalesReportApp:
    def __init__(self, root):
        self.root = root
        tb.Style().theme_use(theme)
        self.root.title("Issued Books")
        # self.root.geometry("800x600")
        self.root.state("zoomed")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Issued Books",
                                    font=("Arial", 24))
        self.title_label.pack(pady=20)

        # Generate Report Button

        self.mode = tk.IntVar()
        self.mode.set(0)
        tb.Radiobutton(self.root, text="User ID", value=0, variable=self.mode, bootstyle="success").pack(pady=5)
        tb.Radiobutton(self.root, text="User Name", value=1, variable=self.mode, bootstyle="success").pack()

        self.words = tb.Entry(self.root)
        self.words.pack(padx=10, pady=10)

        self.find_by_user_button = tk.Button(self.root, text="Find By User", font=("Arial", 16), bg=primary_color,
                                             fg=bg_color, command=self.generate_report)
        self.find_by_user_button.pack(pady=20)

        self.all_button = tk.Button(self.root, text="Complete Report", font=("Arial", 16), bg=primary_color,
                                    fg=bg_color, command=self.show_complete_report)
        self.all_button.pack(pady=20)

        # Report Display Frame
        self.report_frame = tk.Frame(self.root, bg=bg_color)
        self.report_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.report_text = tk.Text(self.report_frame, wrap=tk.WORD, font=("Arial", 12),
                                   bg=bg_color, fg=text_color)
        self.report_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def generate_report(self):
        report = ""
        try:
            if self.mode.get() == 0:
                results = db_issue.search(self.words.get(), 3)
                if not results:
                    raise ValueError
                else:
                    self.report_text.configure(fg=text_color, font=("Ariel", 12, "bold"))

                    report = "No.\tUser\t\t\t|\t Book\t\t\t|\t Issued Date\t\t\t|\tReturn Date\t\t\t|\tMembership\n"
                    report += "-" * 250
                    report += f"\n\t         \t\t\t|\t      \t\t\t|\t         \t\t\t|\t     \t\t\t|\t\n"
                    report += "   \t         \t\t\t|\t      \t\t\t|\t         \t\t\t|\t     \t\t\t|\t\n"
                    report += "   \t         \t\t\t|\t      \t\t\t|\t         \t\t\t|\t     \t\t\t|\t\n"

                    for record, counter in zip(results, range(1, len(results) + 1)):
                        user_name = db_user.get_user_by_id(record[1]).capitalize()
                        report += f"{counter}\t{user_name}\t\t\t|\t{record[0].capitalize()}\t\t\t|\t{record[1]}\t\t\t|\t{record[3]}\t\t\t|\t{record[2]}\n"
            elif self.mode.get() == 1:
                user_id = db_user.search(self.words.get().lower(), 0)[0][0]
                results = db_issue.search(user_id, 3)
                if not results:
                    raise ValueError
                else:
                    self.report_text.configure(fg=text_color, font=("Ariel", 12, "bold"))

                    report = "No.\tUser\t\t\t|\t Book\t\t\t|\t Issued Date\t\t\t|\tReturn Date\t\t\t|\tMembership\n"
                    report += "-" * 250
                    report += f"\n\t         \t\t\t|\t      \t\t\t|\t         \t\t\t|\t     \t\t\t|\t\n"
                    report += "   \t         \t\t\t|\t      \t\t\t|\t         \t\t\t|\t     \t\t\t|\t\n"
                    report += "   \t         \t\t\t|\t      \t\t\t|\t         \t\t\t|\t     \t\t\t|\t\n"

                    for record, counter in zip(results, range(1, len(results) + 1)):
                        user_name = db_user.get_user_by_id(record[1])
                        report += f"{counter}\t{user_name}\t\t\t|\t{record[0].capitalize()}\t\t\t|\t{record[1]}\t\t\t|\t{record[3]}\t\t\t|\t{record[2]}\n"
        except:
            report = "\t\t\t\tNo Records Found"
            self.report_text.configure(fg=error_color, font=("Comic Sans Ms", 20, "bold"))

        self.report_text.delete(1.0, tk.END)
        self.report_text.insert(tk.END, report)

    def show_complete_report(self):
        records = db_issue.show_all()
        if records == []:
            report = "\t\t\t\tNo Books Issued"
            self.report_text.configure(fg=error_color, font=("Comic Sans Ms", 20, "bold"))
        else:
            self.report_text.configure(fg=text_color, font=("Ariel", 12, "bold"))

            report = "No.\tUser\t\t\t|\t Book\t\t\t|\t Issued Date\t\t\t|\tReturn Date\t\t\t|\tMembership\n"
            report += "-" * 255
            report += f"\n\t         \t\t\t|\t      \t\t\t|\t         \t\t\t|\t     \t\t\t|\t\n"
            report += "-" * 255
            report += f"\n\t         \t\t\t|\t      \t\t\t|\t         \t\t\t|\t     \t\t\t|\t\n"
            report += "   \t         \t\t\t|\t      \t\t\t|\t         \t\t\t|\t     \t\t\t|\t\n"
            report += "   \t         \t\t\t|\t      \t\t\t|\t         \t\t\t|\t     \t\t\t|\t\n"

            for record, counter in zip(records, range(1, len(records) + 1)):
                user_name = db_user.get_user_by_id(record[1]).capitalize()
                report += f"{counter}.\t{user_name}\t\t\t|\t{record[0].capitalize()}\t\t\t|\t{record[2]}\t\t\t|\t{record[4]}\t\t\t|\t{record[3]}\n"

        self.report_text.delete(1.0, tk.END)
        self.report_text.insert(tk.END, report)


# function to authorize the user
def authorize():
    if not current_librarian:
        messagebox.showerror("Error", "Please login to continue")
    else:
        root = tk.Tk()
        app = SalesReportApp(root)
        root.mainloop()


if __name__ == "__main__":
    bg_color = "#f0f0f0"
    primary_color = "#004d40"
    accent_color = "#00bfa5"
    text_color = "#333333"
    error_color = "#ff5252"

    authorize()
