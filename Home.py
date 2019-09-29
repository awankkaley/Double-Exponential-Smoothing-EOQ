
try:
    from Tkinter import *
    import Tkinter, Tkconstants, tkFileDialog, tkMessageBox
    import ttk
except ImportError:
    from tkinter import filedialog as tkFileDialog
    from tkinter import messagebox as tkMessageBox
    from tkinter import *
    import tkinter.ttk as ttk

import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import View



class Plot:
    path = ''

    def __init__(self, master):
        self.master = master
        self.master.title("Wirawan 065113459")


        self.judul = Label(self.master, text="DOUBLE EXPONENTIAL SMOOTHING", font="Helvetica 16 bold")
        self.judul.grid(row=0, column=1, columnspan=4, ipady=15)
        self._separator = ttk.Separator(self.master, orient="horizontal")
        self._separator.grid(row=1,column=0,columnspan=4, sticky="we")
        self.label1 = Label(self.master, text="Pilih Data: ", anchor=E, justify=RIGHT,pady=10)
        self.chooseFile = Button(self.master, text="Browse", command=self.pilih_file)
        self.label1.grid(row=2, column=1, ipadx=20)
        self.chooseFile.grid(row=2, column=2, ipadx=20)

        self._separator = ttk.Separator(self.master, orient="horizontal")
        self._separator.grid(row=4,column=0,columnspan=4, sticky="we")

        self.tableSales = Button(self.master, text="GO !", command=self.grafik_penjualan)
        self.tableSales.grid(row=5, column=1, columnspan=4,padx=10, ipadx=10, pady=15)


    def pilih_file(self):
        # file_name = tkFileDialog.askopenfilename()
        file_name = tkFileDialog.askopenfilename()
        if not file_name:
            return
        hasil = pd.read_excel(file_name)
        if len(hasil.Penjualan) < 6:
            tkMessageBox.showerror('Peringatan', 'Data Tidak Mencukupi !')
        self.path = file_name
        self.adaFile["text"] = file_name



    def grafik_penjualan(self):
        View.main()
        View.Tk.destroy()




def main():
    root_window = Tk()
    program = Plot(root_window)
    root_window.mainloop()



if __name__ == '__main__':
    main()
