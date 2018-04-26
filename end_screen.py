import Tkinter as tk
import better
import game_history

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("Game Over")

        # Message
        self.user_name = "temp_user"
        self.user_status = "lose"
        self.winner_name = "player1"
        self.message = self.generate_message()

        self.show = tk.Label(self, text=self.message, font=("ms serif", 30), pady=10)
        self.show.pack()

        # Buttons
        self.new_game_btn = tk.Button(self, text="Start a New Game", width=30, command=self.start_new_game)
        self.stats_btn = tk.Button(self, text="View Game History", width=30, command=self.stats)
        self.quit_btn = tk.Button(self, text="Quit", width=30, command=self.quit_game)
        self.new_game_btn.pack()
        self.stats_btn.pack()
        self.quit_btn.pack()

    def generate_message(self):
        if self.winner_name == self.user_name:  # user win
            self.message = "Congratulation! You win! Good job " + self.user_name
        elif self.user_status == "quit":  # user quit
            self.message = "You quit the game"
        else:  # user lose
            self.message = self.winner_name + " win!"
        return self.message

    def start_new_game(self):
        self.parent.destroy()
        self.user_page = better.user_page()
        self.user_page.grid(row=0)

    def stats(self):
        self.history = game_history.main()

    def quit_game(self):
        self.parent.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(width=False, height=False)
    MainApplication(root).pack()
    root.geometry('450x450')
    root.mainloop()