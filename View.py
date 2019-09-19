# from Tkinter import *
# import Tkinter, Tkconstants, tkFileDialog
from tkinter import *
from tkinter import filedialog, messagebox

import matplotlib
# from Tkinter import
import pandas as pd

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import Peramalan as u
from Grafik import cetakGrafikRamalan,cetakGrafikPenjualan


x = [] #Bulan
y = [] #Penjualan
z = [] #PE


class Plot:
    def __init__(self, master):
        self.master = master
        self.master.title("Wirawan 065113459")
        self.master.minsize(600, 280)
        self.master.maxsize(600,280)

        self.judul = Label(self.master, text="DOUBLE EXPONENTIAL SMOOTHING", font="Helvetica 16 bold")
        self.judul.grid(row=0, column=1, columnspan = 4, ipady = 15)
        self.label1 = Label(self.master, text="Pilih File: ", anchor=E, justify=RIGHT)
        self.chooseFile = Button(self.master, text="Browse",command=self.pilih_file)
        self.label1.grid(row=2, column=1, ipadx=20)
        self.chooseFile.grid(row=2, column=2,ipadx=20)
        self.txt = Label(self.master, text="*.xlxx", anchor=W)
        self.txt.grid(row=2, column=3, ipadx=20)
        self.adaFile = Label(self.master, text="File belum ada")
        self.adaFile.grid(row=3, column=1, columnspan = 4)

        self.tableSales = Button(self.master, text="Grafik Penjualan", command=self.grafik_penjualan)
        self.tableSales.grid(row=4, column=0, padx=10, ipadx=10, pady=15)
        self.tableForecast = Button(self.master, text="Grafik Peramalan", command=self.grafik_ramalan)
        self.tableForecast.grid(row=4, column=1, ipadx=10)
        self.tableMape = Button(self.master, text="Grafik MAPE", command=self.grafik_ramalan)
        self.tableMape.grid(row=4, column=2, ipadx=10)

        self.lineGraph = Button(self.master, text="Tabel Penjualan", command=self.grafik_penjualan)
        self.lineGraph.grid(row=5, column=0, ipadx=10)
        self.graph_forecast = Button(self.master, text="Tabel Ramalan", command=self.grafik_ramalan)
        self.graph_forecast.grid(row=5, column=1, ipadx=15)
        self.graph_mape = Button(self.master, text="Tabel MAPE", command=self.grafik_ramalan)
        self.graph_mape.grid(row=5, column=2, ipadx=10)

        self.graph_mape = Button(self.master, text="HITUNG EOQ", command=self.grafik_ramalan)
        self.graph_mape.grid(row=4, column=3,columnspan=3,rowspan=2, ipadx=10,ipady=25)



    def pilih_file(self):
        # file_name = tkFileDialog.askopenfilename()
        file_name = filedialog.askopenfilename()
        if not file_name:
            return
        hasil = pd.read_excel(file_name)
        dataBulan = hasil.Bulan
        dataPenjualan = hasil.Penjualan
        x.append(dataBulan)
        y.append(dataPenjualan)
        z.append(u.ft)
        self.adaFile["text"] = file_name

    def grafik_penjualan(self):
        if self.adaFile["text"] == "File belum ada":
            messagebox.showerror("Perhatian","Harap Masukan Data Anda  !")
        else:
            cetakGrafikPenjualan(x,y)

    def grafik_ramalan(self):
        if self.adaFile["text"] == "File belum ada":
            messagebox.showerror("Perhatian","Harap Masukan Data Anda  !")
        else:
            cetakGrafikRamalan(x,y,z)

def main():
    root_window = Tk()
    program = Plot(root_window)
    root_window.mainloop()

if __name__ == '__main__':
    main()
