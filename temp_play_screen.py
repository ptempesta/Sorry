from Tkinter import *
import board as b

def create_screen():
    
    root = Tk()
    root.resizable(width=False, height=False)
    root.title("Sorry!")
    root.geometry('700x450')

    # CREATING FRAMES
    board_fm = Frame(root, background="bisque")

    # top frame
    topframe = Frame(board_fm)
    topframe.pack(side = TOP)

    # bottom frame
    bottomframe = Frame(board_fm)
    bottomframe.pack(side = BOTTOM)

    # left frames
    leftframe = Frame(board_fm)
    leftframe.pack(side = LEFT)

    insideleft = Frame(leftframe)
    insideleft.pack(side = RIGHT)

    # right frames
    rightframe = Frame(board_fm)
    rightframe.pack(side = RIGHT)

    insideright = Frame(rightframe)
    insideright.pack(side = LEFT)

    # CREATING SPACES

    # left common area
    index = 13
    for num in range(14):
        btn = Button(leftframe, text = "  ", height=0, width=0, command=lambda index=index: common_area(btn, "red", index))
        btn.pack(side = TOP)
        index -= 1

    # top common area   
    index = 14
    for num in range(16):
        btn = Button(topframe, text = "  ", height=0, width=0, command=lambda index=index:common_area(btn, "blue", index))
        btn.pack(side = LEFT)
        index += 1

    # right common area
    for num in range(14):
        btn = Button(rightframe, text = "  ", height=0, width=0, command=lambda index=index:common_area(btn, "yellow",index))
        btn.pack(side = TOP)
        index += 1

    # bottom common area
    index = index + 15
    for num in range(16):
        btn = Button(bottomframe, text = "  " , height=0, width=0, command=lambda index=index:common_area(btn, "green", index))
        btn.pack(side = LEFT)
        index -= 1


    # red safety zone
    for i in range(14):
        if i != 10:
            btn = Label(insideleft, text = "  " , height=0, width=0)
            btn.grid(row=i, column=0, pady = 3)
        else:
            # red start zone
            btn = Button(insideleft, text = "  " , height=0, width=0, command=lambda:start_zone(btn, "red"))
            btn.grid(row=i, column=0)
    for r_index in range(6):
        btn = Button(insideleft, text = "  " , height=0, width=0, command=lambda:safety_zone(btn, "red"))
        btn.grid(row=12, column=r_index)

    # blue safety zone
    for b_index in range(6):
        btn = Button(insideleft, text = "  " , height=0, width=0, command=lambda:safety_zone(btn, "blue"))
        btn.grid(row=b_index, column=1)
    # blue start zone
    # PHOTO TESTING
    #im = PhotoImage('pawn2.png', height = 10, width = 10)
    btn = Button(insideleft , fg = 'red', text = "X", height=0, width=0, command=lambda:start_zone(btn, "blue"))
    btn.grid(row=0, column=3)

    # yellow safety zone
    for i in range(14):
        if i != 3:
            btn = Label(insideright, text = "  " , height=0, width=0)
            btn.grid(row=i, column=0, pady = 3)
        else:
            # yellow start zone
            btn = Button(insideright, text = "  " , height=0, width=0, command=lambda:start_zone(btn, "yellow")) 
            btn.grid(row=i, column=5)
    y_index = 5
    for i in range(6):
        btn = Button(insideright, text = "  ", height=0, width=0, command=lambda:safety_zone(btn, "yellow"))
        btn.grid(row=1, column=i)
        y_index-=1

    g_index = 5
    # green safety zone
    for i in range(6):
        btn = Button(insideright, text = "  " , height=0, width=0, command=lambda:safety_zone(btn, "green"))
        btn.grid(row=(i+8), column=4)
        g_index -= 1
    # green start 
    btn = Button(insideright, text = "  " , height=0, width=0, command=lambda:start_zone(btn, "green"))
    btn.grid(row=13, column=2)


    ###################### Functions

    right_func_fm = Frame(root)
    save_game = Button(right_func_fm, text="Save Game", width=20).pack(side=TOP)

    instructions = Button(right_func_fm, text="Instructions", width=20).pack(side=TOP)

    message = "Welcome" + "\n" + "Click"

    def update_message():

        ##### Test
        message = "Red Player Turn"
        # to be updated, for each time the user click that buttn
        label1.configure(text=message)

    draw = Button(right_func_fm, text="Draw Card", width=20, command=update_message).pack(side=TOP)

    b1 = Label(right_func_fm, text="This"+"\n"+"That", borderwidth=2, relief="groove", width=10, height=10).pack(side=TOP)

    label1 = Label(right_func_fm, text=message)
    label1.pack(side=TOP)

    board_fm.pack(side = LEFT,fill=None, expand=False)
    right_func_fm.pack(side=RIGHT, fill = BOTH)


    # FUNCTIONS TRIGGERED
                
    root.mainloop()

def safety_zone(btn, color):
    print(color, "safety zone space")

def start_zone(btn, color):
    print(color, "start zone")

def common_area(btn, color, index):
    print(color, "common area space")
    
def create_all(playerColorChoice, adversaryCount):

    b.board(playerColorChoice, adversaryCount)
    create_screen()


