from tkinter import *

root = Tk()

stringND = StringVar()
stringNA = StringVar()

def Can(a):
    can = ["Quý", "Giáp", "Ất", "Bính", "Đính", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm"]
    for i in range(len(can)):
        if (i == a):
            return can[i]

def Chi(b):
    chi = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tị", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
    if (b == 0):
        return chi [11]
    else:
        for i in range(len(chi)):
            if (i == b - 1):
                return chi[i]

def Chuyen():
    d = int(stringND.get())
    d -=  3
    aa = str(d)
    cc = len(aa)-1
    bb = int(aa[cc])
    can = Can(bb)
    ch = d % 12
    chi = str(Chi(int(ch)))
    nam = can + " " + chi
    stringNA.set(str(nam))



root.minsize(height =150, width = 330)
root.configure(bg="yellow")

Label(root, text="Nhập nâm dương:", bg="yellow").grid(row = 0, column=0)
Entry(root, width=15, textvariable=stringND, fg="red").grid(row = 0, column = 1)

aButton = Frame(root)
Button(root, text = "Chuyển", command = Chuyen, width = 4).grid(row = 1, column = 1)

Label(root, text="Nhập âm:", bg="yellow").grid(row = 2, column=0)
Entry(root, width=15, textvariable=stringNA, bg="yellow").grid(row = 2, column = 1)

root.mainloop()
