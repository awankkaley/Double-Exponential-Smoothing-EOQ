import requests
import json
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import datetime

sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/penjualan', pool_recycle=3600)
connection = pymysql.connect('localhost', 'root',
                             '', 'penjualan')
dbConnection = sqlEngine.connect()


def POSTDATA(path, nama):
    test = pd.read_excel(path)
    test.to_sql(name=nama, con=dbConnection, if_exists='append')


def GETLISTDATA():
    df = pd.read_sql("SHOW TABLES", con=dbConnection, )
    return df


def GETDATA(nama):
    df = pd.read_sql("select * from " + nama, con=dbConnection, )
    return df


def HAPUSDATA(nama):
    cursor = connection.cursor()
    sql = "DROP TABLE IF EXISTS {}".format(nama)
    cursor.execute(sql)

# HAPUSDATA("yrs23")