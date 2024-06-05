# Imports
from tkinter import *
from tkinter import messagebox

# Global Variables
bg_color = "#f0f0f0"
primary_color = "#004d40"
accent_color = "#00bfa5"
text_color = "#333333"
error_color = "#ff5252"


# Functions
def calculate():
    if fuel_price.get() == "" or total_distance.get() == "" or vehicle_fuel_avg.get() == "":
        messagebox.showerror("Error", "Please fill all the fields")
        return
    try:
        fuel_price_value = float(fuel_price.get())
        total_distance_value = float(total_distance.get())
        vehicle_fuel_avg_value = float(vehicle_fuel_avg.get())
        if fuel_price_value < 1 or total_distance_value < 1 or vehicle_fuel_avg_value < 1:
            raise ValueError
        fuel_cost_value = (total_distance_value / vehicle_fuel_avg_value) * fuel_price_value
        fuel_cost.config(text=str(round(fuel_cost_value, 2)))
    except ValueError:
        messagebox.showerror("Error", "Invalid Input")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Vehicle fuel Average can't be 0")


# Main Window
root = Tk()
root.title("Fuel Cost Calculator")
root.geometry("350x300")
root.resizable(False, False)
root.configure(bg=bg_color)

Label(root, text="Fuel Price for 1 litre(PKR):", font=("Arial", 13), bg=bg_color, fg=primary_color).grid(row=0,
                                                                                                         column=0,
                                                                                                         padx=10,
                                                                                                         pady=10)
fuel_price = Entry(root, font=("Arial", 10), bg="white", fg=text_color, relief=FLAT, width=13, justify="center",
                   highlightbackground="light green", highlightcolor='Light green', highlightthickness=1)
fuel_price.grid(row=0, column=1, pady=10)

Label(root, text="Total Distance(Km):", font=("Arial", 13), bg=bg_color, fg=primary_color).grid(row=1, column=0,
                                                                                                padx=10,
                                                                                                pady=10)
total_distance = Entry(root, font=("Arial", 10), bg="white", fg=text_color, relief=FLAT, width=13, justify="center",
                       highlightbackground="light green", highlightcolor='Light green', highlightthickness=1)
total_distance.grid(row=1, column=1, pady=10)

Label(root, text="Vehicle fuel Average(Km/L):", font=("Arial", 13), bg=bg_color, fg=primary_color).grid(row=2, column=0,
                                                                                                        padx=10,
                                                                                                        pady=10)
vehicle_fuel_avg = Entry(root, font=("Arial", 10), bg="white", fg=text_color, relief=FLAT, width=13, justify="center",
                         highlightbackground="light green", highlightcolor='Light green', highlightthickness=1)
vehicle_fuel_avg.grid(row=2, column=1, pady=10)

Label(root, text="Fuel Cost PKR.", font=("Arial", 13, 'underline'), bg=bg_color, fg=primary_color).grid(row=3, column=0,
                                                                                                        pady=30)
fuel_cost = Label(root, text="0", font=("Arial", 13), bg=bg_color, fg=primary_color)
fuel_cost.grid(row=3, column=1, pady=30)

calculate_button = Button(root, text="Calculate", font=("Arial", 13), bg=accent_color, fg="white", relief=FLAT,
                          command=calculate, borderwidth=0, highlightthickness=1)
calculate_button.grid(row=4, column=0, columnspan=2)

root.mainloop()
