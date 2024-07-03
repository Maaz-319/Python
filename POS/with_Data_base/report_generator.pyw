import tkinter as tk
import database_handler_order as db_order
import database_handler_item as db_item
from data import total_sales, current_cashier
from datetime import datetime
from tkinter import messagebox


class SalesReportApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sales Report Generator")
        # self.root.geometry("800x600")
        self.root.state("zoomed")
        self.root.resizable(False, False)
        self.root.configure(bg=bg_color)

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Sales Report Generator",
                                    font=("Arial", 24), bg=bg_color, fg=primary_color)
        self.title_label.pack(pady=20)

        # Date Range Frame
        self.date_frame = tk.Frame(self.root, bg=bg_color)
        self.date_frame.pack(pady=10)

        tk.Label(self.date_frame, text="Date Format (YYYY-MM-DD)",
                 font=("Arial", 14), bg=bg_color, fg=text_color).grid(row=0, column=0, columnspan=4, pady=10)

        self.start_date_label = tk.Label(self.date_frame, text="Start Date:",
                                         font=("Arial", 14), bg=bg_color, fg=text_color)
        self.start_date_label.grid(row=1, column=0, padx=10)
        self.start_date_entry = tk.Entry(self.date_frame, font=("Arial", 14))
        self.start_date_entry.grid(row=1, column=1, padx=10)

        self.end_date_label = tk.Label(self.date_frame, text="End Date:",
                                       font=("Arial", 14), bg=bg_color, fg=text_color)
        self.end_date_label.grid(row=1, column=2, padx=10)
        self.end_date_entry = tk.Entry(self.date_frame, font=("Arial", 14))
        self.end_date_entry.grid(row=1, column=3, padx=10)

        # Generate Report Button
        self.generate_button = tk.Button(self.root, text="Generate Report",
                                         font=("Arial", 16), bg=primary_color, fg=bg_color,
                                         command=self.generate_report)
        self.generate_button.pack(pady=20)

        # Report Display Frame
        self.report_frame = tk.Frame(self.root, bg=bg_color)
        self.report_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.report_text = tk.Text(self.report_frame, wrap=tk.WORD, font=("Arial", 12),
                                   bg=bg_color, fg=text_color)
        self.report_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def generate_report(self):
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            self.report_text.delete(1.0, tk.END)
            self.report_text.configure(bg=primary_color, fg=error_color, font=("Comic Sans Ms", 20, "bold"))
            self.report_text.insert(tk.END, "Invalid date format. Please use YYYY-MM-DD.\n")
            return

        records = db_order.fetch_data_by_date(start_date, end_date)
        if records == []:
            report = "\t\t\t\tNo Sale In Selected Range"
            self.report_text.configure(bg=primary_color, fg=error_color, font=("Comic Sans Ms", 20, "bold"))
        else:
            self.report_text.configure(bg="white", fg=text_color, font=("Ariel", 12, "bold"))
            
            report = f"\t\t\t\t\t\t\tDate Range: {start_date} -\t {end_date}\n"


            report += "\nNo.\tItem Name\t\t\t|\t Price\t\t\t|\t Quantity\t\t\t|\tSales\t\t\t|\tDate\n"
            report += "-" * 250
            report += f"\n   \t         \t\t\t|\t      \t\t\t|\t         \t\t\t|\tTotal Sales: Rs. Error\n|"
            report += "   \t         \t\t\t|\t      \t\t\t|\t         \t\t\t|\t     \t\t\t|\t\n"
            report += "   \t         \t\t\t|\t      \t\t\t|\t         \t\t\t|\t     \t\t\t|\t\n"
            
            for record, counter in zip(records, range(1, len(records) + 1)):
                report += f"{counter}\t{record[0]}\t\t\t|\t{db_item.get_item_by_name(record[0])[1]}\t\t\t|\t{record[2]}\t\t\t|\t{db_item.get_item_by_name(record[0])[1] * record[2]}\t\t\t|\t{record[1]}\n"


        self.report_text.delete(1.0, tk.END)
        self.report_text.insert(tk.END, report)


# function to authorize the user
def authorize():
    if not current_cashier:
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