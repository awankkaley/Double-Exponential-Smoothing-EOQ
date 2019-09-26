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
import TabelDetailEOQ

class Plot:
    path = ''
    dataEOQ = []
    dataTAC = []


    def __init__(self, master, data, peramalan):
        self.ttk = ttk
        self.master = master
        self.master.title("Economic Order Quantity")
        # self.master.minsize(550, 280)
        # self.master.maxsize(550, 280)

        self.judul = Label(self.master, text="ECONOMIC ORDER QUANTITY", font="Helvetica 16 bold")
        self.judul.grid(row=0, column=0, columnspan=4, ipady=15)
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
        self.harikerja = Entry(self.master, textvariable=self.harikerja_id, width=10)
        self.harikerja.grid(row=5, column=3, padx=20)

        self.labelleadtime = Label(self.master, text="Lead Time (Hari) : ", anchor=E, justify=LEFT)
        self.labelleadtime.grid(row=6, column=2)
        self.leadtime_id = StringVar()
        self.leadtime = Entry(self.master, textvariable=self.leadtime_id, width=10)
        self.leadtime.grid(row=6, column=3)

        self.tombol_proses = Button(self.master, text="Proses", command=lambda: self.proses(data, peramalan),
                                    bg='green',
                                    width='10')
        self.tombol_proses.grid(row=7, column=3)

        self._separator = ttk.Separator(self.master, orient="horizontal")
        self._separator.grid(row=8, column=0, columnspan=4, sticky="we", pady=10)

        self.judulhasil = Label(self.master, text="HASIL", font="Helvetica 11 bold")
        self.judulhasil.grid(row=9, column=0, columnspan=4)

        self.detaileoq = Label(self.master, text="Detail EOQ/TAC : ", anchor=E, justify=LEFT)
        self.detaileoq.grid(row=10, column=0)
        self.tombol_lihat = Button(self.master, text="Lihat", command=self.lihatdetaileoq,
                                   width='10')
        self.tombol_lihat.grid(row=10, column=1)

        self.judul_eoqoptimal = Label(self.master, text="EOQ Optimal : ", anchor=E, justify=LEFT)
        self.judul_eoqoptimal.grid(row=11, column=0)
        self.hasil_eoqoptimal = Label(self.master, text="-", anchor=E, justify=LEFT)
        self.hasil_eoqoptimal.grid(row=11, column=1)

        self.judul_penggunaanharian = Label(self.master, text="Penggunaan/hari : ", anchor=E, justify=LEFT)
        self.judul_penggunaanharian.grid(row=12, column=0)
        self.hasil_penggunaanharian = Label(self.master, text="-", anchor=E, justify=LEFT)
        self.hasil_penggunaanharian.grid(row=12, column=1)

        self.judul_penggunaanleadtime = Label(self.master, text="Penggunaan/leadtime : ", anchor=E, justify=LEFT)
        self.judul_penggunaanleadtime.grid(row=13, column=0)
        self.hasil_penggunaanleadtime = Label(self.master, text="-", anchor=E, justify=LEFT)
        self.hasil_penggunaanleadtime.grid(row=13, column=1)

        self.judul_frekuensi = Label(self.master, text="Frekuensi : ", anchor=E, justify=LEFT)
        self.judul_frekuensi.grid(row=10, column=2)
        self.hasil_frekuensi = Label(self.master, text="-", anchor=E, justify=LEFT)
        self.hasil_frekuensi.grid(row=10, column=3)

        self.judul_jarak = Label(self.master, text="Jarak Order (hari) : ", anchor=E, justify=LEFT)
        self.judul_jarak.grid(row=11, column=2)
        self.hasil_jarak = Label(self.master, text="-", anchor=E, justify=LEFT)
        self.hasil_jarak.grid(row=11, column=3)

        self.judul_rop = Label(self.master, text="Reorder Point : ", anchor=E, justify=LEFT)
        self.judul_rop.grid(row=12, column=2)
        self.hasil_rop = Label(self.master, text="-", anchor=E, justify=LEFT)
        self.hasil_rop.grid(row=12, column=3)


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
                hasil = [round(EOQAWAL)]
                self.dataEOQ.append(round(EOQAWAL))
                for n in range(1, len(MOQ)):
                    hasil.append(MOQ[n])
                    self.dataEOQ.append(MOQ[n])
                return hasil

            def cariTAC():
                TAC = []
                for n in range(0, len(eoq_awal())):
                    hitung = ((dataku / eoq_awal()[n]) * int(self.ongkir.get()) + (
                            (eoq_awal()[n] / 2) * (harga[n] * float(self.gudang.get()))) + (dataku * harga[n]))
                    TAC.append(round(hitung))
                    self.dataTAC.append(round(hitung))
                return TAC

            def cariEOQ():
                TAC1 = cariTAC()[0]
                for n in range(1, len(cariTAC())):
                    hitung = cariTAC()[n]
                    if hitung < TAC1:
                        TAC1 = hitung
                return MOQ[cariTAC().index(TAC1)]

            penggunaanharian = round(dataku / int(self.harikerja.get()))
            penggunaanleadtime = round(penggunaanharian * int(self.leadtime.get()))
            frekuensi = round(dataku / cariEOQ())
            jarakreorder = round(int(self.harikerja.get()) / frekuensi)
            rop = round(statistics.mean(peramalan.Penjualan) + penggunaanleadtime)

            self.hasil_eoqoptimal["text"] = cariEOQ()
            self.hasil_penggunaanharian["text"] = penggunaanharian
            self.hasil_penggunaanleadtime["text"] = penggunaanleadtime
            self.hasil_frekuensi["text"] = frekuensi
            self.hasil_jarak["text"] = jarakreorder
            self.hasil_rop["text"] = rop

    def lihatdetaileoq(self):
        hasil = pd.read_excel(self.path)
        TabelDetailEOQ.main(self.dataEOQ,hasil.Harga,self.dataTAC)


def main(data, peramalan):
    root_window = Tk()
    program = Plot(root_window, data, peramalan)
    root_window.mainloop()



