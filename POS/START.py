from tkinter import *
from tkinter import messagebox
from data import items_name, items_price, order_data
import class_item as item
import class_order as order
from random import randint

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
order_no = randint(0000, 9999)


# Functions
def save_item():
    global new_item
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
        if item_name in items_name:
            messagebox.showerror("Error", "Item already exists")
            return
        else:
            items_list_box.insert(END, f"{item_name}")
            item_name_entry.delete(0, END)
            item_price_entry.delete(0, END)

            # Save new item to Database
            new_item.save_item(order_data)
            messagebox.showinfo("Success", f"{new_item.name} added for Rs.{new_item.price}")


def search_items():
    pass


def delete_item():
    global new_item
    selected_index = items_list_box.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Please select an item to delete")
        return
    elif len(selected_index) > 1:
        messagebox.showerror("Error", "Please select only one item to delete")
        items_list_box.selection_clear(0, END)
        return
    selected_index = selected_index[0]
    selected_item = items_list_box.get(selected_index)
    new_item = item.Item(selected_item, items_price[selected_index])
    new_item.delete_item(order_data)
    items_list_box.delete(selected_index)
    selected_index = None

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
    receipt_text = new_order.save_order(order_text, total_price, order_data)
    messagebox.showinfo("Order Placed!", receipt_text)
    clear_order()
    order_no = randint(0000, 9999)
    order_no_label.config(text=f"Your Order: {order_no}")


def add_ordered_items():
    global total_price, new_item
    selected_item = items_list_box.curselection()
    try:
        quantity = int(quantity_entry.get())
        if quantity < 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Quantity must be a positive integer")
        return

    if not selected_item:
        messagebox.showerror("Error", "Please select an item to order")
        return

    for x in selected_item:
        new_item = item.Item(items_name[x], items_price[x])
        order_text_box_name.insert(END, items_name[x])
        order_text_box_price.insert(END, str(items_price[x]) + ' x ' + str(quantity))
        total_price += items_price[x] * quantity
    price_label.config(text=str(total_price))
    items_list_box.selection_clear(0, END)


def clear_order():
    global total_price
    total_price = 0
    price_label.config(text=str(total_price))
    order_text_box_name.delete(0, END)
    order_text_box_price.delete(0, END)


def preload():
    if items_name and items_price:
        for x in items_name:
            items_list_box.insert(END, f"{x}")


def search_item(_=None):
    search_text = search_field.get()
    if search_text != "":
        for x in items_name:
            if len(search_text) == 1:
                if search_text.lower() == x.lower()[0]:
                    items_list_box.selection_clear(0, END)
                    items_list_box.select_set(items_name.index(x))
                    return
            else:
                if search_text.lower() in x.lower():
                    items_list_box.selection_clear(0, END)
                    items_list_box.select_set(items_name.index(x))
                    return


def search_bar_text_focus_in(event):
    search_field.delete(0, END)
    search_field['fg'] = 'black'


def search_bar_text_focus_out(event):
    search_field.delete(0, END)
    search_field.insert(0, "Search Item")
    search_field['fg'] = 'grey'


# ================ Initialize the root window ===================
root = Tk()
root.title("POS System")
root.state("zoomed")
root.configure(bg=bg_color)
root.resizable(False, False)
root.bind("<Return>", search_item)
# ===============================================================

# ================= Create a frame for the save item button ===========================
save_item_frame = Frame(root, bg=bg_color, width=700, height=180, padx=10, pady=10)
save_item_frame.place(x=5, y=5)

Label(save_item_frame, text="Save Item", font=("Arial", 20, 'bold'), bg=bg_color, fg=primary_color).grid(row=0,
                                                                                                         column=0,
                                                                                                         columnspan=4,
                                                                                                         pady=(0, 10))
Label(save_item_frame, text="Item Name:", font=("Comic Sans MS", 12), bg=bg_color, fg=text_color).grid(row=1, column=0,
                                                                                                       sticky='w')
item_name_entry = Entry(save_item_frame, font=("Arial", 12), bg="white", fg=text_color, borderwidth=0)
item_name_entry.grid(row=1, column=1, padx=10)
Label(save_item_frame, text="Item Price:", font=("Comic Sans MS", 12), bg=bg_color, fg=text_color).grid(row=1, column=2,
                                                                                                        sticky='w')
item_price_entry = Entry(save_item_frame, font=("Arial", 12), bg="white", fg=text_color, borderwidth=0)
item_price_entry.grid(row=1, column=3, padx=10)

save_item_button = Button(save_item_frame, text="Save Item", font=("Arial", 12), bg=accent_color, fg="white",
                          borderwidth=0,
                          command=save_item)
save_item_button.grid(row=1, column=4, columnspan=2, pady=10, padx=10)
# ====================================================================================


# ======================== Create a frame for the items list ===========================
items_list_frame = Frame(root, bg=bg_color, width=300, height=600, padx=10, pady=10)
items_list_frame.place(relx=0.98, rely=0.5, anchor='e')

