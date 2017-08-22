
import psycopg2
import pandas as pd
import numpy as np
import tushare as ts


def conn2pg_db_tb(dbname,tbname):
    dbname = dbname
    tbname = tbname
    sql1 = 'select * from '+ tbname + ' limit 100'
    connpg = psycopg2.connect(host="127.0.0.1",user="postgres",password="root",database=dbname)
    print('数据库连接成功')

    df1 = pd.read_sql(sql1, con=connpg)
    return df1
    connpg.close()

new = conn2pg_db_tb('wuhan','gsm')

def gupiao():
    df = ts.get_hist_data('000875')  # 读取数据，格式为DataFrame
    dftoday = ts.get_today_all()







