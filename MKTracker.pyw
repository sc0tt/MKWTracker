import Tkinter
import sqlite3
import time

class MKTracker(Tkinter.Frame):
  track_list = ("Bowser's Castle","Coconut Mall","Daisy Circuit","DK Summit","Dry Dry Ruins","DS Delfino Square","DS Desert Hills","DS Peach Gardens","DS Yoshi Falls","GBA Bowser Castle 3","GBA Shy Guy Beach","GCN DK Mountain","GCN Mario Circuit","GCN Peach Beach","GCN Waluigi Stadium","Grumble Volcano","Koopa Cape","Luigi Circuit","Maple Treeway","Mario Circuit","Moo Moo Meadows","Moonview Highway","Mushroom Gorge","N64 Bowser's Castle","N64 DK's Jungle Parkway","N64 Mario Raceway","N64 Sherbert Land","Rainbow Road","SNES Ghost Valley 2","SNES Mario Circuit 3","Toad's Factory","Wario's Gold Mine")
  types = ("100","150","Mirrored")

  def __init__(self, parent):
    Tkinter.Frame.__init__(self, parent)
    self.db = sqlite3.connect("mk.db")
    self.cursor = self.db.cursor()
    self.cursor.execute("CREATE TABLE IF NOT EXISTS mk_data (time string, num_players integer, type string, track string, rank integer, d_score integer, f_score integer, b_score integer)")
    self.init_ui()

  def init_ui(self):
    self.pack(fill=Tkinter.BOTH, expand=1)

    self.num_players = Tkinter.StringVar()
    Tkinter.Label(self, text="Number of Players:").grid(sticky=Tkinter.E, row=0, column=0, padx=5, pady=5)
    Tkinter.Entry(self, textvariable=self.num_players).grid(sticky=Tkinter.E+Tkinter.W, row=0, column=1, padx=5, pady=5)

    self.type = Tkinter.StringVar()
    self.type.set(self.types[0])
    Tkinter.Label(self, text="Type:").grid(sticky=Tkinter.E, row=1, column=0, padx=5, pady=5)
    Tkinter.OptionMenu(self, self.type, *self.types).grid(sticky=Tkinter.E+Tkinter.W, row=1, column=1, padx=5, pady=5)

    self.track = Tkinter.StringVar()
    self.track.set(self.track_list[0])
    Tkinter.Label(self, text="Track:").grid(sticky=Tkinter.E, row=2, column=0, padx=5, pady=5)
    Tkinter.OptionMenu(self, self.track, *self.track_list).grid(sticky=Tkinter.E+Tkinter.W, row=2, column=1, padx=5, pady=5)

    self.rank = Tkinter.StringVar()
    Tkinter.Label(self, text="Rank:").grid(sticky=Tkinter.E, row=3, column=0, padx=5, pady=5)
    Tkinter.Entry(self, textvariable=self.rank).grid(sticky=Tkinter.E+Tkinter.W, row=3, column=1, padx=5, pady=5)

    self.d_score = Tkinter.StringVar()
    Tkinter.Label(self, text="Delta Score:").grid(sticky=Tkinter.E, row=4, column=0, padx=5, pady=5)
    Tkinter.Entry(self, textvariable=self.d_score).grid(sticky=Tkinter.E+Tkinter.W, row=4, column=1, padx=5, pady=5)

    self.f_score = Tkinter.StringVar()
    Tkinter.Label(self, text="Final Score:").grid(sticky=Tkinter.E, row=5, column=0, padx=5, pady=5)
    Tkinter.Entry(self, textvariable=self.f_score).grid(sticky=Tkinter.E+Tkinter.W, row=5, column=1, padx=5, pady=5)

    Tkinter.Button(self, text="Add", command=self.add_entry).grid(sticky=Tkinter.W+Tkinter.E, row=6, columnspan=2, padx=5, pady=5)

  def add_entry(self):
    b_score = int(self.f_score.get()) + -int(self.d_score.get())
    input_data = (time.time(),
                  self.num_players.get(),
                  self.type.get(),
                  self.track.get(),
                  self.rank.get(),
                  self.d_score.get(),
                  self.f_score.get(),
                  str(b_score)
                  )
    self.cursor.execute("INSERT INTO mk_data VALUES (?,?,?,?,?,?,?,?)", input_data)
    self.db.commit()



if __name__ == '__main__':
  root = Tkinter.Tk()
  root.title("Mario Kart Tracker")
  MKTracker(root)
  root.mainloop()