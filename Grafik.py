import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# DATA PENJUALAN
def cetakGrafikPenjualan(bulan,penjualan):
    plt.plot(bulan, penjualan)
    plt.scatter(bulan, penjualan)
    plt.ylabel('Periode')
    plt.xlabel('Qty')
    plt.show()


# PERBANDINGAN XT FT
def cetakGrafikRamalan(bulan,penjualan, ft):
    plt.plot(bulan, penjualan)
    plt.plot(bulan, ft)
    plt.scatter(bulan, penjualan)
    plt.scatter(bulan, ft)
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
