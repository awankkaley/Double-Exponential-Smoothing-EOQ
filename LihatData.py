try:
    from Tkinter import *
    import Tkinter, Tkconstants, tkFileDialog, tkMessageBox
    import ttk
except ImportError:
    from tkinter import filedialog as tkFileDialog
    from tkinter import messagebox as tkMessageBox
    from tkinter import *
    import tkinter.ttk as ttk


import History
import Ramalan
import Database


class LhatData(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        master = Frame(self)
        master.pack(fill=BOTH, expand=True)
        menubar = Menu(master)
        controller.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Lihat", command=lambda: controller.show_frame(Ramalan.Ramalan))
        menubar.add_cascade(label="Import", menu=fileMenu)
        hisMenu = Menu(menubar)
        hisMenu.add_command(label="Lihat", command=lambda: controller.show_frame(History.History))
        menubar.add_cascade(label="History", menu=hisMenu)
        lhtMenu = Menu(menubar)
        lhtMenu.add_command(label="Lihat Data", command=lambda: controller.show_frame(LhatData))
        menubar.add_cascade(label="Lihat Data", menu=lhtMenu)

        self.judul = Label(master, text="LIST DATA", font="Helvetica 16 bold")
        self.judul.pack(fill=X, ipady=15)
        self._separator = ttk.Separator(master, orient="horizontal")
        self._separator.pack(fill=X)
        data = Database.GETBARANG()

        for n in range(len(data.Nama)):
            row = data.Nama[n]
            self.frame1 = Frame(master)
            self.frame1.pack(fill=X,anchor="c")
            self.data1 = Label(self.frame1, text=row,width="15")
            self.data1.pack( side=LEFT)

            self.penjualan1 = Button(self.frame1, text="Hapus", width="10", command=lambda: self.tabel_penjualan(row))
            self.penjualan1.pack( side=LEFT)



    def tabel_penjualan(self,data):
        print (data)
        # print (data
