import tkinter as tk
from tkinter import filedialog
import pandas as pd
import statistics as stats
from tkinter import messagebox


class StatisticalCalculator(tk.Tk):
    # Main class for the application
    def __init__(self):
        super().__init__()
        self.geometry("610x350")  # Set the window size
        self.title("Statistical Calculator")  # Set the window title
        self.configure(bg="White")  # Set the background color

        self.data = None  # To store loaded data

        # Label to show results
        self.results_label = tk.Label(self, text="", font=("Arial", 15), bg="White", fg="green", wraplength=600)
        self.results_label.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

        self.create_widgets()  # Create the widgets

    def create_widgets(self):
        # Button to upload a file
        upload_button = tk.Button(self, text="Upload File", command=self.load_file, bg='Light Blue', fg="Black",
                                  borderwidth=0, font=("Arial", 15))
        upload_button.grid(row=1, column=1, pady=30, padx=10)

        # ===============Buttons for statistical calculations================
        # Button to calculate mean
        calculate_mean_button = tk.Button(self, text="Calculate Mean", command=self.calculate_mean, bg='Light Blue',
                                          fg="Black", borderwidth=0, font=("Arial", 15))
        calculate_mean_button.grid(row=2, column=0, pady=10, padx=10)

        # Button to calculate mode
        calculate_mode_button = tk.Button(self, text="Calculate Mode", command=self.calculate_mode, bg='Light Blue',
                                          fg="Black", borderwidth=0, font=("Arial", 15))
        calculate_mode_button.grid(row=2, column=1, pady=10, padx=10)

        # Button to calculate median
        calculate_median_button = tk.Button(self, text="Calculate Median", command=self.calculate_median,
                                            bg='Light Blue', fg="Black", borderwidth=0, font=("Arial", 15))
        calculate_median_button.grid(row=2, column=2, pady=10, padx=10)

        # Button to calculate range
        calculate_range_button = tk.Button(self, text="Calculate Range", command=self.calculate_range, bg='Light Blue',
                                           fg="Black", borderwidth=0, font=("Arial", 15))
        calculate_range_button.grid(row=3, column=0, pady=10, padx=10)

        # Button to calculate variance
        calculate_variance_button = tk.Button(self, text="Calculate Variance", command=self.calculate_variance,
                                              bg='Light Blue', fg="Black", borderwidth=0, font=("Arial", 15))
        calculate_variance_button.grid(row=3, column=1, pady=10, padx=10)

        # Button to calculate standard deviation
        calculate_stddev_button = tk.Button(self, text="Calculate Std Deviation", command=self.calculate_stddev,
                                            bg='Light Blue', fg="Black", borderwidth=0, font=("Arial", 15))
        calculate_stddev_button.grid(row=3, column=2, pady=10, padx=10)

        # Button to calculate quartiles
        calculate_quartiles_button = tk.Button(self, text="Calculate Quartiles", command=self.calculate_quartiles,
                                               bg='Light Blue', fg="Black", borderwidth=0, font=("Arial", 15))
        calculate_quartiles_button.grid(row=4, column=1, pady=10, padx=10)

    def load_file(self):  # Function to load a file
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])  # Open file dialog
        if file_path:  # If a file is selected then perform the further operations
            try:
                self.data = pd.read_csv(file_path)['values']  # Read data from 'values' column
                self.results_label['text'] = "File Loaded"  # Indicate that the file is loaded
            except Exception as e:
                messagebox.showerror("Error", f"Error loading file: {e}")  # Show error message if any error occurs

    def calculate_mean(self):  # Function to calculate mean
        if self.data is not None:  # Check if data exists
            mean = self.data.mean()  # Calculate mean
            self.results_label['text'] = f"Mean: {mean}"  # Display the mean
        else:
            messagebox.showerror("Error", "Please load a correct file.")

    def calculate_mode(self):  # Function to calculate mode
        if self.data is not None:  # Check if data exists
            mode = stats.mode(self.data)  # Calculate mode
            self.results_label['text'] = f"Mode: {mode}"  # Display the mode
        else:
            messagebox.showerror("Error", "Please load a correct file.")

    def calculate_median(self):  # Function to calculate median
        if self.data is not None:  # Check if data exists
            median = stats.median(self.data)  # Calculate median
            self.results_label['text'] = f"Median: {median}"  # Display the median
        else:
            messagebox.showerror("Error", "Please load a correct file.")

    def calculate_range(self):  # Function to calculate range
        if self.data is not None:  # Check if data exists
            data_range = max(self.data) - min(self.data)  # Calculate range
            self.results_label['text'] = f"Range: {data_range}"  # Display the range
        else:
            messagebox.showerror("Error", "Please load a correct file.")

    def calculate_variance(self):  # Function to calculate variance
        if self.data is not None:  # Check if data exists
            variance1 = stats.variance(self.data)  # Calculate variance
            self.results_label['text'] = f"Variance: {variance1}"  # Display the variance
        else:
            messagebox.showerror("Error", "Please load a correct file.")

    def calculate_stddev(self):  # Function to calculate standard deviation
        if self.data is not None:  # Check if data exists
            stddev = stats.stdev(self.data)  # Calculate standard deviation

            # Display the standard deviation to the nearest 2 decimal places
            self.results_label['text'] = f"Standard Deviation: {round(stddev, 2)}"
        else:
            messagebox.showerror("Error", "Please load a correct file.")

    def calculate_quartiles(self):  # Function to calculate quartiles
        if self.data is not None:  # Check if data exists

            # Calculate the quartiles
            q1 = stats.quantiles(self.data, n=4)[0]
            q2 = stats.median(self.data)
            q3 = stats.quantiles(self.data, n=4)[-1]

            # Display the quartiles
            self.results_label[
                'text'] = f"Q1->{q1:.1f},\tQ2->{q2:.1f},\tQ3->{q3:.1f}"
        else:
            messagebox.showerror("Error", "Please load a correct file.")


# Run the application
if __name__ == "__main__":
    app = StatisticalCalculator()
    app.mainloop()  # Start the main loop to keep the GUI running
