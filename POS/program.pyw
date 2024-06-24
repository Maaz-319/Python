from tkinter import *
from tkinter import messagebox
from data import order_data, items_list, current_cashier, cashier_login
import class_item as item
import class_order as order
from random import randint
import datetime

# Global variables
bg_color = "#f0f0f0"
primary_color = "#004d40"
accent_color = "#00bfa5"
text_color = "#333333"
error_color = "#ff5252"
total_price = 0
new_item = None
new_customer = None
new_order = None
item_price_entry = None
item_name_entry = None
save_item_window = None
items_list_sorted = None
order_no = randint(0000, 9999)


# Functions
def authorize():
    if not current_cashier:
        messagebox.showerror("Error", "Please login to continue")
        root.destroy()
    else:
        preload()


def save_item():
    global new_item, item_name_entry, item_price_entry, save_item_window
    try:
        item_name = item_name_entry.get()
        item_price = int(item_price_entry.get())
        if item_price < 1:
            raise ValueError
        new_item = item.Item(item_name, item_price)
    except ValueError:
        messagebox.showerror("Error", "Item Price must be a positive integer")
        return

    if item_name == "":
        messagebox.showerror("Error", "All fields are required")
    else:
        if item_name in items_list.keys():
            messagebox.showerror("Error", "Item already exists")
            return
        else:
            items_list_box.insert(END, f"{item_name}")
            item_name_entry.delete(0, END)
            item_price_entry.delete(0, END)

            # Save new item to Database
            new_item.save_item(order_data)
            preload()
            messagebox.showinfo("Success", f"{new_item.name} added for Rs.{new_item.price}")
            items_list_box.select_set(list(items_list_sorted.keys()).index(new_item.name))
            save_item_window.destroy()


def create_save_item_window(_=None):
    global item_name_entry, item_price_entry, save_item_window
    save_item_window = Toplevel()
    save_item_window.title("Add New Item")
    save_item_window.geometry("400x200")
    save_item_window.configure(bg=bg_color)
    save_item_window.resizable(False, False)

    item_name_label = Label(save_item_window, text="Item Name:", font=("Arial", 12), bg=bg_color, fg=text_color)
    item_name_label.place(relx=0.1, rely=0.1)
    item_name_entry = Entry(save_item_window, font=("Arial", 12), bg="white", fg=text_color, borderwidth=0)
    item_name_entry.place(relx=0.3, rely=0.1)

    item_price_label = Label(save_item_window, text="Item Price:", font=("Arial", 12), bg=bg_color, fg=text_color)
    item_price_label.place(relx=0.1, rely=0.3)
    item_price_entry = Entry(save_item_window, font=("Arial", 12), bg="white", fg=text_color, borderwidth=0)
    item_price_entry.place(relx=0.3, rely=0.3)

    save_button = Button(save_item_window, text="Save Item", font=("Arial", 12), bg=accent_color, fg="white",
                         borderwidth=0, command=save_item)
    save_button.place(relx=0.4, rely=0.5)

    save_item_window.mainloop()


def delete_item(_=None):
    global new_item
    selected_index = items_list_box.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Please select an item to delete")
        return
    elif len(selected_index) > 1:
        messagebox.showerror("Error", "Please select only one item to delete")
        items_list_box.selection_clear(0, END)
        return
    if messagebox.askokcancel("Delete Item", "Are you sure you want to delete this item?"):
        selected_index = selected_index[0]
        selected_item = items_list_box.get(selected_index)
        # print(items_list[selected_item])
        new_item = item.Item(selected_item, items_list[selected_item])
        new_item.delete_item(order_data)
        selected_index = None
        preload()
        messagebox.showinfo("Deleted", f"'{new_item.name} - {new_item.price} Rs' has been deleted!")


def place_order():
    global total_price, order_no, new_order, new_item
    new_item = "None"
    order_text = ""
    if not order_text_box_name.get(0, END):
        messagebox.showerror("Error", "Please add items to order")
        return
    orders_name = order_text_box_name.get(0, END)
    orders_price = order_text_box_price.get(0, END)
    new_order = order.Order(order_no, new_item)
    for x in orders_name:
        new_item = item.Item(x, orders_price[orders_name.index(x)])
        new_order.items.append(new_item)
        order_text = f"{order_text}\n{x} - {orders_price[orders_name.index(x)]}"
    receipt_text = new_order.save_order(order_text, total_price, order_data,
                                        datetime.datetime.now().strftime("%I:%M %p, %d:%m:%Y"))
    user_choice = messagebox.askquestion("Order Placed!", f"{receipt_text}\n\n\nPrint Receipt?", icon='info')
    print_receipt(receipt_text) if user_choice == 'yes' else None
    clear_order()
    order_no = randint(0000, 9999)
    order_no_label.config(text=f"Your Order: {order_no}")


