import tkinter as tk
from tkinter import messagebox

def add():
    try:
        numbers = list(map(int, entry.get().split()))
        result.set(f"Result: {sum(numbers)}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers separated by spaces")

def subtract():
    try:
        numbers = list(map(int, entry.get().split()))
        res = numbers[0] - sum(numbers[1:]) if len(numbers) > 1 else numbers[0]
        result.set(f"Result: {res}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers separated by spaces")

def multiply():
    try:
        numbers = list(map(int, entry.get().split()))
        res = 1
        for num in numbers:
            res *= num
        result.set(f"Result: {res}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers separated by spaces")

def divide():
    try:
        num1, num2 = map(float, entry.get().split())
        if num2 == 0:
            messagebox.showerror("Math Error", "Cannot divide by zero")
        else:
            result.set(f"Result: {num1 / num2}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter exactly two valid numbers")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x250")

# Create and place widgets
label = tk.Label(root, text="Enter numbers (space-separated):")
label.pack()
entry = tk.Entry(root, width=50)
entry.pack()

add_button = tk.Button(root, text="Addition", command=add)
add_button.pack()

subtract_button = tk.Button(root, text="Subtraction", command=subtract)
subtract_button.pack()

multiply_button = tk.Button(root, text="Multiplication", command=multiply)
multiply_button.pack()

divide_button = tk.Button(root, text="Division (only 2 numbers)", command=divide)
divide_button.pack()

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

# Run the application
root.mainloop()
