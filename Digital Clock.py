from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title("Digital Clock ")
lbl = Label(root, font="Times 30 bold ", background = "#000000", foreground = "#45CCC3")
lbl.pack(anchor= "center")
def time():
    string= strftime(" %H:%M:%S %p ")
    lbl.config(text=string)
    lbl. after(1000, time)
time()
root.mainloop()