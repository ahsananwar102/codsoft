import tkinter as tk

# Defining expression as a global variable
expression = "" 

def button_click(btn): # Function to display and evaluate the expression
    global expression
    button_text = btn.cget("text")
    if button_text == "=":
        try:
            result = eval(expression)
            result = str(round(result, 6))
            textbox.config(text=result)
            expression = ""
        except ZeroDivisionError:
            textbox.config(text="Error: Division by zero")
            expression = ""
        except SyntaxError:
            textbox.config(text="Error: Invalid Syntax")
            expression = ""
    elif button_text == "C":
        expression = ""
        textbox.config(text="")
    elif button_text == "<--":
        expression = expression[:-1]
        textbox.config(text=expression)
    else:
        expression = expression + button_text
        textbox.config(text=expression)

root = tk.Tk()
root.title("Calculator")
root.geometry("375x450")
root.resizable(width=False, height=False)

frame1 = tk.Frame(root) # Frame for the expression textbox
frame1.pack(expand=True, fill="both")

# Textbox for displaying the expression
textbox = tk.Label(frame1, height=1, font=("Courier 20 bold"), text="")
textbox.pack(expand=True, fill="both", pady=10)

# Separator
separator = tk.Frame(root, bd=10, relief='sunken', height=4)
separator.pack(side='top', fill='x', padx=20, pady=(0, 30))

# Frame for all the buttons
frame2 = tk.Frame(root)
frame2.pack(expand=True, fill="both")

# Button definitions
button_back = tk.Button(frame2, text="<--", font=("Verdana 15"), command=lambda: button_click(button_back))
button_back.grid(row=0, column=0, sticky="nsew", columnspan=2)

button_c = tk.Button(frame2, text="C", font=("Verdana 15"), command=lambda: button_click(button_c))
button_c.grid(row=0, column=2, sticky="nsew", columnspan=2)

button1 = tk.Button(frame2, text="1", font=("Verdana 15"), command=lambda: button_click(button1))
button1.grid(row=1, column=0, sticky="nsew")

button2 = tk.Button(frame2, text="2", font=("Verdana 15"), command=lambda: button_click(button2))
button2.grid(row=1, column=1, sticky="nsew")

button3 = tk.Button(frame2, text="3", font=("Verdana 15"), command=lambda: button_click(button3))
button3.grid(row=1, column=2, sticky="nsew")

button_plus = tk.Button(frame2, text="+", font=("Verdana 15"), command=lambda: button_click(button_plus))
button_plus.grid(row=1, column=3, sticky="nsew")

button4 = tk.Button(frame2, text="4", font=("Verdana 15"), command=lambda: button_click(button4))
button4.grid(row=2, column=0, sticky="nsew")

button5 = tk.Button(frame2, text="5", font=("Verdana 15"), command=lambda: button_click(button5))
button5.grid(row=2, column=1, sticky="nsew")

button6 = tk.Button(frame2, text="6", font=("Verdana 15"), command=lambda: button_click(button6))
button6.grid(row=2, column=2, sticky="nsew")

button_minus = tk.Button(frame2, text="-", font=("Verdana 15"), command=lambda: button_click(button_minus))
button_minus.grid(row=2, column=3, sticky="nsew")

button7 = tk.Button(frame2, text="7", font=("Verdana 15"), command=lambda: button_click(button7))
button7.grid(row=3, column=0, sticky="nsew")

button8 = tk.Button(frame2, text="8", font=("Verdana 15"), command=lambda: button_click(button8))
button8.grid(row=3, column=1, sticky="nsew")

button9 = tk.Button(frame2, text="9", font=("Verdana 15"), command=lambda: button_click(button9))
button9.grid(row=3, column=2, sticky="nsew")

button_mul = tk.Button(frame2, text="*", font=("Verdana 15"), command=lambda: button_click(button_mul))
button_mul.grid(row=3, column=3, sticky="nsew")

button0 = tk.Button(frame2, text="0", font=("Verdana 15"), command=lambda: button_click(button0))
button0.grid(row=4, column=0, sticky="nsew")

button_point = tk.Button(frame2, text=".", font=("Verdana 15"), command=lambda: button_click(button_point))
button_point.grid(row=4, column=1, sticky="nsew")

button_equals = tk.Button(frame2, text="=", font=("Verdana 15"), command=lambda: button_click(button_equals))
button_equals.grid(row=4, column=2, sticky="nsew")

button_div = tk.Button(frame2, text="/", font=("Verdana 15"), command=lambda: button_click(button_div))
button_div.grid(row=4, column=3, sticky="nsew")

for i in range(5):
    frame2.grid_rowconfigure(i, weight=1)
for j in range(4):
    frame2.grid_columnconfigure(j, weight=1)

root.mainloop()