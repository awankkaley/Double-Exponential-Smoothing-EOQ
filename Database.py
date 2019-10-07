import requests
import json
import pandas as pd

headers = {
    'content-type': "application/json",
    'x-apikey': "6cb2f59932784a801a4ff10e2a4f15b89c287",
    'cache-control': "no-cache"
}


def POSTPENJUALAN(bulan, penjualan, barang):
    url = "https://skripsiku-e093.restdb.io/rest/penjualan"
    payload = json.dumps({"Bulan": str(bulan), "Penjualan": penjualan, "Barang": barang})
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)


def POSTEOQ(moq, harga, barang):
    url = "https://skripsiku-e093.restdb.io/rest/eoqq"
    payload = json.dumps({"MOQ": moq, "Harga": harga, "Barang": barang})
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)


def POSTBARANG(barang):
    url = "https://skripsiku-e093.restdb.io/rest/barang"
    payload = json.dumps({"Nama": barang})
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)


def GETBARANG():
    url = "https://skripsiku-e093.restdb.io/rest/barang"
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    nama = [item['Nama'] for item in data]

    df = pd.DataFrame(
        {'Nama': nama,
         })
    return df


def GETPENJUALAN(nama):
    url = "https://skripsiku-e093.restdb.io/rest/penjualan"
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    bulan = [item['Bulan'] for item in data]
    penjualan = [item['Penjualan'] for item in data]
    barang = [item['Barang'] for item in data]

    df = pd.DataFrame(
        {'Bulan': bulan, 'Penjualan': penjualan,'Barang':barang})
    data = df.loc[df['Barang'] == nama]
    return data

def GETMOQ(nama):
    url = "https://skripsiku-e093.restdb.io/rest/eoqq"
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    moq = [item['MOQ'] for item in data]
    harga = [item['Harga'] for item in data]
    barang = [item['Barang'] for item in data]

    df = pd.DataFrame(
        {'MOQ': moq, 'Harga': harga, 'Barang': barang})
    data = df.loc[df['Barang'] == nama]
    return data

# print (GETMOQ("YRS23"))