def print_receipt(receipt_text):
    with open(f'{order_no}.txt', 'w') as f:
        f.write(receipt_text)
        f.close()
    messagebox.showinfo("Receipt Printed", "Receipt has been printed successfully")


def add_ordered_items(_=None):
    global total_price, new_item, items_list_sorted
    selected_item = items_list_box.curselection()
    try:
        quantity = int(quantity_spinbox.get())
        if quantity < 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Quantity must be a positive integer")
        return

    if not selected_item:
        messagebox.showerror("Error", "Please select an item to order")
        return
    for x in selected_item:
        new_item = item.Item(list(items_list_sorted.keys())[x], items_list[list(items_list_sorted.keys())[x]])
        order_text_box_name.insert(END, list(items_list_sorted.keys())[x])
        order_text_box_price.insert(END, str(items_list[list(items_list_sorted.keys())[x]]) + ' x ' + str(quantity))
        total_price += items_list[list(items_list_sorted.keys())[x]] * quantity
    price_label.config(text=str(total_price))
    items_list_box.selection_clear(0, END)


def clear_order():
    global total_price
    total_price = 0
    price_label.config(text=str(total_price))
    order_text_box_name.delete(0, END)
    order_text_box_price.delete(0, END)
    responsive_price_preview_label.config(text="")


def preload():
    global items_list_sorted
    if items_list:
        items_list_box.delete(0, END)
        items_list_sorted = {key: items_list[key] for key in sorted(items_list)}
        # items_list = items_list_sorted
        for x in items_list_sorted.keys():
            items_list_box.insert(END, f"{x}")


def search_item(_=None):
    global items_list_sorted
    search_text = search_field.get()
    if search_text != "":
        for x in items_list_sorted.keys():
            if len(search_text) == 1:
                if search_text.lower() == x.lower()[0]:
                    items_list_box.selection_clear(0, END)
                    items_list_box.select_set(list(items_list_sorted.keys()).index(x))
                    return
            else:
                if search_text.lower() in x.lower():
                    items_list_box.selection_clear(0, END)
                    items_list_box.select_set(list(items_list_sorted.keys()).index(x))
                    return
    return


# This function is called when the search bar is Focused or Clicked
def search_bar_text_focus_in(event):
    search_field.delete(0, END)
    search_field['fg'] = 'black'


# This function is called when the search bar is not focused or clicked
def search_bar_text_focus_out(event):
    search_field.delete(0, END)
    search_field.insert(0, "Search Item")
    search_field['fg'] = 'grey'


# This Function is called when the user presses the 'Ctrl + F' key combination
def focus_search_bar(event):
    search_field.focus_set()


def on_select_order_name(event):
    selection = order_text_box_name.curselection()
    if selection:
        responsive_price_preview_label.config(text=items_list[order_text_box_name.get(selection[0])])
    else:
        responsive_price_preview_label.config(text="")


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        with open('data.py', 'w') as f:
            f.write(
                f'items_list = {items_list}\norder_data = {order_data}\ncashier_login = {cashier_login}\ncurrent_cashier = None\n')
            f.close()
        root.destroy()


def light_theme(element):
    if element in [search_frame, items_list_frame, order_preview_frame, total_price_frame]:
        element['background'] = bg_color
        return
    element['background'] = bg_color
    element['foreground'] = text_color


def dark_theme(element):
    if element in [search_frame, items_list_frame, order_preview_frame, total_price_frame]:
        element['background'] = text_color
        return
    element['background'] = text_color
    element['foreground'] = bg_color


