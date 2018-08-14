import pymysql
from config.database import MYSQL

import pandas
import xlrd

def main():
    test_pymysql()


def test_pymysql():
    cnx = pymysql.connect(MYSQL.HOST, MYSQL.USER, MYSQL.PASSWD, MYSQL.DB)
    try:
        cursor = cnx.cursor()
        sql = 'SELECT * FROM `surginet` WHERE `id`=%s'
        cursor.execute(sql, (1,))
        result = cursor.fetchone()
        print(result)
    finally:
        cnx.close()

def load_surginet():
    df = pandas.read_excel('')

if __name__ == "__main__":
    main()
