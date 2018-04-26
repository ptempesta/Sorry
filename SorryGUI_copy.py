from tkinter import *
import player as p
import board as b
import time

CLICK = True
START_IND = 0
END_IND = 0
TURN_INDEX = 0
TURN = "red"
WIN = {"red":0,"blue":0,"yellow":0,"green":0}

def create_screen(sorry_board):
    
    root = Tk()
    root.resizable(width=False, height=False)
    root.title("Sorry!")

    def whos_turn():
        global TURN_INDEX
        turns = ['red', 'blue', 'yellow', 'green']
        turn = turns[TURN_INDEX]
        TURN_INDEX += 1
        if TURN_INDEX == 4:
            TURN_INDEX = 0
        return turn
        

    # create an empty list of buttons
    buttons = [None]*60
    r_btns = [None]*6
    b_btns = [None]*6
    y_btns = [None]*6
    g_btns = [None]*6
    
    # CREATING FRAMES
    boardframe = Frame(root)
    boardframe.pack(side = LEFT)

    outsideright = Frame(root, padx=30, pady = 30)
    outsideright.pack(side = RIGHT)
    
    # top frame
    topframe = Frame(boardframe)
    topframe.pack(side = TOP)

    # bottom frame
    bottomframe = Frame(boardframe)
    bottomframe.pack(side = BOTTOM)

    # left frames
    leftframe = Frame(boardframe)
    leftframe.pack(side = LEFT)

    insideleft = Frame(leftframe)
    insideleft.pack(side = RIGHT)

    # right frames
    rightframe = Frame(boardframe)
    rightframe.pack(side = RIGHT)

    insideright = Frame(rightframe)
    insideright.pack(side = LEFT)

    # STORING PAWN INFORMATION

    # common zone information 
    occupying_pawns = []
    colored_pawns = []
    for sq in sorry_board.commonSquareList:
        occupying_pawns.append(sq.occupBool)
        if sq.occupBool == True:
            colored_pawns.append(sq.occupyingPawn.color)
        else:
            colored_pawns.append(None)
    
    # safety zone information 
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
    
    # user player scores
    userPlayerScores = []
    for pawn in sorry_board.userPlayer.pawnList:
        userPlayerScores.append(pawn.score)

    # computer player scores
    compPlayer1Scores = []
    for pawn in sorry_board.compPlayer1.pawnList:
        compPlayer1Scores.append(pawn.score)
    compPlayer2Scores = []
    for pawn in sorry_board.compPlayer2.pawnList:
        compPlayer2Scores.append(pawn.score)
    compPlayer3Scores = []
    for pawn in sorry_board.compPlayer3.pawnList:
        compPlayer3Scores.append(pawn.score)

    # as of now, these numeric values have to line up otherwise error face
    occupying_pawns[26] = True
    colored_pawns[26] = "blue"
    occupying_pawns[38] = True
    colored_pawns[38] = "red"
    occupying_pawns[2] = True
    colored_pawns[2] = "yellow"
    occupying_pawns[0] = True
    colored_pawns[0] = "green"
    
    red_safety[3] = True
    red_safety[1] = True
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

    # Deck and drawing cards

    save_game = Button(outsideright, text="Save Game", width=20)
    save_game.pack(side=TOP)

    instructions = Button(outsideright, text="Instructions", width=20)
    instructions.pack(side=TOP)

    message = "Welcome" + "\n" + "Click"

    draw = Button(outsideright, text="Draw Card", width=20, command = lambda: update_card())
    draw.pack(side=TOP)

    b1 = Label(outsideright, text="Draw Card to begin", borderwidth=2, relief="groove", width=17, height=15)
    b1.pack(side=TOP)

    def update_card():
        card_message =  sorry_board.cardDeck.draw(sorry_board.cardDeck.cardStack).cardMessage
        b1.text = card_message
        b1.config(text = card_message)
        

    label1 = Label(outsideright, text=message)
    label1.pack(side=TOP)

    outsideright.pack(side=RIGHT, fill = BOTH)
    # Update methods are called everytime that a common space button is clicked
    # CLICK = True represents the first click, used to select a pawn
    # CLICK = False represents the second click, used to choose the pawn destination

    global TURN
    TURN = whos_turn()
    label1.configure(text=("Turn:", TURN))

    # Computer update method lets say comp 1 that is blue
    def computer_move():
        move = 4
        # get current location
        # current_location = (sorry_board.compPlayer1.pawnList[0].score) + offset
        current_location = 26
        occupying_pawns[current_location] = False
        # remove
        ims[current_location] = PhotoImage(file = 'regSquare.gif')
        buttons[current_location].image = ims[current_location]
        buttons[current_location].config(image = ims[current_location])
        # place
        # time.sleep(1)
        new_location = current_location + move
        ims[new_location] = PhotoImage(file = 'bluePawn.gif')
        buttons[new_location].image = ims[new_location]
        buttons[new_location].config(image = ims[new_location])
        occupying_pawns[current_location] = True
        # next turn
        TURN = whos_turn()
        label1.configure(text=("Turn" + TURN))
        
    #  User Common Area Update Method
    def common_update(btn, index):
        global CLICK
        global TURN
        if CLICK ==True:
            print(occupying_pawns[index] , colored_pawns[index], TURN) 
            if occupying_pawns[index] == True and colored_pawns[index] == TURN:
                occupying_pawns[index] = False
                colored_pawns[index] = None
                ims[index] = PhotoImage(file = 'regSquare.gif')
                btn.image = ims[index]
                btn.config(image = ims[index])
                CLICK = False
        elif CLICK == False:
            if occupying_pawns[index] == False:
                occupying_pawns[index] = True
                colored_pawns[index] = TURN
                if TURN == "red":
                    ims[index] = PhotoImage(file = 'redPawn.gif')
                elif TURN == "blue":
                    ims[index] = PhotoImage(file = 'bluePawn.gif')
                elif TURN == "yellow":
                    ims[index] = PhotoImage(file = 'yellowPawn.gif')
                elif TURN == "green":
                    ims[index] = PhotoImage(file = 'greenPawn.gif')
                btn.image = ims[index]
                btn.config(image = ims[index])
                CLICK = True
                TURN = whos_turn() # update turn when pawn is successfully placed somewhere
                label1.configure(text=("Turn:" +TURN))
