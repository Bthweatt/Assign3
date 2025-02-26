# Program Name: Assignment3.py (use the name the program is saved as)
# Course: IT3883/Section XXX
# Student Name: Brandon Thweatt
# Assignment Number: Lab3
# Due Date: 02/25/ 2025
# Purpose: What does the program do (in a few sentences)?
# The goal of this program is to provide a simple user interface that will convert MPG to KMPL,
# all while being dynamically represented on the output. The application should not crash during invalid input.
# List Specific resources used to complete the assignment.
# Pycharm enterprise edition

import tkinter as tk
from tkinter import StringVar

# Function that performs the conversion
def convert_mpg_to_kmpl(*args):
    try:
        mpg_value = float(mpg_var.get())
        kmpl_value = mpg_value * 0.425143707
        kmpl_var.set(f"{kmpl_value:.4f}")  # Display result with 4 decimal places
    except ValueError:
        kmpl_var.set("Invalid Input")  # Handle non-numeric input

# Create tkinter window
root = tk.Tk()
root.title("MPG to KM/L Converter")
root.geometry("300x150")

# String variables for the user input and output
mpg_var = StringVar()
kmpl_var = StringVar()

# Attach event listener to update conversion as user types
mpg_var.trace_add("write", convert_mpg_to_kmpl)

# GUI Layout lable for input
tk.Label(root, text="Miles per Gallon (MPG):").pack(pady=5)
mpg_entry = tk.Entry(root, textvariable=mpg_var)
mpg_entry.pack(pady=5)

# GUI Layout lable for output
tk.Label(root, text="Kilometers per Liter (KM/L):").pack(pady=5)
kmpl_label = tk.Label(root, textvariable=kmpl_var, font=("Arial", 12, "bold"))
kmpl_label.pack(pady=5)

# Init application
root.mainloop()
