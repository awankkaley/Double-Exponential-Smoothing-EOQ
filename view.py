from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import matplotlib
# from Tkinter import
import pandas as pd

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import uji as u


x = []
y = []
z = []


class Plot:
    def __init__(self, master):
        self.master = master
        self.master.title("Optimasi dengan EOQ")
        self.master.minsize(200, 100)

        self.judul = Label(self.master, text="Peramalan DES", )
        self.judul.grid(row=0, column=1)
        self.label1 = Label(self.master, text="Pilih File: ", anchor=E, justify=RIGHT)
        self.chooseFile = Button(self.master, text="Browse", command=self.choose_file)
        self.label1.grid(row=1, column=0, ipadx=25)
        self.chooseFile.grid(row=1, column=1, ipadx=20)
        self.txt = Label(self.master, text="*.xlxx", anchor=W, justify=LEFT)
        self.txt.grid(row=1, column=2, ipadx=25)

        self.keterangan = Label(self.master, text="Ubah ke:")
        self.keterangan.grid(row=2, column=1)

        self.lineGraph = Button(self.master, text="Grafik Penjualan", command=self.line_Graph)
        self.lineGraph.grid(row=3, column=0, ipadx=15)
        self.graph_forecast = Button(self.master, text="Grafik Peramalan", command=self.graph_forecast)
        self.graph_forecast.grid(row=3, column=1, ipadx=15)

        self.adaFile = Label(self.master, text="File belum ada")
        self.adaFile.grid(row=4, column=1)

    def choose_file(self):
        file_name = tkFileDialog.askopenfilename()
        if not file_name:
            return
        hasil = pd.read_excel(file_name)
        dataBulan = hasil.Bulan
        dataPenjualan = hasil.Penjualan
        x.append(dataBulan)
        y.append(dataPenjualan)
        z.append(u.ft)
        self.adaFile["text"] = file_name

    def line_Graph(self):
        plt.figure(num='Grafik Data Penjualan')
        plt.scatter(x, y)
        plt.xlabel("Bulan")
        plt.ylabel("Jumlah")
        plt.show()

    def graph_forecast(self):
        plt.figure(num='Grafik Uji Peramalan')
        plt.scatter(x,y)
        plt.scatter(x,z)
        plt.legend(['penjualan', 'ramalan'])
        plt.ylabel('Periode')
        plt.xlabel('Qty')
        plt.show()

def main():
    root_window = Tk()
    program = Plot(root_window)
    root_window.mainloop()



if __name__ == '__main__':
    main()
