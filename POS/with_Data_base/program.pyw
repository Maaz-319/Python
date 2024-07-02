from tkinter import *
from tkinter import messagebox
from data import current_cashier
import class_item as item
import class_order as order
from random import randint
import datetime
import database_handler_item as db_item
import database_handler_order as db_order
import webbrowser

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
theme_changed = False
the_item = []
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
        new_item = item.Item(item_name.capitalize(), item_price)
    except ValueError:
        save_item_window.destroy()
        messagebox.showerror("Error", "Item Price must be a positive integer")
        return

    if item_name == "":
        messagebox.showerror("Error", "All fields are required")
        save_item_window.destroy()
    else:
        if item_name.lower() in db_item.get_all_items_name():
            messagebox.showerror("Error", "Item already exists")
            save_item_window.destroy()
            return
        else:
            # Save new item to Database
            new_item.save_item()
            item_name_entry.delete(0, END)
            item_price_entry.delete(0, END)
            preload()
            items_list_box.see(items_list_box.get(0, END).index(new_item.name))
            messagebox.showinfo("Success", f"{new_item.name} added for Rs.{new_item.price}")
            save_item_window.destroy()


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
        new_item = item.Item(selected_item, db_item.get_item_by_name(selected_item)[1])
        new_item.delete_item()
        selected_index = None
        preload()
        messagebox.showinfo("Deleted", f"'{new_item.name} - {new_item.price} Rs' has been deleted!")


def create_modify_item_price(_=None):
    global new_item
    selected_index = items_list_box.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Please select an item to Modify")
        return
    elif len(selected_index) > 1:
        messagebox.showerror("Error", "Please select only one item to Modify")
        items_list_box.selection_clear(0, END)
        return
    else:
        update_window = Toplevel()
        update_window.title("Update Price")
        update_window.geometry("300x200")
        update_window.configure(bg=bg_color)
        update_window.resizable(False, False)

        selected_index = selected_index[0]
        selected_item = items_list_box.get(selected_index)

        Label(update_window, text=f"Enter Price for {selected_item}:", font=("Arial", 12), bg=bg_color,
              fg=text_color).place(relx=0.1, rely=0.1)
        price_entry = Entry(update_window, font=("Arial", 12), bg=bg_color, fg=text_color, borderwidth=1)
        price_entry.place(relx=0.1, rely=0.3)

        btn = Button(update_window, text="Update Price", font=("Arial", 12), bg=accent_color, fg="white",
                     borderwidth=0, command=lambda: modify_item_price(selected_item, price_entry.get(), update_window))
        btn.place(relx=0.1, rely=0.5)

        update_window.mainloop()


def modify_item_price(selected_item, modified_price, window):
    try:
        modified_price = int(modified_price)
        if modified_price < 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Price must be a positive integer")
        return
    global new_item
    new_item = item.Item(selected_item, modified_price)
    new_item.update_item()
    preload()
    window.destroy()
    messagebox.showinfo("Updated", f"'{new_item.name} - {new_item.price} Rs' has been updated!")


def place_order():
    global total_price, order_no, new_order, new_item, the_item
    order_text = ""
    if not order_text_box_name.get(0, END):
        messagebox.showerror("Error", "Please add items to order")
        return
    orders_name = order_text_box_name.get(0, END)
    orders_price = order_text_box_price.get(0, END)
    new_order = order.Order(order_no, [], str(datetime.datetime.now().strftime("%I:%M %p, %d:%m:%Y")), current_cashier)
    for x in orders_name:
        new_item = item.Item(x, orders_price[orders_name.index(x)])
        new_order.items.append(new_item)
        order_text = f"{order_text}\n{x} - {orders_price[orders_name.index(x)]}"
    receipt_text = new_order.save_order(order_text, total_price)
    user_choice = messagebox.askquestion("Order Placed!", f"{receipt_text}\n\n\nPrint Receipt?", icon='info')
    print_receipt(receipt_text) if user_choice == 'yes' else None
    clear_order()
    order_no = randint(0000, 9999)
    order_no_label.config(text=f"Your Order: {order_no}")
    the_item = []


def print_receipt(receipt_text):
    with open(f'{order_no}.txt', 'w') as f:
        f.write(receipt_text)
    messagebox.showinfo("Receipt Printed", "Receipt has been printed successfully")


