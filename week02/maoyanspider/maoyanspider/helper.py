import pymysql
import pymysql.cursors
from maoyanspider.items import MaoyanspiderItem


class ConnDB(object):
    conn = None

    def __init__(self, dbInfo):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        if not ConnDB.conn:
            ConnDB.conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                db=self.db
            )

    def insert(self, item: MaoyanspiderItem):
        try:
            with ConnDB.conn.cursor() as cursor:
                sql = "INSERT INTO `t_movies` (`Fmovie_name`, `Fmovie_type`, `Fmovie_date`) VALUES (%s, %s, %s)"
                cursor.execute(
                    sql, (item['movie_name'], item['movie_type'], item['movie_date']))

            ConnDB.conn.commit()
        except Exception as e:
            print(e)
        finally:
            pass # ConnDB.conn.close()

    def select(self, name):
        try:
            with ConnDB.conn.cursor() as cursor:
                # Read a single record
                sql = "SELECT * FROM `t_movies` WHERE `Fmovie_name`=%s"
                cursor.execute(sql, (name,))
                result = cursor.fetchone()
                print(result)
        except Exception as e:
            print(e)
        finally:
            ConnDB.conn.close()
