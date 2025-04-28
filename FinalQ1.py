#!/usr/bin/env python3

TAX = 0.06

def sales_tax(t)
    sales_tax = total * tax
    return total

def main():
    print("Sales Tax Calculator\n")
    Total = input("Enter total: ")
    total_after_tax = round(total + sales_tax(total), 2)
    print("Total after tax: ", total_aftertax)
    
if _name_ == "__main__":
    MAIN()




# Pseudocode: Import required modules for GUI and file operations
import tkinter as tk
from tkinter import messagebox

# Pseudocode: Define a function to handle user input and perform actions
def process_input():
    # Pseudocode: Get text from input field
    user_input = entry.get()

    try:
        # Pseudocode: Try to convert input to float
        float_number = float(user_input)

        # Pseudocode: Round number to 3 decimal places
        rounded = round(float_number, 3)

        # Pseudocode: Use if-elif-else to describe number
        if rounded < 0:
            message = f"Rounded: {rounded}\nThe number is negative."
        elif rounded == 0:
            message = f"Rounded: {rounded}\nThe number is zero."
        else:
            message = f"Rounded: {rounded}\nThe number is positive."

        # Pseudocode: Write the result to a text file
        with open("output.txt", "w") as file:
            file.write(message)

        # Pseudocode: Show result in a messagebox
        messagebox.showinfo("Result", message)

    except ValueError:
        # Pseudocode: Show error message if input is not a float
        messagebox.showerror("Error", "Please enter a valid number.")

# Pseudocode: Set up the main GUI window
window = tk.Tk()
window.title("Number Analyzer")
window.geometry("300x150")

# Pseudocode: Add a label prompting for input
label = tk.Label(window, text="Enter a number:")
label.pack(pady=5)

# Pseudocode: Add an entry field for user input
entry = tk.Entry(window)
entry.pack(pady=5)

# Pseudocode: Add a button to trigger processing
button = tk.Button(window, text="Submit", command=process_input)
button.pack(pady=10)

# Pseudocode: Start the GUI event loop
window.mainloop()
