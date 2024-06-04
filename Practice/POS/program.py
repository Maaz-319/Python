from tkinter import *
from tkinter import messagebox
from data import items_name, items_price, order_data
from random import randint

# Global variables
bg_color = "#f0f0f0"
primary_color = "#004d40"
accent_color = "#00bfa5"
text_color = "#333333"
error_color = "#ff5252"
total_price = 0


# Functions
def save_data_to_file():
    with open('data.py', 'w') as f:
        f.write(f'items_name = {items_name}\nitems_price = {items_price}\norder_data = {order_data}')
        f.close()


def preload():
    if items_name and items_price:
        for x in items_name:
            items_list_box.insert(END, f"{x} - {items_price[items_name.index(x)]}")


def save_item():
    try:
        item_name = item_name_entry.get()
        item_price = int(item_price_entry.get())
        if item_price < 1:
            raise ValueError
        items_name.append(item_name)
        items_price.append(item_price)
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
            items_name.append(item_name)
            items_price.append(item_price)
            save_data_to_file()
            items_list_box.insert(END, f"{item_name} - {item_price}")
            item_name_entry.delete(0, END)
            item_price_entry.delete(0, END)


def add_ordered_items():
    global total_price
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
        order_text_box.insert(END, str(items_list_box.get(x)) + ' - x' + str(quantity))
        total_price += items_price[x] * quantity
    price_label.config(text=str(total_price))


def delete_item():
    selected_item = items_list_box.get(ANCHOR)
    if not selected_item:
        messagebox.showerror("Error", "Please select an item to delete")
        return
    index = items_list_box.index(ANCHOR)
    items_list_box.delete(ANCHOR)
    del items_name[index]
    del items_price[index]
    del order_data[index]
    with open('data.py', 'w') as f:
        f.write(f'items_name = {items_name}\nitems_price = {items_price}\norder_data = {order_data}')
        f.close()
    messagebox.showinfo("Deleted", f"'{str(selected_item).split(' ')[0]}' has been deleted!")


def place_order():
    global total_price
    if not order_text_box.get(0, END):
        messagebox.showerror("Error", "Please add items to order")
        return
    order_text = "\n".join(order_text_box.get(0, END))
    receipt_text = f"Order Receipt\n\n{order_text}\n\nTotal Price: Rs {total_price}"
    messagebox.showinfo(f"Order nO. {randint(0000, 9999)}", receipt_text)
    order_data.append(order_text)
    save_data_to_file()
    clear_order()


def clear_order():
    global total_price
    total_price = 0
    order_text_box.delete(0, END)
    price_label.config(text="0")
    quantity_entry.delete(0, END)
    quantity_entry.insert(END, '1')


def search_items(*args):
    search_term = search_var.get().lower()
    items_list_box.delete(0, END)
    for name, price in zip(items_name, items_price):
        if search_term in name.lower():
            items_list_box.insert(END, f"{name} - {price}")


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


# Initialize the root window
root = Tk()
root.title("POS System")
root.state("zoomed")
root.configure(bg=bg_color)
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_closing)

# Create a frame for the save item button
save_item_frame = Frame(root, bg=bg_color, width=700, height=180, padx=10, pady=10)
save_item_frame.place(x=5, y=5)

Label(save_item_frame, text="Save Item", font=("Arial", 20, 'bold'), bg=bg_color, fg=primary_color).grid(row=0,
                                                                                                         column=0,
                                                                                                         columnspan=4,
                                                                                                         pady=(0, 10))
Label(save_item_frame, text="Item Name:", font=("Arial", 12), bg=bg_color, fg=text_color).grid(row=1, column=0,
                                                                                               sticky='w')
item_name_entry = Entry(save_item_frame, font=("Arial", 12), bg="white", fg=text_color, borderwidth=0)
item_name_entry.grid(row=1, column=1, padx=10)
Label(save_item_frame, text="Item Price:", font=("Arial", 12), bg=bg_color, fg=text_color).grid(row=1, column=2,
                                                                                                sticky='w')
item_price_entry = Entry(save_item_frame, font=("Arial", 12), bg="white", fg=text_color, borderwidth=0)
item_price_entry.grid(row=1, column=3, padx=10)

save_item_button = Button(save_item_frame, text="Save Item", font=("Arial", 12), bg=accent_color, fg="white",
                          borderwidth=0,
                          command=save_item)
save_item_button.grid(row=1, column=4, columnspan=2, pady=10, padx=10)

# Create a frame for the items list
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

# Create a frame for the order preview
order_preview_frame = Frame(root, bg=bg_color, width=800, height=530, padx=10, pady=10)
order_preview_frame.place(x=0, y=150)

Label(order_preview_frame, text="Your Order:", font=("Arial", 20, 'bold'), bg=bg_color, fg=primary_color).pack(
    anchor='n', pady=(0, 10))
order_text_box = Listbox(order_preview_frame, width=72, height=18, font=("Arial", 13), bg="white", fg=primary_color,
                         borderwidth=0, justify='left', selectbackground="Light Green", selectforeground="black",
                         selectmode=SINGLE)
order_text_box.pack(pady=10)

# Main root elements
main_frame = Frame(root, bg=bg_color, padx=10, pady=10)
main_frame.place(relx=0.5, rely=0.9, anchor='center')

order_button = Button(main_frame, text="Place Order", font=("Arial", 12), bg=primary_color, fg="white", borderwidth=0,
                      width=20, height=1, command=place_order)
order_button.grid(row=0, column=0, padx=20, pady=10)
add_ordered_items_button = Button(main_frame, text="Add to Order", font=("Arial", 12), bg=primary_color, fg="white",
                                  borderwidth=0, width=20, height=1, command=add_ordered_items)
add_ordered_items_button.grid(row=0, column=1, padx=20, pady=10)

Label(main_frame, text="Quantity:", font=("Arial", 15), fg=primary_color, bg=bg_color).grid(row=1, column=0, sticky='e',
                                                                                            padx=(0, 10))
quantity_entry = Entry(main_frame, font=("Arial", 12), bg="white", fg=text_color, borderwidth=0, width=10,
                       justify='center')
quantity_entry.insert(END, '1')
quantity_entry.grid(row=1, column=1, sticky='w')

Label(main_frame, text="Total Price(PKR):", font=("Arial", 15), fg=primary_color, bg=bg_color).grid(row=2, column=0,
                                                                                                    sticky='e',
                                                                                                    padx=(0, 10))
price_label = Label(main_frame, text="0", font=("Arial", 15), fg=primary_color, bg=bg_color)
price_label.grid(row=2, column=1, sticky='w')

clear_order_button = Button(main_frame, text="Clear Order", font=("Arial", 12), bg=error_color, fg="white",
                            borderwidth=0, width=20, height=1, command=clear_order)
clear_order_button.grid(row=3, column=0, columnspan=2, pady=10)
preload()

# Run the main loop
root.mainloop()
