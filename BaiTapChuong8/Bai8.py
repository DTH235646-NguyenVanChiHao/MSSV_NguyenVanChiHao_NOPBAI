from tkinter import *

root = Tk()

stringF = StringVar()
stringC = StringVar()

def Chuyen():
    f = int(stringF.get())
    c = (f - 32)/1.8
    stringC.set(str(c))

root.minsize(height =150, width = 330)
root.configure(bg="yellow")

Label(root, text="Nhập độ F:", bg="yellow").grid(row = 0, column=0)
Entry(root, width=15, textvariable=stringF, fg="red").grid(row = 0, column = 1)

aButton = Frame(root)
Button(root, text = "Chuyển", command = Chuyen, width = 4).grid(row = 1, column = 1)

Label(root, text="Độ C:", bg="yellow").grid(row = 2, column=0)
Entry(root, width=15, textvariable=stringC, bg="yellow").grid(row = 2, column = 1)

root.mainloop()