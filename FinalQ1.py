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
Would you like me to create and send you the .py file for download?



You said:
change for nfl team wins

ChatGPT said:
Got it! Let's adapt the GUI program to work with NFL team wins instead of just a generic number input.

✅ Implemented Features (Same 5, just in a new context):
Input validated as a float number (e.g., handles "Ten" without crashing)

Display a value rounded to 3 decimal places

If-elif-else logic to interpret win totals

GUI with user input and button

Write result to .txt file

📋 Program Description:
The user enters the number of wins an NFL team has. The program:

Validates the input as a number.

Rounds it to 3 decimal places.

Displays whether it's a losing season (<9 wins), average season (exactly 9), or winning season (>9).

Saves the result to a file.

Shows results in a message box.

📁 LastNameFirstName_FinalQ2.py
python
Copy
Edit
# Pseudocode: Import required modules for GUI and file operations
import tkinter as tk
from tkinter import messagebox

# Pseudocode: Define a function to process NFL win input
def evaluate_wins():
    # Pseudocode: Get text from input field
    user_input = entry.get()

    try:
        # Pseudocode: Try converting input to float
        wins = float(user_input)

        # Pseudocode: Round to 3 decimal places
        wins_rounded = round(wins, 3)

        # Pseudocode: Determine season quality using if-elif-else
        if wins_rounded < 9:
            message = f"{wins_rounded} wins - Losing season."
        elif wins_rounded == 9:
            message = f"{wins_rounded} wins - Average season."
        else:
            message = f"{wins_rounded} wins - Winning season!"

        # Pseudocode: Write result to output file
        with open("nfl_wins_output.txt", "w") as file:
            file.write(message)

        # Pseudocode: Show result to user
        messagebox.showinfo("Season Evaluation", message)

    except ValueError:
        # Pseudocode: Show error if input is invalid
        messagebox.showerror("Input Error", "Please enter a valid number of wins.")

# Pseudocode: Create the main window
window = tk.Tk()
window.title("NFL Team Win Evaluator")
window.geometry("350x150")

# Pseudocode: Add label for user prompt
label = tk.Label(window, text="Enter number of wins for the NFL team:")
label.pack(pady=5)

# Pseudocode: Add entry field for win input
entry = tk.Entry(window)
entry.pack(pady=5)

# Pseudocode: Add button to submit input
button = tk.Button(window, text="Evaluate", command=evaluate_wins)
button.pack(pady=10)

# Pseudocode: Run the GUI loop
window.mainloop()
