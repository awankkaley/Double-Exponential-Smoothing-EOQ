try:
    import Tkinter
    import ttk
    import pandas as pd
except ImportError:  # Python 3
    import tkinter as Tkinter
    import tkinter.ttk as ttk

from reference import UbahBulan


class TabelPenjualan(Tkinter.Frame):

    def __init__(self, parent):
        '''
        Constructor
        '''
        Tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_user_interface()

    def initialize_user_interface(self):
        self.parent.title("Penjualan")
        self.parent.config(background="lavender")

        # Set the treeview
        self.tree = ttk.Treeview(self.parent,
                                 columns=('Periode', 'Quantity'))
        self.tree.heading('#0', text='Item')
        self.tree.heading('#1', text='Periode')
        self.tree.heading('#2', text='Quantity')
        self.tree.column('#1', width = 90)
        self.tree.column('#2', stretch=Tkinter.YES,width = 90,anchor = 'center')
        self.tree.column('#0', stretch=Tkinter.YES,width = 50)
        self.tree.grid(row=4, columnspan=4, sticky='nsew')
        self.treeview = self.tree
        # Initialize the counter
        self.i = 1

    def insert_data(self,data):
        for n in range(0, len(data)):
            self.treeview.insert('', 'end', text=str(self.i),
                                 values=(UbahBulan.ubah(str(data.Bulan[n])),
                                         data.Penjualan[n]))
            # Increment counter
            self.i = self.i + 1

def main(data):
    root = Tkinter.Tk()
    d = TabelPenjualan(root)
    d.insert_data(data)
    root.mainloop()

