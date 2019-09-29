import pandas as pd
import numpy as np
import statistics



# PERAMALAN CODE
def peramalan(data, alpha):
    xt = data.Penjualan
    p1 = [xt[0]]
    for n in range(1, len(xt)):
        p1.append(float((alpha * xt[n]) + ((1 - alpha) * p1[n - 1])))
    p2 = [xt[0]]
    for n in range(1, len(xt)):
        p2.append(float(alpha * p1[n] + (1 - alpha) * p2[n - 1]))
    at = [xt[0]]
    for n in range(1, len(p1)):
        at.append((float(2 * p1[n]) - p2[n]))
    bt = [0]
    for n in range(1, len(p1)):
        bt.append(float((alpha / (1 - alpha)) * (p1[n] - p2[n])))
    hasil = [0]
    for n in range(1, len(at)):
        hasil.append(float(at[n-1] + bt[n-1]))
    return hasil

# PERAMALAN Pertama
def peramalanPertama(data, alpha):
    xt = data.Penjualan
    p1 = [xt[0]]
    for n in range(1, len(xt)):
        p1.append(float(alpha * xt[n] + (1 - alpha) * p1[n - 1]))
    p2 = [xt[0]]
    for n in range(1, len(xt)):
        p2.append(float(alpha * p1[n] + (1 - alpha) * p2[n - 1]))
    at = [xt[0]]
    for n in range(1, len(p1)):
        at.append((float(2 * p1[n]) - p2[n]))
    bt = [0]
    for n in range(1, len(p1)):
        bt.append(float((alpha / (1 - alpha)) * (p1[n] - p2[n])))
    hasil = [0]
    for n in range(1, len(at)+1):
        hasil.append(float(at[n-1] + bt[n-1]))
    return hasil[len(hasil)-1]

# HITUNG MAPE
def PE(data, alpha):
    xt = data.Penjualan.values.tolist()
    ft = peramalan(data, alpha)
    pe = [0.00]
    for n in range(1, len(ft)):
        pe.append(float(abs((xt[n] - ft[n]) / xt[n]) * 100))
    return pe

def cariMAPE(data):
    alpha = 0.0000
    datajadi = float(statistics.mean(PE(data, 0.1)))
    for n in np.arange(0.1, 1, 0.1):
        hasil = float(statistics.mean(PE(data, n)))
        if hasil < datajadi:
            alpha = n
            datajadi = hasil  # overidedataPE
    return alpha

def daftarMAPE(data):
    hasil = []
    alpha = []
    daftar = {'Alpha':alpha,
        'Hasil':hasil}
    datajadi = statistics.mean(PE(data, 0.1))
    for n in np.arange(0.1, 1, 0.1):
        hasil.append(float(statistics.mean(PE(data, n))))
        alpha.append(n)
    dfmape = pd.DataFrame(daftar)
    return dfmape


# xt = data.Penjualan.values.tolist()
# ft = peramalan(data, cariMAPE(data))
# pe = PE(data, cariMAPE(data))
# hasilperamalan = peramalanPertama(data,cariMAPE(data))
# listpe = daftarMAPE(data)
#
# frameramalan = [xt, ft]
# dataSetRamalan = pd.DataFrame(frameramalan)

#
# cetakmape = cetakListMape(listpe.Hasil,listpe.Alpha)
# cetakpenjualan = cetakGrafikPenjualan(data)
# cetakramalan = cetakGrafikRamalan(data,ft)
