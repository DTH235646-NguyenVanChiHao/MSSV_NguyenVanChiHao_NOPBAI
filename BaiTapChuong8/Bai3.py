from tkinter import *

root = Tk()

stringA = StringVar()
stringB = StringVar()
stringKQ = StringVar()

root.title("PTB2")
root.minsize(height =150, width = 300)

def congAction():
    a = float(stringA.get())
    b = float(stringB.get())
    stringKQ.set(a + b)

def truAction():
    a = float(stringA.get())
    b = float(stringB.get())
    stringKQ.set(a - b)
    pass
def nhanAction():
    a = float(stringA.get())
    b = float(stringB.get())
    stringKQ.set(a * b)
    pass
def chiaAction():
    a = float(stringA.get())
    b = float(stringB.get())
    stringKQ.set(a / b)

Label(root, text="Cộng Trừ Nhân Chia", fg="blue", font=("tahoma", 16)).grid(row = 0, columnspan = 3)

frameButton = Frame(root)
Button(frameButton, text="Cộng", command=congAction).pack(side = TOP, fill= X)
Button(frameButton, text="Tru", command=truAction).pack(side = TOP, fill= X)
Button(frameButton, text="Nhân", command=nhanAction).pack(side = TOP, fill= X)
Button(frameButton, text="Chia", command=chiaAction).pack(side = TOP, fill= X)
frameButton.grid(row = 1, column = 0, rowspan = 4)

Label(root, text="Số a: ").grid(row = 1, column = 2)
Entry(root, width=15, textvariable=stringA).grid(row = 1, column = 3)
Label(root, text="Số b: ").grid(row = 2, column = 2)
Entry(root, width=15, textvariable=stringB).grid(row = 2, column = 3)
Label(root, text="Số c: ").grid(row = 3, column = 2)
Entry(root, width=15, textvariable=stringKQ).grid(row = 3, column = 3)

Button(root , text="Thoát", command = root.quit()).grid(row = 4, column = 2)

root.mainloop()
