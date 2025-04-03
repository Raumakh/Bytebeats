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

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x200")

# Create and place widgets
label = tk.Label(root, text="Enter numbers (space-separated):")
label.pack()
entry = tk.Entry(root, width=50)
entry.pack()

add_button = tk.Button(root, text="Addition", command=add)
add_button.pack()

subtract_button = tk.Button(root, text="Subtraction", command=subtract)
subtract_button.pack()

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

# Run the application
root.mainloop()
