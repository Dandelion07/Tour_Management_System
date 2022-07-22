import sqlite3


class DatabaseManager:
    connection: sqlite3.Connection = None
    DATABASE_NAME = 'tourDB.db'

    @classmethod
    def get_connection(cls) -> sqlite3.Connection:
        if cls.connection is None:
            cls.connection = sqlite3.connect(cls.DATABASE_NAME, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
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
