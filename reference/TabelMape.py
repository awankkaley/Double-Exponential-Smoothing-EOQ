try:
    import Tkinter
    import ttk
    import pandas as pd
except ImportError:  # Python 3
    import tkinter as Tkinter
    import tkinter.ttk as ttk


class TabelPenjualan(Tkinter.Frame):

    def __init__(self, parent):
        '''
        Constructor
        '''
        Tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_user_interface()

    def initialize_user_interface(self):
        self.parent.title("Tabel MAPE")
        self.parent.config(background="lavender")

        # Set the treeview
        self.tree = ttk.Treeview(self.parent,
                                 columns=('Alpha', 'MAPE'))
        self.tree.heading('#0', text='No')
        self.tree.heading('#1', text='Alpha')
        self.tree.heading('#2', text='MAPE')
        self.tree.column('#0', stretch=Tkinter.YES, width=50)
        self.tree.column('#1', width=90)
        self.tree.column('#2', stretch=Tkinter.YES,width = 90,anchor = 'center')
        self.tree.grid(row=4, columnspan=4, sticky='nsew')
        self.treeview = self.tree
        # Initialize the counter
        self.i = 1

    def insert_data(self, data):
        for n in range(0, len(data)):
            self.treeview.insert('', 'end', text=str(self.i),
                                 values=(round(data.Alpha[n],2),
                                         round(data.Hasil[n],2)))
            # Increment counter
            self.i = self.i + 1


def main(data):
    root = Tkinter.Tk()
    d = TabelPenjualan(root)
    d.insert_data(data)
    root.mainloop()
