import Tkinter

class MKTracker(Tkinter.Frame):
  def __init__(self, parent):
    Tkinter.Frame.__init__(self, parent)

    self.init_ui()

  def init_ui(self):
    self.pack(fill=Tkinter.BOTH, expand=1)

    self.num_players = Tkinter.StringVar()
    Tkinter.Label(text="Number of Players:").grid(row=0, column=0)


    Tkinter.Label(text="Type:").grid(row=1, column=0)


    Tkinter.Label(text="Track:").grid(row=2, column=0)


    Tkinter.Label(text="Rank:").grid(row=3, column=0)


    Tkinter.Label(text="Delta Score:").grid(row=4, column=0)


    Tkinter.Label(text="Final Score:").grid(row=5, column=0)


if __name__ == '__main__':
  root = Tkinter.Tk()
  root.title("Mario Kart Tracker")
  MKTracker(root)
  root.mainloop()