def add_ordered_items():
    global total_price, new_item, the_item
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
        if items_list_box.get(x) in the_item:
            if messagebox.askyesno("Item Found", f"{items_list_box.get(x)} Already in Order\nAdd {quantity} more?"):
                item_index = order_text_box_name.get(0, "end").index(items_list_box.get(x))
                item_things = order_text_box_price.get(item_index).split(' x ')
                order_text_box_price.delete(item_index)
                order_text_box_name.delete(item_index)
                order_text_box_name.insert(END, items_list_box.get(x))
                order_text_box_price.insert(END, f"{item_things[0]} x {int(item_things[1]) + quantity}")
                total_price += int(item_things[0]) * quantity
        else:
            the_item.append(items_list_box.get(x))
            new_item = item.Item(items_list_box.get(x), db_item.get_item_by_name(items_list_box.get(x))[1])
            order_text_box_name.insert(END, new_item.name)
            order_text_box_price.insert(END,
                                        str(new_item.price) + ' x ' + str(quantity))
            total_price += new_item.price * quantity
    price_label.config(text=str(total_price))
    items_list_box.selection_clear(0, END)
    quantity_spinbox.delete(0, "end")
    quantity_spinbox.insert(0, "1")


def search_item(_=None):
    search_text = search_field.get()
    if search_text != "":
        for x in db_item.get_all_items_name():
            if len(search_text) == 1:
                if search_text.lower() == x[0]:
                    items_list_box.selection_clear(0, END)
                    items_list_box.select_set(items_list_box.get(0, END).index(x.capitalize()))
                    items_list_box.see(items_list_box.get(0, END).index(x.capitalize()))
                    return
            else:
                if search_text.lower() in x:
                    items_list_box.selection_clear(0, END)
                    items_list_box.select_set(items_list_box.get(0, END).index(x.capitalize()))
                    items_list_box.see(items_list_box.get(0, END).index(x.capitalize()))
                    return
    return


def clear_order():
    global total_price
    total_price = 0
    price_label.config(text=str(total_price))
    order_text_box_name.delete(0, END)
    order_text_box_price.delete(0, END)
    responsive_price_preview_label.config(text="")


def preload():
    items_list_box.delete(0, END)
    items_name = []
    for x in db_item.get_all_items():
        items_name.append(x[0])
    for x in items_name:
        items_list_box.insert(END, x)


# This function is called when the search bar is Focused or Clicked
def search_bar_text_focus_in(event):
    search_field.delete(0, END)
    search_field['fg'] = 'black'


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
    item_name_entry.place(relx=0.35, rely=0.1)

    item_price_label = Label(save_item_window, text="Item Price:", font=("Arial", 12), bg=bg_color, fg=text_color)
    item_price_label.place(relx=0.1, rely=0.3)
    item_price_entry = Entry(save_item_window, font=("Arial", 12), bg="white", fg=text_color, borderwidth=0)
    item_price_entry.place(relx=0.35, rely=0.3)

    save_button = Button(save_item_window, text="Save Item", font=("Arial", 12), bg=accent_color, fg="white",
                         borderwidth=0, command=save_item)
    save_button.place(relx=0.4, rely=0.5)

    save_item_window.mainloop()


def feedback():
    webbrowser.open_new_tab("https://forms.gle/PPwtdPAD4t975ZLD8")


# This function is called when the search bar is not focused or clicked
def search_bar_text_focus_out(event):
    search_field.delete(0, END)
    search_field.insert(0, "Search Item")
    search_field['fg'] = 'grey'


# This Function is called when the user presses the 'Ctrl + F' key combination
def focus_search_bar(event):
    search_field.focus_set()


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        with open('data.py', 'w') as f:
            f.write(
                f'current_cashier = None\n')
        db_item.end_connection()
        db_order.end_connection()
        root.destroy()


def update_listboxes(*args):
    # items_price_list_box.yview(*args)
    items_list_box.yview(*args)


def light_theme(element):
    if element in [search_frame, items_list_frame, order_preview_frame, total_price_frame]:
        element['background'] = "white"
        return
    element['background'] = bg_color
    element['foreground'] = text_color


def dark_theme(element):
    if element in [search_frame, items_list_frame, order_preview_frame, total_price_frame]:
        element['background'] = text_color
        return
    element['background'] = text_color
    element['foreground'] = bg_color


def change_theme():
    global theme_changed
    if not theme_changed:
        # dark theme

        # managing colors
        root.configure(bg=text_color)
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

        # managing colors
        root.configure(bg=bg_color)
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
    theme_changed = not theme_changed


def buttons_hover_control_focus_in(element, message):
    if element in [order_text_box_name, order_text_box_price, items_list_box, search_field]:
        root.title(f"POS | By Maaz | {message}")
        return
    element['borderwidth'] = 1
    root.title(f"POS | By Maaz | {message}")


def buttons_hover_control_focus_out(element):
    if element in [order_text_box_name, order_text_box_price, items_list_box, search_field]:
        root.title(f"POS | By Maaz")
        return
    element['borderwidth'] = 0
    root.title("POS | By Maaz")


# ================ Initialize the root window ===================
root = Tk()
root.title("POS | By Maaz")
root.state("zoomed")
root.configure(bg=bg_color)
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_closing)

