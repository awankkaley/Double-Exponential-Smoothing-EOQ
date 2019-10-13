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
from reference.Grafik import cetakGrafikRamalan, cetakGrafikPenjualan, cetakListMape
from reference import TabelRamalan, TabelMape, TabelPenjualan, IncrementBulan, Peramalan as u
import History
import LihatData
import Database


class Ramalan(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        master = Frame(self)
        master.pack(fill=BOTH, expand=True)


        self.judul = Label(master, text="IMPORT DATA", font="Helvetica 16 bold")
        self.judul.grid(row=0, column=1, columnspan=4, ipady=15)
        self._separator = ttk.Separator(master, orient="horizontal")
        self._separator.grid(row=1, column=0, columnspan=4, sticky="we")
        self.label1 = Label(master, text="Pilih File: ", anchor=E, justify=RIGHT, pady=10)
        self.chooseFile = Button(master, text="Browse", command=self.pilih_file)
        self.label1.grid(row=2, column=1, ipadx=20)
        self.chooseFile.grid(row=2, column=2, ipadx=20)
        self.txt = Label(master, text="*.xlxx", anchor=W)
        self.txt.grid(row=2, column=3, ipadx=20)
        self.adaFile = Label(master, text="File belum ada")
        self.adaFile.grid(row=3, column=1, columnspan=4)
        self._separator = ttk.Separator(master, orient="horizontal")
        self._separator.grid(row=4, column=0, columnspan=4, sticky="we")

        self.tableSales = Button(master, text="Grafik Penjualan", command=self.grafik_penjualan)
        self.tableSales.grid(row=5, column=1, padx=10, ipadx=10, pady=15)
        self.tableForecast = Button(master, text="Grafik Peramalan", command=self.grafik_ramalan)
        self.tableForecast.grid(row=5, column=2, ipadx=10)
        self.tableMape = Button(master, text="Grafik MAPE", command=self.grafik_mape)
        self.tableMape.grid(row=5, column=3, ipadx=10, padx=10)

        self.lineGraph = Button(master, text="Tabel Penjualan", command=self.tabel_penjualan)
        self.lineGraph.grid(row=6, column=1, ipadx=10)
        self.graph_forecast = Button(master, text="Tabel Ramalan", command=self.tabel_ramalan)
        self.graph_forecast.grid(row=6, column=2, ipadx=15)
        self.graph_mape = Button(master, text="Tabel MAPE", command=self.tabel_mape)
        self.graph_mape.grid(row=6, column=3, ipadx=10, padx=10)

        self.labelAlpha = Label(master, text="Alpha Optimal: -", justify=LEFT, anchor=E)
        self.labelAlpha.grid(row=7, column=1, pady=10)
        self.labelMape = Label(master, text="Nilai MAPE: -", justify=LEFT, anchor=E)
        self.labelMape.grid(row=7, column=2)

        self.labelData = Label(master, text="Data Testing: -", justify=LEFT, anchor=E)
        self.labelData.grid(row=8, column=1)
        self.labelHasil = Label(master, text="Hasil Ramalan: -", justify=LEFT, anchor=E)
        self.labelHasil.grid(row=8, column=2)

        self.graph_mape = Button(master, text="SIMPAN", bg='green', command=lambda: self.simpan_data(controller))
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
        self.labelHasil["text"] = "Hasil : " + str(
            round(u.peramalanPertama(hasil, u.cariMAPE(hasil))))
        self.labelMape["text"] = "MAPE : " + str(round(statistics.mean(u.PE(hasil, u.cariMAPE(hasil))), 2))
        self.labelData["text"] = "Data Uji : " + str(len(hasil))
        print(hasil.Harga.dropna())

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

    def simpan_data(self, controller):
        if self.adaFile["text"] == "File belum ada":
            tkMessageBox.showerror("Perhatian", "Harap Masukan Data Anda  !")
        else:
            hasil = pd.read_excel(self.path)
            Database.POSTDATA(self.path, hasil.Barang[1])
            controller.show_frame(History.History)



