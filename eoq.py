from Peramalan import peramalanPertama,cariMAPE,d
import pandas as pd
import math
import statistics as st

# dataeoq = pd.read_excel(r'D:\AWANK FILE\SKRIPSI\Master Skripsi\EOQ.xlsx')
dataeoq = pd.read_excel(r'/Users/macbookpro/Desktop/EOQ.xlsx')

D = round(peramalanPertama(data,cariMAPE(data))) #Permintaan
S = 300000 #ongkir
biayaduang = 0.1
harikerja = 26
leadtime = 7

MOQ = dataeoq.MOQ.values.tolist()
harga = dataeoq.Harga.values.tolist()

def replaceeoq():
    EOQAWAL = math.sqrt((2 * D * S) / (harga[0] * biayaduang))
    hasil = [round(EOQAWAL)]
    for n in range(1,len(MOQ)):
        hasil.append(MOQ[n])
    return hasil
EOQ = replaceeoq()

def cariTAC():
    TAC = []
    for n in range(0,len(EOQ)):
        hitung = (((D/EOQ[n])*S)+((EOQ[n]/2)*(harga[n]*biayaduang))+(D*harga[n]))
        TAC.append(round(hitung))
    return TAC
TAC = cariTAC()

def cariEOQ():
    TAC1 = TAC[0]
    for n in range(1,len(TAC)):
        hitung = TAC[n]
        if hitung < TAC1:
            TAC1 = hitung
    return MOQ[TAC.index(TAC1)]
EOQOPTIMAL = cariEOQ()
# set = {'EOQ':EOQ,'TAC':TAC}
# dataSet = pd.DataFrame(set)

penggunaanharian = round(D/harikerja)
penggunaanleadtime = penggunaanharian*leadtime
frekuensi = D/EOQOPTIMAL
jarakreorder = harikerja/frekuensi
rop = st.mean(data.Penjualan)+penggunaanleadtime

print(D)