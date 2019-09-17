from Peramalan import peramalanPertama,cariMAPE,data
import math

D = round(peramalanPertama(data,cariMAPE(data))) #Permintaan
S = 300000 #ongkir
harga1 = 30750 #0>5999
harga2 = 29520 #6000>11999
harga3 = 28700 #12000
biayaduang = 0.1

EOQAWAL = math.sqrt((2*D*S)/(harga1*biayaduang))
EOQDUA = 6000
EOQTIGA = 12000

TAC1 = (((D/EOQAWAL)*S)+((EOQAWAL/2)*(harga1*biayaduang))+(D*harga1))
TAC2 = (((D/EOQDUA)*S)+((EOQDUA/2)*(harga2*biayaduang))+(D*harga2))
TAC3 = (((D/EOQTIGA)*S)+((EOQTIGA/2)*(harga3*biayaduang))+(D*harga3))

print (TAC1,TAC2,TAC3)