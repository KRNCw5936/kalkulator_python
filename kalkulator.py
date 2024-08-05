import tkinter as tk
from math import *

# Function to evaluate the expression
def evaluate(event=None):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry widget
def clear():
    entry.delete(0, tk.END)

# Function to clear the last entry (CE)
def clear_entry():
    current_text = entry.get()
    if current_text:
        entry.delete(len(current_text) - 1, tk.END)

# Function to append text to the entry widget
def append_text(text):
    entry.insert(tk.END, text)

# Function to append mathematical functions
def append_function(func):
    entry.insert(tk.END, func + '(')

# Function to handle inverse functions
def append_inverse(func):
    if func == 'sin':
        append_text('asin(')
    elif func == 'cos':
        append_text('acos(')
    elif func == 'tan':
        append_text('atan(')
    elif func == 'sinh':
        append_text('asinh(')
    elif func == 'cosh':
        append_text('acosh(')
    elif func == 'tanh':
        append_text('atanh(')

# Creating the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Creating the entry widget
entry = tk.Entry(root, width=40, borderwidth=5, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=6)

# Binding the enter key to the evaluate function
root.bind('<Return>', evaluate)

# Button layout
buttons = [
    '7', '8', '9', '/', 'π', 'cos',
    '4', '5', '6', '*', '2π', 'cosh',
    '1', '2', '3', '-', 'log', 'tanh',
    '0', '.', '=', '+', 'Inv', 'sinh',
    'C', 'CE', '√', '%', 'Mod', 'e',
    '(', ')', 'log2', 'log10', 'deg', 'expm1',
    '±', 'log1p', 'lgamma'
]

# Functions corresponding to each button
functions = {
    'π': 'pi', '2π': '2*pi', '√': 'sqrt', 'cos': 'cos', 'cosh': 'cosh',
    'sin': 'sin', 'sinh': 'sinh', 'tan': 'tan', 'tanh': 'tanh',
    'log': 'log', 'log2': 'log2', 'log10': 'log10', 'log1p': 'log1p',
    'expm1': 'expm1', 'lgamma': 'lgamma', 'deg': 'degrees',
    'Mod': '%', 'e': 'e', 'Inv': 'Inv'
}

row = 1
col = 0

# Creating the buttons and placing them in the grid
for button in buttons:
    if button in functions:
        if button == 'Inv':
            tk.Button(root, text=button, width=5, height=2, font=('Arial', 14),
                      command=lambda b=button: append_inverse(functions[b])).grid(row=row, column=col, sticky="nsew")
        else:
            tk.Button(root, text=button, width=5, height=2, font=('Arial', 14),
                      command=lambda b=button: append_function(functions[b])).grid(row=row, column=col, sticky="nsew")
    elif button == 'C':
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 14), command=clear, bg="lightblue").grid(row=row, column=col, sticky="nsew")
    elif button == 'CE':
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 14), command=clear_entry, bg="lightblue").grid(row=row, column=col, sticky="nsew")
    elif button == '=':
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 14), command=evaluate, bg="lightblue").grid(row=row, column=col, sticky="nsew")
    elif button in ['+', '-', '*', '/']:
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 14), command=lambda b=button: append_text(b), bg="lightblue").grid(row=row, column=col, sticky="nsew")
    elif button.isdigit() or button == '.':
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 14), command=lambda b=button: append_text(b), bg="orange").grid(row=row, column=col, sticky="nsew")
    elif button == '±':
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 14), command=lambda: append_text('(-1)*'), bg="lightblue").grid(row=row, column=col, sticky="nsew")
    else:
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 14), command=lambda b=button: append_text(b), bg="lightgray").grid(row=row, column=col, sticky="nsew")

    col += 1
    if col == 6:
        col = 0
        row += 1

# Set column and row weights to make buttons expandable
for i in range(6):
    root.grid_columnconfigure(i, weight=1)
for i in range(row + 1):
    root.grid_rowconfigure(i, weight=1)

# Running the main loop
root.mainloop()