def change_theme(mode):
    if mode == 0:
        # dark theme
        theme_button['command'] = lambda: change_theme(1)
        theme_button['text'] = 'Light Theme'

        # managing colors
        root.configure(bg=text_color)
        light_theme(theme_button)
        dark_theme(search_frame)
        dark_theme(items_list_frame)
        dark_theme(order_preview_frame)
        dark_theme(total_price_frame)
        dark_theme(order_no_label)
        dark_theme(responsive_price_preview_label)
        dark_theme(price_label)
        dark_theme(order_text_box_name)
        dark_theme(order_text_box_price)
        dark_theme(cashier_label)
        dark_theme(item_list_preview_label)
        dark_theme(total_price_preview_label)
        dark_theme(item_name_preview_label)
        dark_theme(item_price_preview_label)
        dark_theme(quantity_preview_label)
        dark_theme(items_list_box)
        dark_theme(quantity_spinbox)
    else:
        # light theme
        theme_button['command'] = lambda: change_theme(0)
        theme_button['text'] = 'Dark Theme'

        # managing colors
        root.configure(bg=bg_color)
        dark_theme(theme_button)
        light_theme(search_frame)
        light_theme(items_list_frame)
        light_theme(order_preview_frame)
        light_theme(total_price_frame)
        light_theme(order_no_label)
        light_theme(responsive_price_preview_label)
        light_theme(price_label)
        light_theme(order_text_box_name)
        light_theme(order_text_box_price)
        light_theme(cashier_label)
        light_theme(item_list_preview_label)
        light_theme(total_price_preview_label)
        light_theme(item_name_preview_label)
        light_theme(item_price_preview_label)
        light_theme(quantity_preview_label)
        light_theme(items_list_box)
        light_theme(quantity_spinbox)


# ================ Initialize the root window ===================
root = Tk()
root.title("POS System")
root.state("zoomed")
root.configure(bg=bg_color)
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_closing)

root.bind("<Return>", search_item)
root.bind('<Control-f>', focus_search_bar)
root.bind('<Control-n>', create_save_item_window)
root.bind('<Delete>', delete_item)
# ===============================================================

# ================= root items ===========================
save_item_button = Button(root, text="Add New Item", font=("Arial", 12), bg=accent_color, fg="white",
                          borderwidth=0,
                          command=create_save_item_window)
save_item_button.place(relx=0.92, rely=0.005)
show_keyboard_shortcuts = Button(root, text="⌘", font=("Arial", 12), bg=primary_color, fg="white",
                                 borderwidth=0, height=1, command=lambda: messagebox.showinfo("Keyboard Shortcuts",
                                                                                              "Ctrl + F: Seach Item\nCtrl + N: Add New Item\nDelete: Delete Item"))
show_keyboard_shortcuts.place(relx=0.005, rely=0.005)
cashier_label = Label(root, text=f"Logged in: {current_cashier}", font=("Arial", 12, 'bold'), bg=bg_color,
                      fg=primary_color)
cashier_label.place(relx=0.1, rely=0.015, anchor='center')
theme_button = Button(root, text='Dark Theme', font=("Arial", 12), height=1, borderwidth=0, bg=text_color, fg=bg_color,
                      command=lambda: change_theme(0))
theme_button.place(relx=0.45, rely=0.01)
# ====================================================================================


# ======================== Create a frame for the items list ===========================
items_list_frame = Frame(root, bg=bg_color, width=500, height=700, padx=10, pady=10)
items_list_frame.place(relx=0.4, rely=0.5, anchor='e')

item_list_preview_label = Label(items_list_frame, text="Items List:", font=("Arial", 20, 'bold'), bg=bg_color,
                                fg=primary_color)
item_list_preview_label.place(relx=0.35, rely=0.01)
# search_var = StringVar()
# search_var.trace("w", search_items)
items_list_box = Listbox(items_list_frame, width=45, height=23, font=("Arial", 15), bg="white", fg=primary_color,
                         borderwidth=0, justify='center', selectbackground=accent_color, selectforeground="white",
                         selectmode=MULTIPLE)
items_list_box.place(relx=0.5, rely=0.48, anchor='center')
items_list_box.bind("<Double-Button-1>", add_ordered_items)

order_button = Button(items_list_frame, text="Add to Order", font=("Arial", 12), bg=primary_color, fg="white",
                      borderwidth=0, width=20, height=1, command=add_ordered_items)
order_button.place(relx=0.8, rely=0.915, anchor='center')

delete_item_button = Button(items_list_frame, text="Delete Item", font=("Arial", 12), bg=error_color, fg="white",
                            borderwidth=0, command=delete_item)
delete_item_button.place(relx=0.1, rely=0.915, anchor='center')

scrollbar = Scrollbar(items_list_frame, orient=VERTICAL, command=items_list_box.yview, takefocus=0, relief='flat', bd=0,
                      cursor='hand2', width=20)
scrollbar.place(relx=0.99, rely=0.48, anchor='center', relheight=0.7)

items_list_box.config(yscrollcommand=scrollbar.set)

# quantity_spinbox = Entry(items_list_frame, font=("Arial", 12), bg="white", fg=text_color, borderwidth=0, width=10,
#                        justify='center')
# quantity_spinbox.insert(END, '1')
# quantity_spinbox.place(relx=0.43, rely=0.97)
quantity_preview_label = Label(items_list_frame, text="Quantity:", font=("Comic Sans MS", 15), fg=primary_color,
                               bg=bg_color)
