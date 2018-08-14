import pymysql

import config.database as dbcfg


# cnx = pymysql.connect(dbcfg.cnx_str)
connection = pymysql.connect(host='localhost',
                      port=3306,
                      user='surginet_user',
                      passwd='$9jcDcTD%7_48>6*j`N&G$>(',
                      db='psp_emory_surginet')


# with cnx.cursor() as cursor:
#     sql = 'SELECT * FROM surginet WHERE `id`= 1'
#     cursor.execute(sql)
#     result = cursor.fetchone()
#     print(result)

        # Read a single record
sql = "SELECT * FROM 'surginet' WHERE `id`=1"
connection.cursor().execute(sql)
result = connection.cursor().fetchone()
print(result)
connection.close

# cnx.close()
#
# cnx = pymysql.connect(dbcfg.cnx_str_admin)
# with cnx.cursor() as cursor:
#     sql = 'SELECT * FROM surginet WHERE `id`= 1'
#     cursor.execute(sql)
#     result = cursor.fetchone()
#     print(result)
# cnx.close()
