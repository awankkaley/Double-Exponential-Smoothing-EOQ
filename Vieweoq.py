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
import math
import statistics


class Plot:
    path = ''

    def __init__(self, master, data,peramalan):
        self.ttk = ttk
        self.master = master
        self.master.title("Economic Order Quantity")
        # self.master.minsize(550, 280)
        # self.master.maxsize(550, 280)

        self.judul = Label(self.master, text="ECONOMIC ORDER QUANTITY", font="Helvetica 16 bold")
        self.judul.grid(row=0, column=0, columnspan=34, ipady=15)
        self._separator = ttk.Separator(self.master, orient="horizontal")
        self._separator.grid(row=1, column=0, columnspan=4, sticky="we")
        self.label1 = Label(self.master, text="Pilih File: ", anchor=CENTER, justify=LEFT)
        self.chooseFile = Button(self.master, text="Browse", command=self.pilih_file)
        self.label1.grid(row=2, column=1, ipadx=20, pady=15)
        self.chooseFile.grid(row=2, column=2, ipadx=20)
        self.txt = Label(self.master, text="*.xlxx", anchor=W)
        self.txt.grid(row=2, column=3, ipadx=20)
        self.adaFile = Label(self.master, text="File belum ada", anchor=W, justify=CENTER)
        self.adaFile.grid(row=3, column=1, columnspan=4)

        self._separator = ttk.Separator(self.master, orient="horizontal")
        self._separator.grid(row=4, column=0, columnspan=4, sticky="we")

        self.labelpermintaan = Label(self.master, text="Permintaan (Qty) : ", anchor=E, justify=LEFT)
        self.labelpermintaan.grid(row=5, column=0)
        self.permintaan = Label(self.master, text=str(round(data)), anchor=E, justify=LEFT)
        self.permintaan.grid(row=5, column=1)

        self.labelongkir = Label(self.master, text="Biaya Pesan (Rp) : ", anchor=E, justify=LEFT)
        self.labelongkir.grid(row=6, column=0)
        self.ongkir_id = StringVar()
        self.ongkir = Entry(self.master, textvariable=self.ongkir_id, width=10)
        self.ongkir.grid(row=6, column=1)

        self.labelgudang = Label(self.master, text="Biaya Gudang (%) : ", anchor=E, justify=LEFT)
        self.labelgudang.grid(row=7, column=0)
        self.gudang_id = StringVar()
        self.gudang = Entry(self.master, textvariable=self.gudang_id, width=10)
        self.gudang.grid(row=7, column=1)

        self.labelharikerja = Label(self.master, text="Hari Kerja (Hari) : ", anchor=E, justify=LEFT)
        self.labelharikerja.grid(row=5, column=2)
        self.harikerja_id = StringVar()
        self.harikerja = Entry(self.master,textvariable=self.harikerja_id, width=10)
        self.harikerja.grid(row=5, column=3, padx=20)

        self.labelleadtime = Label(self.master, text="Lead Time (Hari) : ", anchor=E, justify=LEFT)
        self.labelleadtime.grid(row=6, column=2)
        self.leadtime_id = StringVar()
        self.leadtime = Entry(self.master,textvariable=self.leadtime_id, width=10)
        self.leadtime.grid(row=6, column=3)

        self.tombol_proses = Button(self.master, text="Proses", command=lambda: self.proses(data,peramalan), bg='green',
                                    width='10')
        self.tombol_proses.grid(row=7, column=3)

        self._separator = ttk.Separator(self.master, orient="horizontal")
        self._separator.grid(row=8, column=0, columnspan=4, sticky="we", pady=20)

    def pilih_file(self):
        # file_name = tkFileDialog.askopenfilename()
        file_name = tkFileDialog.askopenfilename()
        if not file_name:
            return
        hasil = pd.read_excel(file_name)
        if len(hasil.MOQ) == 0:
            tkMessageBox.showerror('Peringatan', 'Data Tidak Mencukupi !')
        self.path = file_name
        self.adaFile["text"] = file_name

    def proses(self, data, peramalan):
        dataku = round(data)
        if self.adaFile["text"] == "File belum ada":
            tkMessageBox.showerror("Perhatian", "Belum Ada Data  !")
        else:
            hasil = pd.read_excel(self.path)
            MOQ = hasil.MOQ.values.tolist()
            harga = hasil.Harga.values.tolist()

            def eoq_awal():
                EOQAWAL = math.sqrt((2 * dataku * int(self.ongkir.get())) / (harga[0] * float(self.gudang.get())))
                hasil = [EOQAWAL]
                for n in range(1, len(MOQ)):
                    hasil.append(MOQ[n])
                return hasil

            def cariTAC():
                TAC = []
                for n in range(0, len(eoq_awal())):
                    hitung = ((dataku / eoq_awal()[n]) * int(self.ongkir.get()) + ((eoq_awal()[n] / 2) * (harga[n] * float(self.gudang.get()))) + (dataku * harga[n]))
                    TAC.append(hitung)
                return TAC

            def cariEOQ():
                TAC1 = cariTAC()[0]
                for n in range(1, len(cariTAC())):
                    hitung = cariTAC()[n]
                    if hitung < TAC1:
                        TAC1 = hitung
                return MOQ[cariTAC().index(TAC1)]

            penggunaanharian = round(dataku/int(self.harikerja.get()))
            penggunaanleadtime = round(penggunaanharian*int(self.leadtime.get()))
            frekuensi = round(dataku/cariEOQ())
            jarakreorder = round(int(self.harikerja.get())/frekuensi)
            rop = round(statistics.mean(peramalan.Penjualan)+penggunaanleadtime)

            print (penggunaanharian)
            print (penggunaanleadtime)
            print (frekuensi)
            print (jarakreorder)
            print (rop)


def main(data,peramalan):
    root_window = Tk()
    program = Plot(root_window, data, peramalan)
    root_window.mainloop()
