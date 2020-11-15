#############################################################################
###########               Import python packages
#############################################################################
import pandas as pd
import mysql.connector as MySQLdb
import config

#############################################################################
###########               Import python packages
#############################################################################
def import_data(req, db_name):
    try:
        conn = MySQLdb.connect(user=config.mysql_user, host=config.mysql_host, password=config.mysql_password, db=config.mysql_db)
        print('Connection ok')
    except:
        print("I am unable to connect to the database")
    try:
        cur = conn.cursor()
        cur.execute(req)
        results = cur.fetchall()
    finally:
        conn.close()
    data = pd.DataFrame(list(results), columns=[row[0] for row in cur.description]).reset_index(drop=True)
    return (data)