quantity_preview_label.place(relx=0.23, rely=0.96)
quantity_spinbox = Spinbox(items_list_frame, from_=1, to=100)
quantity_spinbox.place(relx=0.43, rely=0.97)
# ====================================================================================


# ================ Create a frame for the order preview ===========================
order_preview_frame = Frame(root, bg=bg_color, width=800, height=500, padx=10, pady=10)
order_preview_frame.place(relx=0.58, rely=0.45, anchor='w')

order_no_label = Label(order_preview_frame, text=f"Your Order: {order_no}", font=("Arial", 20, 'bold'), bg=bg_color,
                       fg=primary_color)
order_no_label.place(relx=0.36, rely=0.01, anchor='center')

item_name_preview_label = Label(order_preview_frame, text="Item Name", font=("Comic Sans MS", 15, 'underline'),
                                bg=bg_color,
                                fg=primary_color)
item_name_preview_label.place(relx=0.17, rely=0.1, anchor='center')
order_text_box_name = Listbox(order_preview_frame, width=30, height=18, font=("Arial", 13), bg="white",
                              fg=primary_color, borderwidth=1, justify='left', selectbackground="Light Green",
                              selectforeground="black", selectmode=SINGLE)
order_text_box_name.place(relx=0, rely=0.15, anchor='nw')
order_text_box_name.bind('<<ListboxSelect>>', lambda e: on_select_order_name(order_text_box_name))

item_price_preview_label = Label(order_preview_frame, text="Price", font=("Comic Sans MS", 15, 'underline'),
                                 bg=bg_color, fg=primary_color)
item_price_preview_label.place(relx=0.52, rely=0.1, anchor='center')
order_text_box_price = Listbox(order_preview_frame, width=30, height=18, font=("Arial", 13), bg="white",
                               fg=primary_color, borderwidth=1, justify='center', selectbackground="Light Green",
                               selectforeground="black", selectmode=SINGLE)
order_text_box_price.place(relx=0.7, rely=0.15, anchor='ne')
order_text_box_price.bind('<<ListboxSelect>>', lambda e: on_select_order_name(order_text_box_price))

clear_order_button = Button(order_preview_frame, text="Clear Order", font=("Arial", 12), bg=error_color, fg="white",
                            borderwidth=0, width=20, height=1, command=clear_order)
clear_order_button.place(relx=0.25, rely=0.92)
responsive_price_preview_label = Label(order_preview_frame, font=("Comic Sans MS", 10),
                                       fg=primary_color, bg=bg_color)
responsive_price_preview_label.place(relx=0.57, rely=0.08)
# ====================================================================================

# ================= Create a frame for the total price ===========================
total_price_frame = Frame(root, bg=bg_color, width=450, height=150, padx=10, pady=10)
total_price_frame.place(relx=0.67, rely=0.9, anchor='w')
total_price_preview_label = Label(total_price_frame, text="Total Price(PKR):", font=("Comic Sans MS", 20),
                                  fg=primary_color, bg=bg_color)
total_price_preview_label.place(relx=0.1, rely=0.05)
price_label = Label(total_price_frame, text="0", font=("Arial", 20), fg=primary_color, bg=bg_color)
price_label.place(relx=0.62, rely=0.07)
order_button = Button(total_price_frame, text="Place Order", font=("Arial", 13), bg=primary_color, fg="white",
                      borderwidth=0, width=20, height=2, command=place_order)
order_button.place(relx=0.14, rely=0.5)
# ====================================================================================

# ====================== Search Frame ===========================
search_frame = Frame(root, bg=bg_color, width=250, height=50, padx=10, pady=10)
search_frame.place(relx=0.7, rely=0.03, anchor='w')

search_field = Entry(search_frame, font=("Arial", 16), bg='light green', fg="black", borderwidth=0, width=15,
                     justify='left')
search_field.place(relx=0.003, rely=0.1)
search_button = Button(search_frame, text="🔍", font=("Arial", 12), bg=primary_color, fg="white", borderwidth=0,
                       width=2, height=1, command=search_item)
search_button.place(relx=0.88, rely=0.1)
search_field.bind("<FocusIn>", search_bar_text_focus_in)
search_field.bind("<FocusOut>", search_bar_text_focus_out)
search_bar_text_focus_out(None)
# ====================================================================================
authorize()
# preload()

# Run the main loop
root.mainloop()
