from tkinter import *
from tkinter import ttk 

calc = Tk()
calc.title("Calculator")
calc.iconbitmap(default="calculator.ico")
calc.geometry("300x350+1200+100")
calc.resizable(False,False)
calc.attributes("-topmost", True)


calc.mainloop()