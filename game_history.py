try:
    from Tkinter import *
    from ttk import *
except ImportError:  # Python 3
    from tkinter import *
    from tkinter.ttk import *

import sqlite3

class MainApplication(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.std_window = Toplevel()
        self.std_window.title("Game History")
        self.standard_table = standard_table(self.std_window)
        self.summary_table = summary_table(self.std_window)


class standard_table(Frame):
    def __init__(self, std_window):

        self.tv = Treeview(std_window)
        self.tv['columns'] = ('userName', 'time', 'userStatus', 'winner')
        self.tv.heading("#0", text='Game Number', anchor='w')
        self.tv.column("#0", anchor="w")

        self.tv.heading('userName', text='Player Name')
        self.tv.column('userName', anchor='center', width=100)
        self.tv.heading('time', text='Time')
        self.tv.column('time', anchor='center', width=100)
        self.tv.heading('userStatus', text='Player Status')
        self.tv.column('userStatus', anchor='center', width=100)
        self.tv.heading('winner', text='Winner')
        self.tv.column('winner', anchor='center', width=100)

        self.tv.grid(sticky=(N, S, W, E))
        self.tv.bind("<Double-1>", self.OnDoubleClick)

        try:
            conn = sqlite3.connect("statistics.db")
        except:
            print("Can't connect to sqlite3 database...")

        c = conn.cursor()
        c.execute("SELECT * FROM statistics ORDER BY id DESC")
        std = c.fetchall()
        conn.close()

        for record in std:
            self.tv.insert('', 'end', text=record[0], values=(record[1], record[2], record[3], record[4]))


    def OnDoubleClick(self, event):
        self.record = self.tv.selection()
        self.game_number = self.tv.item(self.record, "text")
        self.child_window = child_window(self.game_number)

class child_window(Frame):
    def __init__(self, game_number):

        win2 = Toplevel()
        win2.title("Computer Settings")

        self.tree = Treeview(win2)
        self.tree['columns'] = ('color', 'difficulty', 'sadism', 'status')
        self.tree.heading("#0", text='Game Number', anchor='w')
        self.tree.column("#0", anchor="w")

        self.tree.heading('color', text='Computer Color')
        self.tree.column('color', anchor='center', width=100)
        self.tree.heading('difficulty', text='Difficulty')
        self.tree.column('difficulty', anchor='center', width=100)
        self.tree.heading('sadism', text='Sadism')
        self.tree.column('sadism', anchor='center', width=100)
        self.tree.heading('status', text='Computer Status')
        self.tree.column('status', anchor='center', width=100)

        self.tree.grid(sticky=(N, S, W, E))

        try:
            conn = sqlite3.connect("statistics.db")
        except:
            print("Can't connect to sqlite3 database...")

        c = conn.cursor()
        c.execute("SELECT * FROM computerSettings WHERE id = " + str(game_number))
        computer = c.fetchall()
        conn.close()

        for record in computer:
            self.tree.insert('', 'end', text=record[0], values=(record[1], record[2], record[3], record[4]))


class summary_table(Frame):
    def __init__(self, std_window):

        self.tv2 = Treeview(std_window)

        self.tv2['columns'] = ('count')
        self.tv2.heading("#0", text='Player Status', anchor='w')
        self.tv2.column("#0", anchor="w")

        self.tv2.heading('count', text='Count')
        self.tv2.column('count', anchor='center', width=100)

        self.tv2.grid(sticky=(N, S, W, E))

        try:
            conn = sqlite3.connect("statistics.db")
        except:
            print("Can't connect to sqlite3 database...")

        c = conn.cursor()

        c.execute("SELECT userStatus, COUNT(*) FROM statistics GROUP BY userStatus ORDER BY COUNT(*) DESC")
        std = c.fetchall()
        conn.close()

        for record in std:
            self.tv2.insert('', 'end', text=record[0], values=(record[1]))


if __name__ == '__main__':
    root = Tk()
    root.resizable(width=False, height=False)
    MainApplication(root).grid()
    root.title("Game History")
    root.mainloop()