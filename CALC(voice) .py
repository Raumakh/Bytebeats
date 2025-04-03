import tkinter as t
from tkinter import messagebox
import math
import speech_recognition as sr

def btn_clk(txt):
    curr = exp.get()
    if txt == "\u221a":
        exp.set(curr + "\u221a")  # Display √ but internally convert to math.sqrt()
    else:
        exp.set(curr + txt)

def clr():
    exp.set("")

def backspace():
    if exp.get():
        exp.set(exp.get()[:-1])

def calc():
    try:
        expression = exp.get().replace("^", "**")
        
        while "\u221a" in expression:
            idx = expression.index("\u221a")
            after_sqrt = ""
            i = idx + 1
            if i < len(expression) and expression[i] == "(":
                open_brackets = 1
                after_sqrt += "("
                i += 1
                while i < len(expression) and open_brackets > 0:
                    after_sqrt += expression[i]
                    if expression[i] == "(":
                        open_brackets += 1
                    elif expression[i] == ")":
                        open_brackets -= 1
                    i += 1
            else:
                while i < len(expression) and (expression[i].isdigit() or expression[i] == "."):
                    after_sqrt += expression[i]
                    i += 1
            
            if after_sqrt:
                expression = expression.replace("\u221a" + after_sqrt, f"math.sqrt({after_sqrt})", 1)
        
        res = eval(expression)
        exp.set(res)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")
        exp.set("")

def voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            messagebox.showinfo("Voice Input", "Speak now...")
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            command = command.replace("plus", "+").replace("minus", "-").replace("times", "*").replace("into", "*").replace("divided by", "/").replace("power", "^")
            exp.set(command)
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Could not understand audio")
        except sr.RequestError:
            messagebox.showerror("Error", "Speech recognition service unavailable")

# Create main window
rt = t.Tk()
rt.title("Calculator")
rt.geometry("250x500")
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
    ('^', '\u221a', '(', ')')
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

# Backspace button
backspace_btn = t.Button(rt, text="\u232b", font=("Arial", 12), command=backspace, width=10, height=2)
backspace_btn.grid(row=len(btns) + 1, column=0, columnspan=2, padx=3, pady=3)

# Voice command button
voice_btn = t.Button(rt, text="🎙 Voice", font=("Arial", 12), command=voice_command, width=10, height=2)
voice_btn.grid(row=len(btns) + 1, column=2, columnspan=2, padx=3, pady=3)

# Run the application
rt.mainloop()