Label(items_list_frame, text="Items List:", font=("Arial", 20, 'bold'), bg=bg_color, fg=primary_color).pack(
    anchor='center', pady=(0, 10))
search_var = StringVar()
search_var.trace("w", search_items)
items_list_box = Listbox(items_list_frame, width=30, height=20, font=("Arial", 15), bg="white", fg=primary_color,
                         borderwidth=0, justify='center', selectbackground=accent_color, selectforeground="white",
                         selectmode=MULTIPLE)
items_list_box.pack(pady=10)

delete_item_button = Button(items_list_frame, text="Delete Item", font=("Arial", 12), bg=accent_color, fg="white",
                            borderwidth=0, command=delete_item)
delete_item_button.pack(pady=10)
# ====================================================================================


# ================ Create a frame for the order preview ===========================
order_preview_frame = Frame(root, bg=bg_color, width=800, height=500, padx=10, pady=10)
order_preview_frame.place(relx=0, rely=0.5, anchor='w')

order_no_label = Label(order_preview_frame, text=f"Your Order: {order_no}", font=("Arial", 20, 'bold'), bg=bg_color,
                       fg=primary_color)
order_no_label.place(relx=0.36, rely=0.01, anchor='center')

Label(order_preview_frame, text="Item Name", font=("Comic Sans MS", 15, 'underline'), bg=bg_color,
      fg=primary_color).place(
    relx=0.2, rely=0.1, anchor='center')
order_text_box_name = Listbox(order_preview_frame, width=30, height=18, font=("Arial", 13), bg="white",
                              fg=primary_color, borderwidth=1, justify='left', selectbackground="Light Green",
                              selectforeground="black", selectmode=SINGLE)
order_text_box_name.place(relx=0, rely=0.15, anchor='nw')

Label(order_preview_frame, text="Price", font=("Comic Sans MS", 15, 'underline'), bg=bg_color, fg=primary_color).place(
    relx=0.52, rely=0.1, anchor='center')
order_text_box_price = Listbox(order_preview_frame, width=30, height=18, font=("Arial", 13), bg="white",
                               fg=primary_color, borderwidth=1, justify='center', selectbackground="Light Green",
                               selectforeground="black", selectmode=SINGLE)
order_text_box_price.place(relx=0.7, rely=0.15, anchor='ne')
# ====================================================================================


# ====================== Main root elements ===========================
# Frame
main_frame = Frame(root, bg=bg_color, padx=10, pady=10)
main_frame.place(relx=0.5, rely=0.9, anchor='center')

order_button = Button(main_frame, text="Place Order", font=("Arial", 12), bg=primary_color, fg="white", borderwidth=0,
                      width=20, height=1, command=place_order)
order_button.grid(row=0, column=0, padx=20, pady=10)
add_ordered_items_button = Button(main_frame, text="Add to Order", font=("Arial", 12), bg=primary_color, fg="white",
                                  borderwidth=0, width=20, height=1, command=add_ordered_items)
add_ordered_items_button.grid(row=0, column=1, padx=20, pady=10)

Label(main_frame, text="Quantity:", font=("Comic Sans MS", 15), fg=primary_color, bg=bg_color).grid(row=1, column=0,
                                                                                                    sticky='e',
                                                                                                    padx=(0, 10))
quantity_entry = Entry(main_frame, font=("Arial", 12), bg="white", fg=text_color, borderwidth=0, width=10,
                       justify='center')
quantity_entry.insert(END, '1')
quantity_entry.grid(row=1, column=1, sticky='w')

Label(main_frame, text="Total Price(PKR):", font=("Comic Sans MS", 15), fg=primary_color, bg=bg_color).grid(row=2,
                                                                                                            column=0,
                                                                                                            sticky='e',
                                                                                                            padx=(
                                                                                                                0, 10))
price_label = Label(main_frame, text="0", font=("Arial", 15), fg=primary_color, bg=bg_color)
price_label.grid(row=2, column=1, sticky='w')

clear_order_button = Button(main_frame, text="Clear Order", font=("Arial", 12), bg=error_color, fg="white",
                            borderwidth=0, width=20, height=1, command=clear_order)
clear_order_button.grid(row=3, column=0, columnspan=2, pady=10)

search_field = Entry(root, font=("Arial", 12), bg='light green', fg="black", borderwidth=0, width=15,
                     justify='left')
search_field.place(relx=0.62, rely=0.5)
search_button = Button(root, text="🔍", font=("Arial", 12), bg=primary_color, fg="white", borderwidth=0,
                       width=2, height=1, command=search_item)
search_button.place(relx=0.66, rely=0.53)
search_field.bind("<FocusIn>", search_bar_text_focus_in)
search_field.bind("<FocusOut>", search_bar_text_focus_out)
search_bar_text_focus_out(None)
# ====================================================================================
preload()

# Run the main loop
root.mainloop()
