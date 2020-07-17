
import mysql.connector

from utils import consts
from utils.utils import init_log

log = init_log()


def select_all(table_name):
    return sql_run(f"SELECT * FROM test_1.{table_name};")


def sql_run(query):
    sql = Sql()
    try:
        if sql.connection.is_connected():
            db_Info = sql.connection.get_server_info()
            log.info(f"Connected to MySQL Server version {db_Info}")
            cursor = sql.connection.cursor()
            cursor.execute(query)
            record = cursor.fetchall()
            log.info(f"You're connected to database")
            return record
    except Exception as e:
        log.error(f"Error while connecting to MySQL {e}")
    finally:
        if sql.connection and (sql.connection.is_connected()):
            cursor.close()
            sql.connection.close()
            log.info(f"MySQL connection is closed")


class Sql:
    connection = None
    
    def __init__(self):
        if Sql.connection is None:
            Sql.connection = \
                mysql.connector.connect(
                    host=consts.HOST,
                    database=consts.DATABASE,
                    user=consts.USER,
                    password=consts.PASSWORD
                )
        elif Sql.connection.is_connected():
            Sql.connection.reconnect()

    