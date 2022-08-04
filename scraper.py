from datetime import date
import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine
import os
import time


def getDBConf():
    host = "host"
    db = "db"
    user = "user"
    password = "passer"
    with open('config.yml') as file:
        conf = yaml.load(file, Loader=yaml.FullLoader)
        host = conf["hostname"]
        db = conf["dbname"]
        user = conf["username"]
        password = conf["password"]
    return host, db, user, password


def getData():
    # get date
    datex = time.strftime("%x")
    fileDate = "_"
    #  format to "01_01_22"
    fileDate = fileDate.join(datex.split("/"))

    params = getDBConf()
    hostname = params[0]
    dbname = params[1]
    uname = params[2]
    pwd = params[3]
    engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                           .format(host=hostname, db=dbname, user=uname, pw=pwd,  use_unicode=True, charset="utf8"))
    sql = "SELECT * FROM v_source_list_agg"
    print(" ====== Downloading new data ... ")
    data = pd.read_sql(sql, engine)
    data.to_csv("new_sources.csv", index=False)
    data.to_csv("sources_"+fileDate+".csv")
    print(" ====== New data downloaded ! =====")
    return 0

def getSourcesData():
    hostname = os.environ.get("CS_RCCE_HOSTNAME")
    dbname = os.environ.get("CS_RCCE_DBNAME")
    uname = os.environ.get("CS_RCCE_USERNAME")
    pwd = os.environ.get("CS_RCCE_PWD")

    engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                           .format(host=hostname, db=dbname, user=uname, pw=pwd,  use_unicode=True, charset="utf8"))
    sql = "SELECT * FROM v_source_list_agg"
    data = pd.read_sql(sql, engine)
    data.to_csv("social_tracker_data.csv", index=False)
    return 