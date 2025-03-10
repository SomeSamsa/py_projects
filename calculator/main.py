from tkinter import *
from tkinter import ttk 

calc = Tk()
calc.title("Calculator")
calc.iconbitmap(default="calculator.ico")
calc.geometry("300x350+1200+100")
calc.resizable(False,False)
calc.attributes("-topmost", True)

future = ttk.Button(text = "will be future entry")
future.grid(row = 0, column = 0, columnspan=4)

def clicked_button(i):
    if i == 1:
        future["text"] = f"{i}st button clicked"
    if i == 2:
        future["text"] = f"{i}nd button clicked"
    if i == 3:
        future["text"] = f"{i}rd button clicked"
    else: 
        future["text"] = f"{i}th button clicked"

number = 0

for r in range(1, 7):
    for c in range(4):
        number += 1
        btn = ttk.Button(text=f"{number}", command = lambda i = number: clicked_button(i))
        btn.grid(row=r, column=c) 


calc.mainloop()