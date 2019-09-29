try:
    import Tkinter
    import ttk
    import pandas as pd
except ImportError:  # Python 3
    import tkinter as Tkinter
    import tkinter.ttk as ttk

import money

class TabelDetailEoq(Tkinter.Frame):

    def __init__(self, parent):
        '''
        Constructor
        '''
        Tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_user_interface()

    def initialize_user_interface(self):
        self.parent.title("Tabel Detail EOQ")
        self.parent.config(background="lavender")

        # Set the treeview
        self.tree = ttk.Treeview(self.parent,
                                 columns=('EOQ', 'Harga', 'TAC'))
        self.tree.heading('#0', text='No')
        self.tree.heading('#1', text='EOQ')
        self.tree.heading('#2', text='Harga')
        self.tree.heading('#3', text='TAC')
        self.tree.column('#0', stretch=Tkinter.YES, width=50)
        self.tree.column('#1', width=70,anchor='center')
        self.tree.column('#2', stretch=Tkinter.YES, width=90, anchor='center')
        self.tree.column('#3', stretch=Tkinter.YES, width=200, anchor='center')
        self.tree.grid(row=4, columnspan=4, sticky='nsew')
        self.treeview = self.tree
        # Initialize the counter
        self.i = 1

    def insert_data(self, dataEoq,dataHarga,dataTAC):

        for n in range(0, len(dataEoq)):
            self.treeview.insert('', 'end', text=str(self.i),
                                 values=(int(dataEoq[n]),
                                         dataHarga[n],money.Money(dataTAC[n],'IDR')))
            self.i = self.i + 1


def main(dataEoq,dataHarga,dataTAC):
    root = Tkinter.Tk()
    d = TabelDetailEoq(root)
    d.insert_data(dataEoq,dataHarga,dataTAC)
    root.mainloop()
