# start screen

from tkinter import *
import play_screen

root = Tk()
root.resizable(width=False, height=False)
root.title("Start Screen!")
root.geometry('450x450')

# FRAMES

bottom_frame = Frame(root)
bottom_frame.pack(side = BOTTOM)

top_frame = Frame(root)
top_frame.pack(side = TOP)

top_left_frame = Frame(top_frame)
top_left_frame.pack(side = LEFT)

top_right_frame = Frame(top_frame)
top_right_frame.pack(side = RIGHT)


# top right frame 
play_game = Button(top_right_frame, text = "Play Game", width = 20, command = lambda:play_screen.create_screen()) 
play_game.pack(side = TOP)

instructions = Button(top_right_frame, text = "Instructions", width = 20) 
instructions.pack(side = TOP)

resume = Button(top_right_frame, text = "Resume Saved Game", width = 20) 
resume.pack(side = TOP)

r = Label(top_right_frame, text = "", width = 20) 
r.pack(side = TOP)
r = Label(top_right_frame, text = "", width = 20) 
r.pack(side = TOP)
r = Label(top_right_frame, text = "", width = 20) 
r.pack(side = TOP)
r = Label(top_right_frame, text = "", width = 20) 
r.pack(side = TOP)
# top left frame

title = Label(top_left_frame, text = "Sorry!", width = 10, height = 2, font = ("ms serif", 40, "italic"))
title.pack(side = TOP)

filler = Label(top_left_frame, text = "", font = ("ms serif", 30, "italic"))
filler.pack(side = TOP)

name = Frame(top_left_frame)
name.pack(side = TOP)

name_label = Label(name, text = "Enter your name:  ", font = ("ms serif", 14))
name_label.pack(side = LEFT)

name_box = Entry(name, width = 10)
name_box.pack(side = RIGHT)

customize = Label(top_left_frame, text = "  Customize opponent(s):  ", font = ("ms serif", 14))
customize.pack(side = LEFT)

player3 = Frame(bottom_frame, bg = "pale green", width = 375, height = 80)
player3.pack(side = BOTTOM)

##p3 = Label(player3, text = "Player 3")
##p3.pack(side = LEFT)

player2 = Frame(bottom_frame, bg = "SkyBlue1", width = 375, height = 80)
player2.pack(side = BOTTOM)

player1 = Frame(bottom_frame, bg = "lightcoral", width = 375, height = 80)
player1.pack(side = BOTTOM)


