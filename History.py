
try:
    from Tkinter import *
    import Tkinter, Tkconstants, tkFileDialog, tkMessageBox
    import ttk
except ImportError:
    from tkinter import filedialog as tkFileDialog
    from tkinter import messagebox as tkMessageBox
    from tkinter import *
    import tkinter.ttk as ttk

import statistics
from reference.Grafik import cetakGrafikRamalan, cetakGrafikPenjualan, cetakListMape
from reference import TabelRamalan, TabelMape, TabelPenjualan, IncrementBulan, Peramalan as u
from Optimasi import main as pindah_eoq
import Ramalan
import LihatData
import Database
class History(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        master = Frame(self)
        master.pack(fill=BOTH, expand=True)
        menubar = Menu(master)
        controller.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Import", command=lambda: controller.show_frame(Ramalan.Ramalan))
        menubar.add_cascade(label="Import", menu=fileMenu)
        hisMenu = Menu(menubar)
        hisMenu.add_command(label="History", command=lambda: controller.show_frame(History))
        menubar.add_cascade(label="History", menu=hisMenu)
        lhtMenu = Menu(menubar)
        lhtMenu.add_command(label="Lihat Data", command=lambda: controller.show_frame(LihatData.LhatData))
        menubar.add_cascade(label="Lihat Data", menu=lhtMenu)
        tkvar = StringVar(self)
        if len(Database.GETBARANG().Nama)!= 0:

            choices = Database.GETBARANG().Nama
            tkvar.set("Pilih Data")  # set the default option
            popupMenu = OptionMenu(master, tkvar, *choices)
            popupMenu.grid(row=2, column=2, ipadx=20)

        def change_dropdown(*args):
            self.pilih_file(tkvar.get())
            self.master.update()

        tkvar.trace('w', change_dropdown)
        self.judul = Label(master, text="HISTORY DATA", font="Helvetica 16 bold")
        self.judul.grid(row=0, column=1, columnspan=4, ipady=15)
        self._separator = ttk.Separator(master, orient="horizontal")
        self._separator.grid(row=1, column=0, columnspan=4, sticky="we")
        self.label1 = Label(master, text="Pilih Data: ", anchor=E, justify=RIGHT, pady=10)
        # self.chooseFile = Button(master, text="Browse", command=self.pilih_file)
        self.label1.grid(row=2, column=1, ipadx=20)
        # self.chooseFile.grid(row=2, column=2, ipadx=20)
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

        self.graph_mape = Button(master, text="HITUNG EOQ", command=self.tombol_eoq, bg='green')
        self.graph_mape.grid(row=8, column=3, pady=10)

    def pilih_file(self,file_name):
        if not file_name:
            return
        hasil = Database.GETPENJUALAN(file_name)
        if len(hasil.Penjualan) < 6:
            tkMessageBox.showerror('Peringatan', 'Data Tidak Mencukupi !')
        self.path = file_name
        self.adaFile["text"] = file_name
        self.labelAlpha["text"] = 'Alpha : ' + str(u.cariMAPE(hasil))
        self.labelHasil["text"] = "Hasil : " + str(
            round(u.peramalanPertama(hasil, u.cariMAPE(hasil))))
        self.labelMape["text"] = "MAPE : " + str(round(statistics.mean(u.PE(hasil, u.cariMAPE(hasil))), 2))
        self.labelData["text"] = "Data Uji : " + str(len(hasil))


    def grafik_penjualan(self):
        if self.adaFile["text"] == "File belum ada":
            tkMessageBox.showerror("Perhatian", "Harap Masukan Data Anda  !")
        else:
            hasil = Database.GETPENJUALAN(self.path)
            cetakGrafikPenjualan(hasil.Bulan, hasil.Penjualan)

    def grafik_ramalan(self):
        if self.adaFile["text"] == "File belum ada":
            tkMessageBox.showerror("Perhatian", "Harap Masukan Data Anda  !")
        else:
            hasil = Database.GETPENJUALAN(self.path)
            ramalan = u.peramalan(hasil, u.cariMAPE(hasil))
            cetakGrafikRamalan(hasil.Bulan, hasil.Penjualan, ramalan)

    def grafik_mape(self):
        if self.adaFile["text"] == "File belum ada":
            tkMessageBox.showerror("Perhatian", "Harap Masukan Data Anda  !")
        else:
            hasil = Database.GETPENJUALAN(self.path)
            cetakListMape(u.daftarMAPE(hasil).Hasil, u.daftarMAPE(hasil).Alpha)

    def tabel_penjualan(self):
        if self.adaFile["text"] == "File belum ada":
            tkMessageBox.showerror("Perhatian", "Harap Masukan Data Anda  !")
        else:
            hasil = Database.GETPENJUALAN(self.path)
            TabelPenjualan.main(hasil)

    def tabel_ramalan(self):
        if self.adaFile["text"] == "File belum ada":
            tkMessageBox.showerror("Perhatian", "Harap Masukan Data Anda  !")
        else:
            hasil = Database.GETPENJUALAN(self.path)
            ramalan = u.peramalan(hasil, u.cariMAPE(hasil))
            TabelRamalan.main(hasil, ramalan)

    def tabel_mape(self):
        if self.adaFile["text"] == "File belum ada":
            tkMessageBox.showerror("Perhatian", "Harap Masukan Data Anda  !")
        else:
            hasil = Database.GETPENJUALAN(self.path)
            daftarmape = u.daftarMAPE(hasil)
            TabelMape.main(daftarmape)

    def tombol_eoq(self):
        if self.adaFile["text"] == "File belum ada":
            tkMessageBox.showerror("Perhatian", "Harap Masukan Data Anda  !")
        else:
            hasil = Database.GETPENJUALAN(self.path)
            eoq = Database.GETMOQ(self.path)

            pindah_eoq(u.peramalanPertama(hasil, u.cariMAPE(hasil)), eoq)

