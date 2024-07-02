import POS.with_Data_base.database_handlers.database_handler_item as db_item
import POS.with_Data_base.database_handlers.database_handler_order as db_order
import tkinter as tk
from tkinter import messagebox


# functions
def calculate_total_sales(mode):
    messagebox.showinfo(f"{mode} Sales",
                        f"Sales: Rs {db_order.get_max_min_order_by_price(mode)[0]}\nDate: {db_order.get_max_min_order_by_price(mode)[0]}")


def total_sales_by_date(mode):
    date = date_entry.get()
    if date == "":
        messagebox.showerror("Error", "Please enter a date")
        return
    data = db_order.get_max_min_order_by_price_on_date(mode, date)[0]
    if not data:
        messagebox.showerror("Error", "No sales on this date\nPlease Enter Date in Correct Format")
        return
    messagebox.showinfo(f"{mode} Sales", f"Sales: Rs {data}")


def get_sold_item_by_number(mode):
    data = db_order.get_most_min_sold_item(mode)
    if not data:
        messagebox.showerror("Error", "No sales for\nPlease Enter Date in Correct Format")
        return
    messagebox.showinfo(f"{mode} Sales",
                        f"Item: {data[0]}\nSold: {data[1]}\nSales: Rs {db_item.get_item_by_name(data[0])[1] * data[1]}")


root = tk.Tk()
root.title("Report Generator")
root.state("zoomed")

# frame for total sales
frame_total_sales = tk.Frame(root, bg="white")
frame_total_sales.pack(pady=50, padx=20)
tk.Label(frame_total_sales, text="Get Total Sales till Now", font=("Arial", 10), bg="white").pack()
max_price_button = tk.Button(frame_total_sales, text="Get Max Sale", command=lambda: calculate_total_sales("max"))
max_price_button.pack()
min_price_button = tk.Button(frame_total_sales, text="Get Min Sale", command=lambda: calculate_total_sales("min"))
min_price_button.pack()

# frame for date
frame_date = tk.Frame(root, bg="white")
frame_date.pack(pady=50, padx=20)
tk.Label(frame_date, text="Enter Date (dd:mm:yyyy)", font=("Arial", 10), bg="white").pack()
date_entry = tk.Entry(frame_date)
date_entry.pack()
max_price_on_date_button = tk.Button(frame_date, text="Get Max Sale on Date",
                                     command=lambda: total_sales_by_date("max"))
max_price_on_date_button.pack()
min_price_on_date_button = tk.Button(frame_date, text="Get Min Sale on Date",
                                     command=lambda: total_sales_by_date("min"))
min_price_on_date_button.pack()

# frame for most min sold item
frame_most_min_sold_item = tk.Frame(root, bg="white")
frame_most_min_sold_item.pack()
tk.Label(frame_most_min_sold_item, text="Item Name", font=("Arial", 10), bg="white").pack()
get_most_sold_item_button = tk.Button(frame_most_min_sold_item, text="Get Most Sold Item",
                                      command=lambda: get_sold_item_by_number("max"))
get_most_sold_item_button.pack()
get_min_sold_item_button = tk.Button(frame_most_min_sold_item, text="Get Least Sold Item",
                                     command=lambda: get_sold_item_by_number("min"))
get_min_sold_item_button.pack()
root.mainloop()
