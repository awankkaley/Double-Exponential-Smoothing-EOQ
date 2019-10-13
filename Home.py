try:
    from Tkinter import *
    import Tkinter, Tkconstants, tkFileDialog, tkMessageBox
    import ttk
except ImportError:
    from tkinter import filedialog as tkFileDialog
    from tkinter import messagebox as tkMessageBox
    from tkinter import *
    import tkinter.ttk as ttk

from Ramalan import Ramalan
from History import History
from LihatData import LhatData

LARGE_FONT = ("Verdana", 12)


class Utama(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        self.menubar = Menu(container)
        self.config(menu=self.menubar)
        self.title("WIRAWAN PRIMA KALEY")
        self.fileMenu = Menu(self.menubar)
        self.fileMenu.add_command(label="Import Baru", command=lambda: self.show_frame(Ramalan, container))
        self.menubar.add_cascade(label="Import", menu=self.fileMenu)
        self.hisMenu = Menu(self.menubar)
        self.hisMenu.add_command(label="Proses Data", command=lambda: self.show_frame(History, container))
        self.menubar.add_cascade(label="History", menu=self.hisMenu)
        self.lhtMenu = Menu(self.menubar)
        self.lhtMenu.add_command(label="Lihat Data", command=lambda: self.show_frame(LhatData, container))
        self.menubar.add_cascade(label="Lihat Data", menu=self.lhtMenu)
        self.exit = Menu(self.menubar)
        self.exit.add_command(label="Keluar", command=lambda: self.quit())
        self.menubar.add_cascade(label="Keluar", menu=self.exit)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.recycle(container)
        self.show_frame(Ramalan, container)

    def show_frame(self, cont, container):
        self.recycle(container)
        frame = self.frames[cont]
        container.pack(side="top", fill="both", expand=True)
        frame.tkraise()

    def recycle(self, container):
        for F in (Ramalan, History, LhatData):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")



app = Utama()
app.mainloop()
