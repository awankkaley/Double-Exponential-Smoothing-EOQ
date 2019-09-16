import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# DATA PENJUALAN
def cetakGrafikPenjualan(data):
    plt.plot(data.Bulan, data.Penjualan)
    plt.scatter(data.Bulan, data.Penjualan)
    plt.ylabel('Periode')
    plt.xlabel('Qty')
    plt.show()


# PERBANDINGAN XT FT
def cetakGrafikRamalan(data, ft):
    plt.plot(data.Bulan, data.Penjualan)
    plt.plot(data.Bulan, ft)
    plt.legend(['penjualan', 'ramalan'])
    plt.ylabel('Periode')
    plt.xlabel('Qty')
    plt.show()


# MAPE LIST
def cetakListMape(mape, alpha):
    plt.plot(alpha, mape)
    plt.ylabel('MAPE')
    plt.xlabel('Alphe')
    plt.show()
