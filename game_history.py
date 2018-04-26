
try:
    from Tkinter import *
    from ttk import *
except ImportError:  # Python 3
    from tkinter import *
    from tkinter.ttk import *

import sqlite3

class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.standard_table()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def standard_table(self):
        tv = Treeview(self)
        tv['columns'] = ('time', 'userStatus', 'winner')
        tv.heading("#0", text='Player Name', anchor='w')
        tv.column("#0", anchor="w")

        tv.heading('time', text='Time')
        tv.column('time', anchor='center', width=100)
        tv.heading('userStatus', text='Player Status')
        tv.column('userStatus', anchor='center', width=100)
        tv.heading('winner', text='Winner')
        tv.column('winner', anchor='center', width=100)

        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv

        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):
        try:
            conn = sqlite3.connect("statistics.db")
        except:
            print("Can't connect to sqlite3 database...")

        c = conn.cursor()

        # user name, time, winner
        c.execute("SELECT userName, dayTime, userStatus, winner FROM statistics")
        std = c.fetchall()
        conn.commit()
        conn.close()

        for record in std:
            self.treeview.insert('', 'end', text=record[0], values=(record[1], record[2], record[3]))

def main():
    root = Tk()
    App(root)
    root.title("Game History")
    root.mainloop()

if __name__ == '__main__':
    main()





#
