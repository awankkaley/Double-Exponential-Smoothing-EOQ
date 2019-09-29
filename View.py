
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
import statistics
import matplotlib
import IncrementBulan
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import Peramalan as u
from Grafik import cetakGrafikRamalan, cetakGrafikPenjualan, cetakListMape
import TabelPenjualan
import TabelRamalan
import TabelMape
from Vieweoq import main as pindah_eoq


class Plot:
    path = ''

    def __init__(self, master):
        self.master = master
        self.master.title("Wirawan 065113459")
        # self.master.minsize(450, 280)
        # self.master.maxsize(500, 280)

        self.judul = Label(self.master, text="DOUBLE EXPONENTIAL SMOOTHING", font="Helvetica 16 bold")
        self.judul.grid(row=0, column=1, columnspan=4, ipady=15)
        self._separator = ttk.Separator(self.master, orient="horizontal")
        self._separator.grid(row=1,column=0,columnspan=4, sticky="we")
        self.label1 = Label(self.master, text="Pilih File: ", anchor=E, justify=RIGHT,pady=10)
        self.chooseFile = Button(self.master, text="Browse", command=self.pilih_file)
        self.label1.grid(row=2, column=1, ipadx=20)
        self.chooseFile.grid(row=2, column=2, ipadx=20)
        self.txt = Label(self.master, text="*.xlxx", anchor=W)
        self.txt.grid(row=2, column=3, ipadx=20)
        self.adaFile = Label(self.master, text="File belum ada")
        self.adaFile.grid(row=3, column=1, columnspan=4)

        self._separator = ttk.Separator(self.master, orient="horizontal")
        self._separator.grid(row=4,column=0,columnspan=4, sticky="we")

        self.tableSales = Button(self.master, text="Grafik Penjualan", command=self.grafik_penjualan)
        self.tableSales.grid(row=5, column=1, padx=10, ipadx=10, pady=15)
        self.tableForecast = Button(self.master, text="Grafik Peramalan", command=self.grafik_ramalan)
        self.tableForecast.grid(row=5, column=2, ipadx=10)
        self.tableMape = Button(self.master, text="Grafik MAPE", command=self.grafik_mape)
        self.tableMape.grid(row=5, column=3, ipadx=10, padx=10)

        self.lineGraph = Button(self.master, text="Tabel Penjualan", command=self.tabel_penjualan)
        self.lineGraph.grid(row=6, column=1, ipadx=10)
        self.graph_forecast = Button(self.master, text="Tabel Ramalan", command=self.tabel_ramalan)
        self.graph_forecast.grid(row=6, column=2, ipadx=15)
        self.graph_mape = Button(self.master, text="Tabel MAPE", command=self.tabel_mape)
        self.graph_mape.grid(row=6, column=3, ipadx=10, padx=10)

        self.labelAlpha = Label(self.master, text="Alpha Optimal: -", justify=LEFT, anchor=E)
        self.labelAlpha.grid(row=7, column=1, pady=10)
        self.labelMape = Label(self.master, text="Nilai MAPE: -", justify=LEFT, anchor=E)
        self.labelMape.grid(row=7, column=2)

        self.labelData = Label(self.master, text="Data Testing: -", justify=LEFT, anchor=E)
        self.labelData.grid(row=8, column=1)
        self.labelHasil = Label(self.master, text="Hasil Ramalan: -", justify=LEFT, anchor=E)
        self.labelHasil.grid(row=8, column=2)

        self.graph_mape = Button(self.master, text="HITUNG EOQ", command=self.tombol_eoq, bg='green')
        self.graph_mape.grid(row=8, column=3, pady=10)

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
        self.labelAlpha["text"] = 'Alpha : ' + str(u.cariMAPE(hasil))
        self.labelHasil["text"] = str(IncrementBulan.add_months(hasil.Bulan[len(hasil.Bulan) - 1],1)) +" : " + str(round(u.peramalanPertama(hasil, u.cariMAPE(hasil))))
        self.labelMape["text"] = "MAPE : " + str(round(statistics.mean(u.PE(hasil, u.cariMAPE(hasil))),2))
        self.labelData["text"] = "Data Uji : " + str(len(hasil))


    def grafik_penjualan(self):
        if self.adaFile["text"] == "File belum ada":
            tkMessageBox.showerror("Perhatian", "Harap Masukan Data Anda  !")
        else:
            hasil = pd.read_excel(self.path)
            cetakGrafikPenjualan(hasil.Bulan, hasil.Penjualan)

    def grafik_ramalan(self):
        if self.adaFile["text"] == "File belum ada":
            tkMessageBox.showerror("Perhatian", "Harap Masukan Data Anda  !")
        else:
            hasil = pd.read_excel(self.path)
            ramalan = u.peramalan(hasil, u.cariMAPE(hasil))
            cetakGrafikRamalan(hasil.Bulan, hasil.Penjualan, ramalan)

    def grafik_mape(self):
        if self.adaFile["text"] == "File belum ada":
            tkMessageBox.showerror("Perhatian", "Harap Masukan Data Anda  !")
        else:
            hasil = pd.read_excel(self.path)
            cetakListMape(u.daftarMAPE(hasil).Hasil, u.daftarMAPE(hasil).Alpha)

    def tabel_penjualan(self):
        if self.adaFile["text"] == "File belum ada":
            tkMessageBox.showerror("Perhatian", "Harap Masukan Data Anda  !")
        else:
            hasil = pd.read_excel(self.path)
            TabelPenjualan.main(hasil)

    def tabel_ramalan(self):
        if self.adaFile["text"] == "File belum ada":
            tkMessageBox.showerror("Perhatian", "Harap Masukan Data Anda  !")
        else:
            hasil = pd.read_excel(self.path)
            ramalan = u.peramalan(hasil, u.cariMAPE(hasil))
            TabelRamalan.main(hasil, ramalan)

    def tabel_mape(self):
        if self.adaFile["text"] == "File belum ada":
            tkMessageBox.showerror("Perhatian", "Harap Masukan Data Anda  !")
        else:
            hasil = pd.read_excel(self.path)
            daftarmape = u.daftarMAPE(hasil)
            TabelMape.main(daftarmape)

    def tombol_eoq(self):
        if self.adaFile["text"] == "File belum ada":
            tkMessageBox.showerror("Perhatian", "Harap Masukan Data Anda  !")
        else:
            hasil = pd.read_excel(self.path)

            pindah_eoq(u.peramalanPertama(hasil, u.cariMAPE(hasil)),hasil)


def main():
    root_window = Tk()
    program = Plot(root_window)
    root_window.mainloop()


if __name__ == '__main__':
    main()
