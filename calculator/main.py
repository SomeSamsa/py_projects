from tkinter import *
from tkinter import ttk 

calc = Tk()
calc.title("Calculator")
calc.iconbitmap(default="calculator.ico")
calc.geometry("300x350+1200+100")
#calc.resizable(False,False)
calc.attributes("-topmost", True)

future = ttk.Button(text = "will be future entry")
future.grid(row = 0, column = 0, columnspan=4)

for r in range(1, 7):
    for c in range(4):
        btn3 = ttk.Button(text=f"({r},{c+1})")
        btn3.grid(row=r, column=c) 


calc.mainloop()