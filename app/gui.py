from tkinter import *
import subprocess

class Application(Frame):
    def send_match(self):
        args = ['python3'] + ['elo/match.py'] + \
                ['--home'] + [self.home.get()] + \
                ['--away'] + [self.away.get()] + \
                ['--home-score'] + [self.home_score.get()] + \
                ['--away-score'] + [self.away_score.get()] + \
                ['--overtime'] + [self.overtime.get()] + \
                ['--league'] + [self.league.get()]

        subprocess.run(args)

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.send = Button(self)
        self.send["text"] = "Enter",
        self.send["command"] = self.send_match

        self.send.pack({"side": "left"})

        self.home = Entry()
        self.home.pack()
        self.home.insert(0, "Home")

        self.away = Entry()
        self.away.pack()
        self.away.insert(0, "Away")

        self.home_score = Entry()
        self.home_score.pack()
        self.home_score.insert(0, "Home score")

        self.away_score = Entry()
        self.away_score.pack()
        self.away_score.insert(0, "Away score")

        self.overtime = Entry()
        self.overtime.pack()
        self.overtime.insert(0, "Overtime")

        self.league = Entry()
        self.league.pack()
        self.league.insert(0, "League")


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
