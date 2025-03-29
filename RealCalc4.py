import tkinter as t
from tkinter import messagebox
import math

def btn_clk(txt):
    curr = exp.get()
    if txt == "√":
        exp.set(curr + "√")  # Display √ but internally convert to math.sqrt()
    else:
        exp.set(curr + txt)

def clr():
    exp.set("")

def calc():
    try:
        expression = exp.get().replace("^", "**").replace("√", "math.sqrt")
        res = eval(expression)
        exp.set(res)
    except Exception as e:
        messagebox.showerror("Err", "Invalid Exp")
        exp.set("")

# Create main window
rt = t.Tk()
rt.title("Calc")
rt.geometry("250x350")
rt.resizable(False, False)

# Entry field for numbers and expressions
exp = t.StringVar()
inp = t.Entry(rt, textvariable=exp, font=("Arial", 16), justify='right', bd=6, relief=t.GROOVE)
inp.grid(row=0, column=0, columnspan=4, ipadx=4, ipady=4)

# Button layout
btns = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+'),
    ('^', '√', '(', ')')  # Added brackets
]

for r_idx, row in enumerate(btns, start=1):
    for c_idx, txt in enumerate(row):
        if txt == "C":
            btn = t.Button(rt, text=txt, font=("Arial", 12), command=clr, width=4, height=2)
        elif txt == "=":
            btn = t.Button(rt, text=txt, font=("Arial", 12), command=calc, width=4, height=2)
        else:
            btn = t.Button(rt, text=txt, font=("Arial", 12), command=lambda b=txt: btn_clk(b), width=4, height=2)
        btn.grid(row=r_idx, column=c_idx, padx=3, pady=3)

# Run the application
rt.mainloop()