import pandas as pd
import datetime
import calendar

data = pd.read_excel(r'/Users/macbookpro/Desktop/Penjualan.xlsx')

def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.datetime(year,month,day,0,0,0)

def pecahBulan(ramalan):
    bualanakhir = data.Bulan[len(data.Bulan)-1]
    increment = add_months(bualanakhir,1)
    object = data.append({'Bulan' : increment,'Penjualan':ramalan},1)
    return object

print (pecahBulan(100))