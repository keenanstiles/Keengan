import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")

        self.history = []

        # Conversion rates (Add more as needed)
        self.conversion_rates = {
            'Meter': 1,
            'Feet': 3.28084,
            'Inches': 39.3701,
            # Add more conversion rates here
        }

        # Variables
        self.from_unit_var = tk.StringVar(value='Meter')
        self.to_unit_var = tk.StringVar(value='Feet')
        self.input_var = tk.DoubleVar()

        # GUI elements
        self.from_unit_label = ttk.Label(root, text="From Unit:")
        self.from_unit_combobox = ttk.Combobox(root, values=list(self.conversion_rates.keys()), textvariable=self.from_unit_var)

        self.to_unit_label = ttk.Label(root, text="To Unit:")
        self.to_unit_combobox = ttk.Combobox(root, values=list(self.conversion_rates.keys()), textvariable=self.to_unit_var)

        self.input_label = ttk.Label(root, text="Enter Value:")
        self.input_entry = ttk.Entry(root, textvariable=self.input_var)

        self.convert_button = ttk.Button(root, text="Convert", command=self.convert)
        self.history_button = ttk.Button(root, text="History", command=self.show_history)
        self.help_button = ttk.Button(root, text="Help/Info", command=self.show_help)

        # Grid layout
        self.from_unit_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.from_unit_combobox.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        self.to_unit_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.to_unit_combobox.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        self.input_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.input_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        self.convert_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.history_button.grid(row=4, column=0, pady=5)
        self.help_button.grid(row=4, column=1, pady=5)

    def convert(self):
        try:
            value = self.input_var.get()
            from_unit = self.from_unit_var.get()
            to_unit = self.to_unit_var.get()

            conversion_rate = self.conversion_rates[to_unit] / self.conversion_rates[from_unit]
            result = value * conversion_rate

            conversion_str = f"{value} {from_unit} is equal to {result:.2f} {to_unit}"
            self.history.append((conversion_str, datetime.now()))

            messagebox.showinfo("Conversion Result", conversion_str)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def show_history(self):
        history_text = "\n".join([f"{item[0]} - {item[1]}" for item in self.history])
        if not history_text:
            history_text = "No history available."

        messagebox.showinfo("Conversion History", history_text)

    def show_help(self):
        help_text = "Conversion Rates:\n"
        for unit, rate in self.conversion_rates.items():
            help_text += f"{unit}: {rate:.6f}\n"

        messagebox.showinfo("Help/Info", help_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()
