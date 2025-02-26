from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Beastars fan")
# root.geometry("300x250+1200+100")

# root.resizable(False, False)
# root.minsize(0, 0)
# root.maxsize(100, 100) will be like this even if geometry tells another

icon = PhotoImage(file = "beast.png")
root.iconphoto(False, icon)

######## Creation of the iconfree window #######
# import tempfile, base64, zlib
# ICON = zlib.decompress(base64.b64decode("eJxjYGAEQgEBBiDJwZDBysAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc="))
# _, ICON_PATH = tempfile.mkstemp()
# with open(ICON_PATH, "wb") as icon_file:
#     icon_file.write(ICON)
# root.iconbitmap(default=ICON_PATH)

# label = Label(text = "I like watching Beastars!")
# label.grid()

def finish():
    root.destroy()
    print("App is closing")

root.protocol("WM_DELETE_WINDOW", finish)

#root.attributes("-transparentcolor", "white") make inreal to touch
root.attributes("-topmost", True) #true-keeps always on top false-allows other to overlay it

#clicks = 0

# def click_counter():
#     global clicks
#     clicks += 1
#     btn["text"] = f"Clicks {clicks}" 

#btn = ttk.Button(text = "Click to say you like it too", command = click_counter)
#btn.pack(expand = True, anchor= E, fill = BOTH, padx = [30,60], pady = 30)

#btn2 = ttk.Button(text = "I do not like this anime", state = ["disabled"])
# btn2.pack(anchor="w", fill = X, padx = 20, pady = 30, ipadx = 10, ipady = 40)
#btn2.place(relx=0.5, rely=0.5, anchor = CENTER,  relwidth=0.66, relheight=0.25)

root.rowconfigure(0, weight = 3)
for column in range(4): root.columnconfigure(index = column, weight=1)

for r in range(6):
    for c in range(4):
        btn3 = ttk.Button(text=f"({r},{c})")
        btn3.grid(row=r, column=c, ipadx=6, ipady=6, padx = [15, 4], pady=4)

root.mainloop()