root.bind("<Return>", search_item)
root.bind('<Control-f>', focus_search_bar)
root.bind('<Control-n>', create_save_item_window)
root.bind('<Delete>', delete_item)
# ===============================================================


# ======================== Create a frame for the items list ===========================
items_list_frame = Frame(root, bg=bg_color, width=700, height=700, padx=10, pady=10)
items_list_frame.place(relx=0.4, rely=0.5, anchor='e')

item_list_preview_label = Label(items_list_frame, text="Items List:", font=("Arial", 20, 'bold'), bg=bg_color,
                                fg=primary_color)
item_list_preview_label.place(relx=0.35, rely=0.01)
# search_var = StringVar()
# search_var.trace("w", search_items)

items_list_box = Listbox(items_list_frame, width=35, height=23, font=("Arial", 15), bg="white", fg=primary_color,
                         borderwidth=0, justify='center', selectbackground=accent_color, selectforeground="white",
                         selectmode=MULTIPLE, cursor='hand2')
items_list_box.place(relx=0.51, rely=0.48, anchor='center')
items_list_box.bind("<Double-Button-1>", create_modify_item_price)
items_list_box.bind("<Enter>", lambda e: buttons_hover_control_focus_in(items_list_box,
                                                                        "Double Click any Item to Update its Price"))
items_list_box.bind("<Leave>", lambda e: buttons_hover_control_focus_out(items_list_box))
# items_price_list_box = Listbox(items_list_frame, width=10, height=23, font=("Arial", 15), bg="white", fg=primary_color,
#                                borderwidth=0, justify='center', selectbackground=accent_color, selectforeground="white",
#                                selectmode=MULTIPLE, cursor='hand2')
# items_price_list_box.place(relx=0.9, rely=0.48, anchor='center')

order_button = Button(items_list_frame, text="Add to Order", font=("Arial", 12), bg=primary_color, fg="white",
                      borderwidth=0, width=20, height=1, command=add_ordered_items, cursor='hand2')
order_button.place(relx=0.8, rely=0.915, anchor='center')
order_button.bind("<Enter>", lambda e: buttons_hover_control_focus_in(order_button, "Add Selected Items to your Order"))
order_button.bind("<Leave>", lambda e: buttons_hover_control_focus_out(order_button))

delete_item_button = Button(items_list_frame, text="Delete Item", font=("Arial", 12), bg=error_color, fg="white",
                            borderwidth=0, command=delete_item, cursor='hand2')
delete_item_button.place(relx=0.3, rely=0.915, anchor='center')
delete_item_button.bind("<Enter>", lambda e: buttons_hover_control_focus_in(delete_item_button,
                                                                            "Delete Selected Item from DataBase"))
delete_item_button.bind("<Leave>", lambda e: buttons_hover_control_focus_out(delete_item_button))

scrollbar = Scrollbar(items_list_frame, orient=VERTICAL, takefocus=0, relief='flat', bd=0,
                      cursor='hand2', width=20, command=update_listboxes)
scrollbar.place(relx=0.78, rely=0.48, anchor='center', relheight=0.7)
# items_price_list_box.config(yscrollcommand=scrollbar.set)
items_list_box.config(yscrollcommand=scrollbar.set)
# items_list_box.unbind("<MouseWheel>")
# items_price_list_box.unbind("<MouseWheel>")

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
order_text_box_name.bind("<Enter>", lambda f: buttons_hover_control_focus_in(order_text_box_name,
                                                                             "Item Price is Shown Right in Front of Each item"))
order_text_box_name.bind("<Leave>", lambda f: buttons_hover_control_focus_out(order_text_box_name))

item_price_preview_label = Label(order_preview_frame, text="Price", font=("Comic Sans MS", 15, 'underline'),
                                 bg=bg_color, fg=primary_color)
item_price_preview_label.place(relx=0.52, rely=0.1, anchor='center')
order_text_box_price = Listbox(order_preview_frame, width=30, height=18, font=("Arial", 13), bg="white",
                               fg=primary_color, borderwidth=1, justify='center', selectbackground="Light Green",
                               selectforeground="black", selectmode=SINGLE)
order_text_box_price.place(relx=0.7, rely=0.15, anchor='ne')
order_text_box_price.bind("<Enter>", lambda f: buttons_hover_control_focus_in(order_text_box_price,
                                                                              "Item Price is Shown Right in Front of Each item"))
order_text_box_price.bind("<Leave>", lambda f: buttons_hover_control_focus_out(order_text_box_price))

clear_order_button = Button(order_preview_frame, text="Clear Order", font=("Arial", 12), bg=error_color, fg="white",
                            borderwidth=0, width=20, height=1, command=clear_order, cursor='hand2')
clear_order_button.place(relx=0.25, rely=0.92)
clear_order_button.bind("<Enter>", lambda e: buttons_hover_control_focus_in(clear_order_button,
                                                                            "Remove all the Items from your Order"))
