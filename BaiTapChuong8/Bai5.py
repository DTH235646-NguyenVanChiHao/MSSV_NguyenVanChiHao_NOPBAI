from tkinter import *

root = Tk()

stringOPW = StringVar()
stringNPW = StringVar()
stringAgain = StringVar()

root.title("ENTER NEW PASSWORD")
root.minsize(height =150, width = 330)

Label(root, text="Old Password: ", anchor = "w").grid(row = 1, column = 0, sticky="w")
Entry(root, width=15, textvariable=stringOPW, show = "*").grid(row = 1, column = 1)
Label(root, text="New Password: ", anchor = "w").grid(row = 2, column = 0, sticky="w")
Entry(root, width=15, textvariable=stringNPW, show = "*").grid(row = 2, column = 1)
Label(root, text="Enter New Password Again: ").grid(row = 3, column = 0)
Entry(root, width=15, textvariable=stringAgain, show = "*").grid(row = 3, column = 1)

aButton = Frame(root)
Button(aButton, text="OK", command = lambda: print ("OK clicked"), width = 4).pack(side = LEFT)
Button(aButton, text="Cancel", command = root.quit(), width = 4).pack(side = LEFT)
aButton.grid(row = 4, column = 0)

root.mainloop()