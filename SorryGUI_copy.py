from tkinter import *
import player as p
import board as b

CLICK = True
START_IND = 0
END_IND = 0

def create_screen(sorry_board):

    root = Tk()
    #root.resizable(width=False, height=False)
    root.title("Sorry!")
    #root.geometry('500x450')

    # create an empty list of buttons
    buttons = [None]*60
    r_btns = [None]*6
    
    # CREATING FRAMES

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

    # Placing pawns in their correct spaces
    
    occupying_pawns = []
    colored_pawns = []
    # sq.occupyingPawn.color 
    for sq in sorry_board.commonSquareList:
        occupying_pawns.append(sq.occupBool)
        if sq.occupBool == True:
            colored_pawns.append(sq.occupyingPawn.color)
        else:
            colored_pawns.append(None)
            
    red_safety = []
    for sq in sorry_board.redSquareList:
        red_safety.append(sq.occupBool)

    blue_safety = []
    for sq in sorry_board.redSquareList:
        blue_safety.append(sq.occupBool)

    yellow_safety = []
    for sq in sorry_board.redSquareList:
        yellow_safety.append(sq.occupBool)

    green_safety = []
    for sq in sorry_board.redSquareList:
        green_safety.append(sq.occupBool)

    # as of now, these have to line up otherwise error face
    occupying_pawns[23] = True
    colored_pawns[23] = "blue"
    red_safety[3] = True
    blue_safety[4] = True
    green_safety[0] = True
    yellow_safety[1] = True
    
    ims = [PhotoImage(file ='regSquare.gif')]*60
    red_ims = [PhotoImage(file ='regSquare.gif')]*6
    blue_ims = [PhotoImage(file ='regSquare.gif')]*6
    yellow_ims = [PhotoImage(file ='regSquare.gif')]*6
    green_ims = [PhotoImage(file ='regSquare.gif')]*6
    
    for i in range(len(occupying_pawns)):
        if occupying_pawns[i] == True:
            if colored_pawns[i] == 'red':
                ims[i] = PhotoImage(file ='redPawn.gif')
            elif colored_pawns[i] == 'blue':
                ims[i] = PhotoImage(file ='bluePawn.gif')
            if colored_pawns[i] == 'yellow':
                ims[i] = PhotoImage(file ='yellowPawn.gif')
            if colored_pawns[i] == 'green':
                ims[i] = PhotoImage(file ='greenPawn.gif')
            

    for i in range(5):
        if red_safety[i] == True:
            red_ims[i] = PhotoImage(file = 'redPawn.gif')
        if blue_safety[i] == True:
            blue_ims[i] = PhotoImage(file = 'bluePawn.gif')
        if yellow_safety[i] == True:
            yellow_ims[i] = PhotoImage(file = 'yellowPawn.gif')
        if green_safety[i] == True:
            green_ims[i] = PhotoImage(file = 'greenPawn.gif')

    
    # Update method called everytim that a common space button is clicked
    # CLICK = True represents the first click, used to select a pawn
    # CLICK = False represents the second click, used to choose the pawn destination
    def update(btn, index):
        global CLICK
        if CLICK ==True:
            if occupying_pawns[index] == True:
                occupying_pawns[index] = False
                ims[index] = PhotoImage(file = 'regSquare.gif')
                btn.image = ims[index]
                btn.config(image = ims[index])
                CLICK = False
        elif CLICK == False:
            if occupying_pawns[index] == False:
                occupying_pawns[index] = True
                ims[index] = PhotoImage(file = 'bluePawn.gif')
                btn.image = ims[index]
                btn.config(image = ims[index])
                CLICK = True

    def r_safety_update(btn, index):
        global CLICK
        if CLICK ==True:
            if red_safety[index] == True:
                red_safety[index] = False
                red_ims[index] = PhotoImage(file = 'regSquare.gif')
                btn.image = red_ims[index]
                btn.config(image = red_ims[index])
                CLICK = False
        elif CLICK == False:
            if red_safety[index] == False:
                red_safety[index] = True
                red_ims[index] = PhotoImage(file = 'redPawn.gif')
                btn.image = ims[index]
                btn.config(image = red_ims[index])
                CLICK = True
            

    # left common area
    index = 13
    for num in range(14):
        btn = Button(leftframe, text = "  ", image = ims[index], height=20, width=20, command=lambda index=index:update(buttons[index], index))
        buttons[index] = btn
        btn.pack(side = TOP)
        index -= 1
        
    # top common area   
    index = 14
    for num in range(16):
        btn = Button(topframe, text = "  ", image = ims[index], height=20, width=20, command=lambda index=index:update(buttons[index], index))
        buttons[index] = btn
        btn.pack(side = LEFT)
        index += 1
        
        
    # right common area
    for num in range(14):
        btn = Button(rightframe, text = "  ", image = ims[index], height=20, width=20, command=lambda index=index:update(buttons[index], index))
        buttons[index] = btn
        btn.pack(side = TOP)
        index += 1

    # bottom common area
    index = index + 15
    for num in range(16):
        btn = Button(bottomframe, text = "  " , image = ims[index] ,height=20, width=20, command=lambda index=index:update(buttons[index], index))
        buttons[index] = btn
        btn.pack(side = LEFT)
        index -= 1


    # red safety zone
    for i in range(14):
        if i != 10:
            btn = Label(insideleft, text = "  " , height=0, width=0)
            btn.grid(row=i, column=0, pady = 3)
        else:
            # red start zone
            btn = Button(insideleft, text = "  " , image = ims[index], height=20, width=20, command=lambda:start_zone(btn, "red"))
            btn.grid(row=i, column=0)
    for r_index in range(6):
        btn = Button(insideleft, text = "  " , image = red_ims[r_index], height=20, width=20, command=lambda r_index = r_index :r_safety_update(r_btns[r_index], r_index))
        r_btns[r_index] = btn
        btn.grid(row=12, column=r_index)

    # blue safety zone
    for b_index in range(6):
        btn = Button(insideleft, text = "  " , image = blue_ims[b_index], height=20, width=20, command=lambda:safety_zone(btn, "blue"))
        btn.grid(row=b_index, column=1)
    # blue start zone
    btn = Button(insideleft, text = " ", image = ims[index],  height=20, width=20, command=lambda:start_zone(btn, "blue"))
    btn.grid(row=0, column=3)

    # yellow safety zone
    for i in range(14):
        if i != 3:
            btn = Label(insideright, text = "  " , height=0, width=0)
            btn.grid(row=i, column=0, pady = 3)
        else:
            # yellow start zone
            btn = Button(insideright, text = "  " , image = ims[index], height=20, width=20, command=lambda:start_zone(btn, "yellow")) 
            btn.grid(row=i, column=5)
    y_index = 5
    for i in range(6):
        btn = Button(insideright, text = "  ", image = yellow_ims[y_index], height=20, width=20, command=lambda:safety_zone(btn, "yellow"))
        btn.grid(row=1, column=i)
        y_index-=1

    g_index = 5
    # green safety zone
    for i in range(6):
        btn = Button(insideright, text = "  " , image = green_ims[g_index], height = 20, width = 20, command=lambda:safety_zone(btn, "green"))
        btn.grid(row=(i+8), column=4)
        g_index -= 1
    # green start
    btn = Button(insideright, image = ims[index], height=20, width=20, command=lambda:p.player("green"))
    btn.grid(row=13, column=2)

    def safety_zone(btn, color):
        print(color, "safety zone space")
            
    def start_zone(btn, color):
        print(color, "start zone")

    root.mainloop()

def create_all(playerColorChoice, adversaryCount):
        sorry_board = b.board(playerColorChoice, adversaryCount)
        #safety squares
        print(sorry_board.redSquareList)
        print(sorry_board.blueSquareList)
        print(sorry_board.yellowSquareList)
        print(sorry_board.greenSquareList)
        #pawn list, one for each player
        #loop through this to see pawn scores, if 0, in start zone, if 65 then in end zone
        print(sorry_board.userPlayer.pawnList)
        for pawn in sorry_board.compPlayer1.pawnList:
            print(pawn.score)
            
        create_screen(sorry_board)

create_all("red", 3)

