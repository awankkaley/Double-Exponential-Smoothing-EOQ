import pandas as pd
import matplotlib
import numpy as np
import statistics
import plotly.graph_objects as go

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

data = pd.read_excel(r'/Users/macbookpro/Desktop/Penjualan.xlsx')
alpha = 0.4

#DATA PENJUALAN
def cetakGrafikPenjualan():
    plt.plot(data.Bulan, data.Penjualan)
    plt.scatter(data.Bulan, data.Penjualan)
    plt.ylabel('Periode')
    plt.xlabel('Qty')
    plt.show()

#PERBANDINGAN XT FT
def dataTest(dataramalan):
    plt.plot(data.Bulan, data.Penjualan)
    plt.plot(data.Bulan, dataramalan)
    plt.legend(['penjualan','ramalan'])
    plt.ylabel('Periode')
    plt.xlabel('Qty')
    plt.show()

#PERAMALAN CODE

def pemulusan1(data):
    hasil = [data[0]]
    for n in range(1, len(data)):
        hasil.append(alpha * data[n] + (1 - alpha) * hasil[n - 1])
    return hasil
def pemulusan2(data):
    hasil = [data[0]]
    for n in range(1, len(data)):
        hasil.append(alpha * data[n] + (1 - alpha) * hasil[n - 1])
    return hasil
def at(p1, p2):
    hasil = [p1[0]]
    for n in range(1, len(p1)):
        hasil.append((2 * p1[n]) - p2[n])
    return hasil
def bt(p1, p2):
    hasil = [p1[0]]
    for n in range(1, len(p1)):
        hasil.append((alpha / (1 - alpha)) * (p1[n] - p2[n]))
    return hasil
def fit(hasilAt, hasilBt):
    hasil = [0,hasilBt[0]]
    for n in range(1, len(hasilAt)):
        hasil.append(hasilAt[n] + hasilBt[n])
    hasil.__delitem__(len(hasil)-1)
    return hasil
hasilAt = at(pemulusan1(data.Penjualan), pemulusan2(pemulusan1(data.Penjualan)))
hasilBt = bt(pemulusan1(data.Penjualan), pemulusan2(pemulusan1(data.Penjualan)))

#MAPE

def MAPE():
    hasil = [0]
    for n in range(1,len(ft)):
        hasil.append(float(abs((xt[n]-ft[n])/xt[n])*100))
    return hasil

#HASILDATA

xt = data.Penjualan.values.tolist()
ft = fit(hasilAt, hasilBt)
mape = MAPE()

collect = [xt,ft]
dataSet = pd.DataFrame(collect)
# dataTest(ft)
# print (dataSet)
