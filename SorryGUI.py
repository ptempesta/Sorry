from tkinter import *

root = Tk()
root.title("SORRY")

#root.config(background = "#0000FF")

#button1 = Button(root, text = " ", height=0, width=0)
#button1.pack(side = RIGHT)

# top frame
topframe = Frame(root)
topframe.pack(side = TOP)

# bottom frame
bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

# left frames
leftframe = Frame(root)
leftframe.pack(side = LEFT)

insideleft = Frame(leftframe)
insideleft.pack(side = RIGHT)

# right frames
rightframe = Frame(root)
rightframe.pack(side = RIGHT)

insideright = Frame(rightframe)
insideright.pack(side = LEFT)


# top common area
for num in range(16):
    btn = Button(topframe, text = " " , height=0, width=0)
    btn.pack(side = LEFT)

# bottom common area
for num in range(16):
    btn = Button(bottomframe, text = " " , height=0, width=0)
    btn.pack(side = LEFT)


# LEFT FRAME

# left common area
for num in range(14):
    btn = Button(leftframe, text = " " , height=0, width=0)
    btn.pack(side = TOP)

# red safety zone
for i in range(14):
    btn = Label(insideleft, text = " " , height=0, width=0)
    btn.grid(row=i, column=0, pady = 3)
for i in range(6):
    btn = Button(insideleft, text = " " , height=0, width=0, command=lambda:safety_zone("red"))
    btn.grid(row=12, column=i)

# blue safety zone
for i in range(6):
    btn = Button(insideleft, text = " " , height=0, width=0, command=lambda:safety_zone("blue"))
    btn.grid(row=i, column=1)

# RIGHT FRAME

# right common area
for num in range(14):
    btn = Button(rightframe, text = " " , height=0, width=0)
    btn.pack(side = TOP)

# yellow safety zone
for i in range(14):
    btn = Label(insideright, text = " " , height=0, width=0)
    btn.grid(row=i, column=0, pady = 3)
for i in range(6):
    space = "yellow"
    btn = Button(insideright, text = " " , height=0, width=0, command=lambda:safety_zone("yellow"))
    btn.grid(row=1, column=i)

# green safety zone
for i in range(6):
    space = "green"
    btn = Button(insideright, text = " " , height=0, width=0, command=lambda:safety_zone("green"))
    btn.grid(row=(i+8), column=4)

def safety_zone(color):
    print(color, "safety zone space")

def common_area():
    print(color, "safety zone space")
    
root.mainloop()



