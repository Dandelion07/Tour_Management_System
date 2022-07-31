import sqlite3
import os
import sys


class DatabaseManager:
    connection: sqlite3.Connection = None
    DATABASE_NAME = 'tourDB.db'

    @classmethod
    def get_database_address(cls) -> str:
        dir_path = os.path.join(os.environ['APPDATA'], 'Tour Management System')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        file_path = os.path.join(dir_path, cls.DATABASE_NAME)
        if not os.path.exists(file_path):
            cls.create_raw_database(file_path)
        return file_path

    @classmethod
    def create_raw_database(cls, file_path: str) -> None:
        cls.connection = sqlite3.connect(
                file_path, detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
        )
        cursor = cls.connection.cursor()
        relative_path = 'raw_database.sql'
        try:
            base_path = sys._MEIPASS
        except:
            base_path = os.path.abspath('.')
        abs_path = os.path.join(base_path, relative_path)
        with open(abs_path, 'r', encoding = 'utf8') as sql_raw_database:
            cursor.executescript(sql_raw_database.read())
            cls.connection.commit()

    @classmethod
    def get_connection(cls) -> sqlite3.Connection:
        if cls.connection is None:
            cls.connection = sqlite3.connect(
                    cls.get_database_address(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
            )
            cls.connection.row_factory = sqlite3.Row
        return cls.connection

    @classmethod
    def query(cls, query_string: str, *params: object) -> sqlite3.Cursor:
        cursor = cls.get_connection().cursor()
        cursor.execute(query_string, list(params))
        return cursor

    @classmethod
    def execute(cls, query_string: str, *params: object) -> sqlite3.Cursor:
        cursor = cls.get_connection().cursor()
        cursor.execute(query_string, list(params))
        cls.get_connection().commit()
        return cursor
