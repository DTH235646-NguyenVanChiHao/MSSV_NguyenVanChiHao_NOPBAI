from tkinter import *
import re

root = Tk()

stringN = StringVar()
stringKQ = StringVar()

root.title("PTB4")
root.minsize(height =250, width = 220)

kq = 0
s = ""

def So1():
    s = stringN.get()
    d = s + "1"
    stringN.set(d)

def So2():
    s = stringN.get()
    d = s + "2"
    stringN.set(d)

def So3():
    s = stringN.get()
    d = s + "3"
    stringN.set(d)

def So4():
    s = stringN.get()
    d = s + "4"
    stringN.set(d)

def So5():
    s = stringN.get()
    d = s + "5"
    stringN.set(d)

def So6():
    s = stringN.get()
    d = s + "6"
    stringN.set(d)

def So7():
    s = stringN.get()
    d = s + "7"
    stringN.set(d)

def So8():
    s = stringN.get()
    d = s + "8"
    stringN.set(d)

def So9():
    s = stringN.get()
    d = s + "9"
    stringN.set(d)

def So0():
    s = stringN.get()
    d = s + "0"
    stringN.set(d)

def Cham():
    s = stringN.get()
    d = s + "."
    stringN.set(d)

def Cong():
    s = stringN.get()
    d = s + "+"
    stringN.set(d)

def Tru():
    s = stringN.get()
    d = s + "-"
    stringN.set(d)

def Nhan():
    s = stringN.get()
    d = s + "*"
    stringN.set(d)

def Chia():
    s = stringN.get()
    d = s + "/"
    stringN.set(d)

def TinhNhan(a,b):
    n = a * b
    return n

def TinhChia(a,b):
    n = a / b
    return n

def TinhTong(a,b):
    n = a + b
    return n

def TinhHieu(a,b):
    n = a - b
    return n

def Bang():
    s = stringN.get()
    d = re.findall(r'\d+', s) #số
    e = re.findall(r'\D+', s) #dấu
    t = 0
    for i in range(0,len(e)):
        if e[i] == "*":
            n1 = float (d[i])
            n2 = float (d[i+1])
            t = t + (n1 * n2)
            d[i] = t
            del d[i + 1]
            del e[i]
        elif e[i] == "/":
            c1 = float (d[i])
            c2 = float (d[i+1])
            t = t + (c1 / c2)
            d[i] = t
            del d[i+1]
            del e[i]

    for i in range(0,len(e)):
        if e[i] == "+":
            t1 = float (d[i])
            t2 = float (d[i+1])
            t = t + (t1 + t2)
            d[i] = t
            del d[i + 1]
            del e[i]
        elif e[i] == "-":
            r1 = float (d[i])
            r2 = float (d[i+1])
            t = t + (r1 - r2)
            d[i] = t
            del d[i + 1]
            del e[i]

    stringKQ.set(d)

def Clear():
    stringN.set("")
    stringKQ.set("")

Entry (root, width = 23, textvariable=stringN).grid(row = 0, column = 0)
Entry (root, width = 23, textvariable=stringKQ).grid(row = 1, column = 0)

aButton = Frame(root)
Button(aButton, text="1", command = So1, width = 4).pack(side = LEFT)
Button(aButton, text="2", command = So2, width = 4).pack(side = LEFT)
Button(aButton, text="3", command = So3, width = 4).pack(side = LEFT)
aButton.grid(row = 2, column = 0, rowspan =1)

bButton = Frame(root)
Button(bButton, text="4", command = So4, width = 4).pack(side = LEFT)
Button(bButton, text="5", command = So5, width = 4).pack(side = LEFT)
Button(bButton, text="6", command = So6, width = 4).pack(side = LEFT)
bButton.grid(row = 3, column = 0, rowspan =1)

cButton = Frame(root)
Button(cButton, text="7", command = So7, width = 4).pack(side = LEFT)
Button(cButton, text="8", command = So8, width = 4).pack(side = LEFT)
Button(cButton, text="9", command = So9, width = 4).pack(side = LEFT)
cButton.grid(row = 4, column = 0, rowspan =1)

dButton = Frame(root)
Button(dButton, text=".", command = Cham, width = 4).pack(side = LEFT)
Button(dButton, text="0", command = So0, width = 4).pack(side = LEFT)
Button(dButton, text="=", command = Bang, width = 4).pack(side = LEFT)
dButton.grid(row = 5, column = 0, rowspan =1)

eButton = Frame(root)
Button(eButton, text="+", command = Cong, width = 2).pack(side = LEFT)
Button(eButton, text="-", command = Tru, width = 2).pack(side = LEFT)
Button(eButton, text="*", command = Nhan, width = 2).pack(side = LEFT)
Button(eButton, text="/", command = Chia, width = 2).pack(side = LEFT)
eButton.grid(row = 6, column = 0, rowspan =1)

fButton = Frame(root)
Button(fButton, text="Clear", command = Clear, width = 20).pack(side = LEFT)
fButton.grid(row = 7, column = 0, rowspan =1)

root.mainloop()