clear_order_button.bind("<Leave>", lambda e: buttons_hover_control_focus_out(clear_order_button))

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
place_order_button = Button(total_price_frame, text="Place Order", font=("Arial", 13), bg=primary_color, fg="white",
                            borderwidth=0, width=20, height=2, command=place_order, cursor='hand2')
place_order_button.place(relx=0.14, rely=0.5)
place_order_button.bind("<Enter>", lambda e: buttons_hover_control_focus_in(place_order_button,
                                                                            "Place the Order for Selected Items"))
place_order_button.bind("<Leave>", lambda e: buttons_hover_control_focus_out(place_order_button))
# ====================================================================================

# ====================== Search Frame ===========================
search_frame = Frame(root, bg=bg_color, width=250, height=50, padx=10, pady=10)
search_frame.place(relx=0.7, rely=0.03, anchor='w')

search_button = Button(search_frame, text="🔍", font=("Arial", 12), bg=primary_color, fg="white", borderwidth=0,
                       width=2, height=1, command=search_item, cursor='hand2')
search_button.place(relx=0.88, rely=0.1)
search_button.bind("<Enter>", lambda e: buttons_hover_control_focus_in(search_button,
                                                                       "Enter Item name in Search Bar and Press Enter or Click the Search Button"))
search_button.bind("<Leave>", lambda e: buttons_hover_control_focus_out(search_button))

search_field = Entry(search_frame, font=("Arial", 16), bg='light green', fg="black", borderwidth=0, width=15,
                     justify='left')
search_field.place(relx=0.003, rely=0.1)
search_field.bind("<Enter>", lambda e: buttons_hover_control_focus_in(search_field,
                                                                      "Enter Item name in Search Bar and Press Enter or Click the Search Button"))
search_field.bind("<Leave>", lambda e: buttons_hover_control_focus_out(search_field))

search_field.bind("<FocusIn>", search_bar_text_focus_in)
search_field.bind("<FocusOut>", search_bar_text_focus_out)
search_bar_text_focus_out(None)
# ====================================================================================

# ================= root items ===========================
# save_item_button = Button(root, text="Add New Item", font=("Arial", 12), bg=accent_color, fg="white",
#                           borderwidth=0, command=create_save_item_window, cursor='hand2')
# save_item_button.bind("<Enter>", lambda e: buttons_hover_control_focus_in(save_item_button, "Add New Item"))
# save_item_button.bind("<Leave>", lambda e: buttons_hover_control_focus_out(save_item_button))
#
# save_item_button.place(relx=0.92, rely=0.005)

# show_keyboard_shortcuts = Button(root, text="⌘", font=("Arial", 12), bg=primary_color, fg="white", cursor='hand2',
#                                  borderwidth=0, height=1, command=lambda: messagebox.showinfo("Keyboard Shortcuts",
#                                                                                               "Ctrl + F: Search Item\nCtrl + N: Add New Item\nDelete: Delete Item"))
# show_keyboard_shortcuts.place(relx=0.005, rely=0.005)
# show_keyboard_shortcuts.bind("<Enter>", lambda e: buttons_hover_control_focus_in(show_keyboard_shortcuts,
#                                                                                  "View all Keyboard Shortcuts to Use POS with Ease"))
# show_keyboard_shortcuts.bind("<Leave>", lambda e: buttons_hover_control_focus_out(show_keyboard_shortcuts))

cashier_label = Label(root, text=f"Logged in: {current_cashier}", font=("Arial", 12, 'bold'), bg=bg_color,
                      fg=primary_color)
cashier_label.place(relx=0.45, rely=0.015, anchor='center')

# theme_button = Button(root, text='Dark Theme', font=("Arial", 12), height=1, borderwidth=0, bg=text_color, fg=bg_color,
#                       command=lambda: change_theme(0), cursor='hand2')
# theme_button.place(relx=0.45, rely=0.01)
# theme_button.bind("<Enter>",
#                   lambda e: buttons_hover_control_focus_in(theme_button, "Change the Colour theme of the Program"))
# theme_button.bind("<Leave>", lambda e: buttons_hover_control_focus_out(theme_button))

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Add New Item", command=create_save_item_window)
file_menu.add_command(label="Change Theme", command=change_theme)
file_menu.add_command(label="Shortcuts", command=lambda: messagebox.showinfo("Keyboard Shortcuts",
                                                                             "Ctrl + F: Search Item\nCtrl + N: Add New Item\nDelete: Delete Item"))
file_menu.add_separator()
file_menu.add_command(label="Feedback", command=feedback)
file_menu.add_command(label="Exit", command=on_closing)
root.config(menu=menu_bar)
# ====================================================================================

authorize()
# preload()
# Run the main loop
root.mainloop()
