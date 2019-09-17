from Peramalan import peramalanPertama,cariMAPE,data
import math

D = round(peramalanPertama(data,cariMAPE(data))) #Permintaan
S = 300000 #ongkir
C = 80640 #penyimpanan dalam persen per item

EOQ = math.sqrt((2*D*S)/C)

print (round(EOQ))