##                if TURN != "red":
##                    time.sleep(1)
##                    computer_move()
                
                    
    # User Safety Zone update method
    # need to make applicable for all possible colors 
    def safety_update(btn, index, safety, s_ims):
        global CLICK
        global TURN
        pawn_images = { "red" : ['redPawn.gif','redPawn2.gif','redPawn3.gif'],
                        "blue": ['bluePawn.gif','bluePawn2.gif','bluePawn3.gif'],
                        "yellow": ['yellowPawn.gif','yellowPawn2.gif','yellowPawn3.gif'],
                        "green": ['greenPawn.gif','greenPawn2.gif','greenPawn3.gif']
                        }
        if index == 5:
            WIN[TURN]+=1
            if WIN[TURN] == 1:
                im = PhotoImage(file = pawn_images[TURN][0])
            elif WIN[TURN] == 2:
                im = PhotoImage(file = pawn_images[TURN][1])
            elif WIN[TURN] == 3:
                im = PhotoImage(file = pawn_images[TURN][2])
                print(TURN, "WINS")
            else:
                im = PhotoImage(file = pawn_image[TURN][3])
            btn.image = im
            btn.config(image = im)
            CLICK = True
            TURN = whos_turn() # update turn when pawn is successfully placed somewhere
            print("Turn:", TURN)
        else:
            if CLICK == True:
                if safety[index] == True:
                    safety[index] = False
                    s_ims[index] = PhotoImage(file = 'regSquare.gif')
                    btn.image = s_ims[index]
                    btn.config(image = s_ims[index])
                    CLICK = False
            elif CLICK == False:
                if safety[index] == False:
                    safety[index] = True
                    s_ims[index] = PhotoImage(file = pawn_images[TURN][0])
                    btn.image = s_ims[index]
                    btn.config(image = s_ims[index])
                    CLICK = True
                    TURN = whos_turn() # update turn when pawn is successfully placed somewhere
                    print("Turn:", TURN)

    # Blue Safety Zone update method 
    def b_safety_update(btn, index):
        global CLICK
        if index == 5:
            WIN["blue"]+=1
            one_image = PhotoImage(file = 'bluePawn.gif')
            btn.image = one_image
            btn.config(image = one_image)
            print("one guy in the safety zone yo!")
        else:
            if CLICK ==True:
                if blue_safety[index] == True:
                    blue_safety[index] = False
                    blue_ims[index] = PhotoImage(file = 'regSquare.gif')
                    btn.image = blue_ims[index]
                    btn.config(image = blue_ims[index])
                    CLICK = False
            elif CLICK == False:
                if blue_safety[index] == False:
                    blue_safety[index] = True
                    blue_ims[index] = PhotoImage(file = 'bluePawn.gif')
                    btn.image = blue_ims[index]
                    btn.config(image = blue_ims[index])
                    CLICK = True
                    
    # Green Safety Zone update method
    def g_safety_update(btn, index):
        global CLICK
        if index == 5:
            WIN["green"]+=1
            one_image = PhotoImage(file = 'greenPawn.gif')
            btn.image = one_image
            btn.config(image = one_image)
            print("one guy in the safety zone yo!")
            print(CLICK)
        else:
            if CLICK ==True:
                if green_safety[index] == True:
                    green_safety[index] = False
                    green_ims[index] = PhotoImage(file = 'regSquare.gif')
                    btn.image = green_ims[index]
                    btn.config(image = green_ims[index])
                    CLICK = False
            elif CLICK == False:
                if green_safety[index] == False:
                    green_safety[index] = True
                    green_ims[index] = PhotoImage(file = 'greenPawn.gif')
                    btn.image = green_ims[index]
                    btn.config(image = green_ims[index])
                    CLICK = True

    # Yellow Safety Zone update method
    def y_safety_update(btn, index):
        global CLICK
        if index == 5:
            WIN["yellow"]+=1
            one_image = PhotoImage(file = 'yellowPawn.gif')
            btn.image = one_image
            btn.config(image = one_image)
            print("one guy in the safety zone yo!")
        else:
            if CLICK ==True:
                if yellow_safety[index] == True:
                    yellow_safety[index] = False
                    yellow_ims[index] = PhotoImage(file = 'regSquare.gif')
                    btn.image = yellow_ims[index]
                    btn.config(image = yellow_ims[index])
                    CLICK = False
            elif CLICK == False:
                if yellow_safety[index] == False:
                    yellow_safety[index] = True
                    yellow_ims[index] = PhotoImage(file = 'yellowPawn.gif')
                    btn.image = yellow_ims[index]
                    btn.config(image = yellow_ims[index])
                    CLICK = True
        
                

    # left common area
    index = 13
    for num in range(14):
        btn = Button(leftframe, text = "  ", image = ims[index], height=30, width=30, command=lambda index=index:common_update(buttons[index], index))
        buttons[index] = btn
        btn.pack(side = TOP)
        index -= 1
        
    # top common area   
    index = 14
    for num in range(16):
        btn = Button(topframe, text = "  ", image = ims[index], height=30, width=30, command=lambda index=index:common_update(buttons[index], index))
        buttons[index] = btn
        btn.pack(side = LEFT)
        index += 1
        
        
    # right common area
    for num in range(14):
        btn = Button(rightframe, text = "  ", image = ims[index], height=30, width=30, command=lambda index=index:common_update(buttons[index], index))
        buttons[index] = btn
        btn.pack(side = TOP)
        index += 1

    # bottom common area
    index = index + 15
    for num in range(16):
        btn = Button(bottomframe, text = "  " , image = ims[index] ,height=30, width=30, command=lambda index=index:common_update(buttons[index], index))
        buttons[index] = btn
        btn.pack(side = LEFT)
        index -= 1


    # red safety zone
    for i in range(14):
        if i != 10:
            btn = Label(insideleft, text = "  " , height=0, width=0)
            btn.grid(row=i, column=0, pady =9)
        else:
            # red start zone
            r_start_img = PhotoImage(file = 'redPawn3.gif')
            btn = Button(insideleft, text = "  " , image = r_start_img, height=30, width=30, command=lambda:start_zone(btn, "red"))
            btn.grid(row=i, column=0)
    for r_index in range(6):
        btn = Button(insideleft, text = "  " , image = red_ims[r_index], height=30, width=30, command=lambda r_index = r_index :safety_update(r_btns[r_index], r_index, red_safety, red_ims))
        r_btns[r_index] = btn
        btn.grid(row=12, column=r_index)

    # blue safety zone
    for b_index in range(6):
        btn = Button(insideleft, text = "  " , image = blue_ims[b_index], height=30, width=30, command=lambda b_index = b_index :safety_update(b_btns[b_index], b_index, blue_safety, blue_ims))
        b_btns[b_index] = btn
        btn.grid(row=b_index, column=1)
    # blue start zone
    b_start_img = PhotoImage(file = 'bluePawn3.gif')
    btn = Button(insideleft, text = " ", image = b_start_img,  height=30, width=30, command=lambda:safety_zone(btn, "blue"))
    btn.grid(row=0, column=3)

    # yellow safety zone
    for i in range(14):
        if i != 3:
            btn = Label(insideright, text = "  " , height=0, width=0)
            btn.grid(row=i, column=0, pady =9)
        else:
            # yellow start zone
            y_start_img = PhotoImage(file = 'yellowPawn3.gif')
            btn = Button(insideright, text = "  " , image = y_start_img, height=30, width=30, command=lambda:start_zone(btn, "yellow")) 
            btn.grid(row=i, column=5)
    y_index = 5
    for i in range(6):
        btn = Button(insideright, text = "  ", image = yellow_ims[y_index], height=30, width=30, command=lambda y_index = y_index: safety_update(y_btns[y_index], y_index, yellow_safety, yellow_ims))
        y_btns[y_index] = btn
        btn.grid(row=1, column=i)
        y_index-=1

    g_index = 5
    # green safety zone
    for i in range(6):
        btn = Button(insideright, text = "  " , image = green_ims[g_index], height = 30, width = 30, padx = 100, command=lambda g_index = g_index: safety_update(g_btns[g_index], g_index, green_safety, green_ims))
        g_btns[g_index] = btn
        btn.grid(row=(i+8), column=4)
        g_index -= 1
    # green start
    g_start_img = PhotoImage(file = 'greenPawn3.gif')
    btn = Button(insideright, image = g_start_img, height=30, width=30, command=lambda:start_zone(btn, "green"))
    btn.grid(row=13, column=2)

    def safety_zone(btn, color):
        print(color, "safety zone space")
            
    def start_zone(btn, color):
        print(color, "start zone")


    root.mainloop()

def create_all(playerColorChoice, adversaryCount, skillR, meanR, skillB, meanB, skillG, meanG):
        sorry_board = b.board(playerColorChoice, adversaryCount)
        #safety squares
##        print(sorry_board.redSquareList)
##        print(sorry_board.blueSquareList)
##        print(sorry_board.yellowSquareList)
##        print(sorry_board.greenSquareList)
##        #pawn list, one for each player
        #loop through this to see pawn scores, if 0, in start zone, if 65 then in end zone
##        print(sorry_board.userPlayer.pawnList)
        for pawn in sorry_board.compPlayer3.pawnList:
            print(pawn.color)
            
        create_screen(sorry_board)

create_all("red", 3, True, True, True, True, True, True)

