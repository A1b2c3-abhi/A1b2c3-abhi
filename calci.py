import tkinter as tk
from tkinter import messagebox

# Function to update expression in the text entry
def press(key):
    current = equation.get()
    equation.set(current + str(key))

# Function to calculate the result and display it
def evaluate():
    try:
        result = str(eval(equation.get()))
        equation.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        equation.set("")

# Function to clear the input
def clear():
    equation.set("")

# Set up the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.resizable(False, False)

# Set up the equation entry box
equation = tk.StringVar()
entry_box = tk.Entry(root, textvariable=equation, font=('Arial', 24), bd=10, insertwidth=4, width=14, borderwidth=4)
entry_box.grid(row=0, column=0, columnspan=4)

# Button configuration
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Add buttons to the calculator
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=30, pady=20, font=('Arial', 18), command=evaluate)
    else:
        button = tk.Button(root, text=text, padx=30, pady=20, font=('Arial', 18), command=lambda t=text: press(t))
    button.grid(row=row, column=col)

# Add Clear button
clear_button = tk.Button(root, text="C", padx=30, pady=20, font=('Arial', 18), command=clear)
clear_button.grid(row=5, column=0, columnspan=4)

# Run the application
root.mainloop()
