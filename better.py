# from Tkinter import *
# import play_screen
import Tkinter as tk
import SorryGui_copy as play_screen



class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.welcome_page = welcome_page()
        self.welcome_page.pack()


class welcome_page(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("Welcome")
        self.start_fm = tk.Frame(self, height=450, width=450)
        self.start_fm.pack()

        self.title = tk.Label(self.start_fm, text="Sorry!", width=8, height=2, font=("ms serif", 40, "italic"))
        self.start_btn = tk.Button(self.start_fm, text="Start a New Game", width=30, command=self.new_game)
        self.resume_btn = tk.Button(self.start_fm, text="Resume a Saved Game", width=30, command=self.resume_game)
        self.stats_btn = tk.Button(self.start_fm, text="View Game History", width=30, command=self.stats)

        self.title.pack()
        self.start_btn.pack()
        self.resume_btn.pack()
        self.stats_btn.pack()

    def resume_game(self):
        self.start_fm.pack_forget()
        self.master.title("Resuming the Saved Game")

    def new_game(self):
        self.start_fm.pack_forget()
        self.master.title("New Game")
        self.user_page = user_page()
        self.user_page.grid(row=0)

    def stats(self):
        self.start_fm.pack_forget()
        self.master.title("Game History")
        # self.return_btn = tk.Button(self.start_fm, text="Return", width=30)
        # self.return_btn.pack()


class user_page(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        self.name = tk.Frame(self, height=450, width=450)
        self.name.grid_propagate(0)
        self.name.grid(row=0)

        self.title = tk.Label(self.name, text="Welcome!", width=8, height=2, font = ("ms serif", 30, "italic"))
        self.title.grid(row=0)

        self.name_label = tk.Label(self.name, text="Enter your name:  ", font=("ms serif", 14))
        global name_box
        name_box = tk.Entry(self.name, width=10)

        self.color_label = tk.Label(self.name, text="Choose your color:  ", font=("ms serif", 14))
        global user_color
        user_color = tk.StringVar(value='0')
        self.color_choice_r = tk.Radiobutton(self.name, text="Red", variable=user_color, value="red")
        self.color_choice_b = tk.Radiobutton(self.name, text="Blue", variable=user_color, value="blue")
        self.color_choice_y = tk.Radiobutton(self.name, text="Yellow", variable=user_color, value="yellow")
        self.color_choice_g = tk.Radiobutton(self.name, text="Green", variable=user_color, value="green")

        self.opponent_label = tk.Label(self.name, text="Number of opponent:  ", font=("ms serif", 14))
        global num_opponent
        num_opponent = tk.IntVar(value=0)
        self.opponent1 = tk.Radiobutton(self.name, text="1", variable=num_opponent, value=1)
        self.opponent2 = tk.Radiobutton(self.name, text="2", variable=num_opponent, value=2)
        self.opponent3 = tk.Radiobutton(self.name, text="3", variable=num_opponent, value=3)

        self.name_label.grid(row=1, column=0, columnspan=2, sticky='W')
        name_box.grid(row=1, column=2, columnspan=2)

        self.color_label.grid(row=2, column=0, columnspan=2, sticky='W')
        self.color_choice_r.grid(row=2, column=2)
        self.color_choice_b.grid(row=2, column=3)
        self.color_choice_y.grid(row=2, column=4)
        self.color_choice_g.grid(row=2, column=5)

        self.opponent_label.grid(row=3, column=0, columnspan=2, sticky='W')
        self.opponent1.grid(row=3, column=2)
        self.opponent2.grid(row=3, column=3)
        self.opponent3.grid(row=3, column=4)

        self.next_cust_btn = tk.Button(self.name, text="Next", command=lambda: self.next_customize_page())
        self.next_cust_btn.grid(row=4, column=3, pady=10)

    def next_customize_page(self):
        self.name.grid_forget()
        self.master.title("Customize")
        self.customize_page = customize_page()
        self.customize_page.grid(row=0)


class customize_page(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        self.title_fm = tk.Frame(self, width=450, height=80)
        self.title_fm.grid_propagate(0)
        self.title_fm.grid(row=0)

        self.player1 = tk.Frame(self, width=450, height=80)
        self.player2 = tk.Frame(self, width=450, height=80)
        self.player3 = tk.Frame(self, width=450, height=80)
        self.player1.grid_propagate(0)
        self.player2.grid_propagate(0)
        self.player3.grid_propagate(0)

        # title
        self.title = tk.Label(self.title_fm, text="Customize Opponents", font = ("ms serif", 30, "italic"))
        self.title.grid(row=0, column=0, rowspan=2, columnspan=4)

        # player 1
        self.name1 = tk.Label(self.player1, text="Player 1")
        self.name1.grid(row=0, column=0)

        self.skill_r = tk.IntVar()
        self.mean_r = tk.IntVar()

        self.r3_r = tk.Radiobutton(self.player1, text="skilled", variable=self.skill_r, value=2)
        self.r4_r = tk.Radiobutton(self.player1, text="unskilled", variable=self.skill_r, value=1)
        self.r5_r = tk.Radiobutton(self.player1, text="nice", variable=self.mean_r, value=1)
        self.r6_r = tk.Radiobutton(self.player1, text="mean", variable=self.mean_r, value=2)

        self.r3_r.grid(row=0, column=1, sticky='W')
        self.r4_r.grid(row=1, column=1, sticky='W')
        self.r5_r.grid(row=0, column=2, sticky='W')
        self.r6_r.grid(row=1, column=2, sticky='W')

        # player 2
        self.name2 = tk.Label(self.player2, text="Player 2")
        self.name2.grid(row=0, column=0)

        self.skill_b = tk.IntVar()
        self.mean_b = tk.IntVar()

        self.r3_b = tk.Radiobutton(self.player2, text="skilled", variable=self.skill_b,value=2)
        self.r4_b = tk.Radiobutton(self.player2, text="unskilled", variable=self.skill_b, value=1)
        self.r5_b = tk.Radiobutton(self.player2, text="nice", variable=self.mean_b, value=1)
        self.r6_b = tk.Radiobutton(self.player2, text="mean", variable=self.mean_b, value=2)

        self.r3_b.grid(row=0, column=1, sticky='W')
        self.r4_b.grid(row=1, column=1, sticky='W')
        self.r5_b.grid(row=0, column=2, sticky='W')
        self.r6_b.grid(row=1, column=2, sticky='W')

        # player 3
        self.name3 = tk.Label(self.player3, text="Player 3")
        self.name3.grid(row=0, column=0)

        self.skill_g = tk.IntVar()
        self.mean_g = tk.IntVar()

        self.r3_g = tk.Radiobutton(self.player3, text="skilled", variable=self.skill_g, value=2)
        self.r4_g = tk.Radiobutton(self.player3, text="unskilled", variable=self.skill_g, value=1)
        self.r5_g = tk.Radiobutton(self.player3, text="nice", variable=self.mean_g, value=1)
        self.r6_g = tk.Radiobutton(self.player3, text="mean", variable=self.mean_g, value=2)

        self.r3_g.grid(row=0, column=1, sticky='W')
        self.r4_g.grid(row=1, column=1, sticky='W')
        self.r5_g.grid(row=0, column=2, sticky='W')
        self.r6_g.grid(row=1, column=2, sticky='W')

        # keep certain number of players depends on the number of opponents
        self.num_oppo = num_opponent.get()

        self.oppo_list = [self.player1, self.player2, self.player3]
        for i in range(self.num_oppo):
            (self.oppo_list)[i].grid(row=(i+1))

        self.btn_fm = tk.Frame(self, width=450, height=80)
        self.btn_fm.grid(row=self.num_oppo + 2)

        self.start_btn = tk.Button(self.btn_fm, text="Next", command=lambda: self.show_board())
        self.start_btn.grid(row=0)

    def show_board(self):
        self.master.destroy()

        play_screen.create_all(user_color.get(),
                                  num_opponent.get(),
                                  bool(self.skill_r.get() - 1),
                                  bool(self.mean_r.get() - 1),
                                  bool(self.skill_b.get() - 1),
                                  bool(self.mean_b.get() - 1),
                                  bool(self.skill_g.get() - 1),
                                  bool(self.mean_g.get() - 1))


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(width=False, height=False)
    MainApplication(root).pack()
    root.geometry('450x450')
    root.mainloop()