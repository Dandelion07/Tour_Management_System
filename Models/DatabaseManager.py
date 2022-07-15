import pyodbc


class DatabaseManager:
    connection = None
    DRIVER = 'SQL SERVER'
    SERVER = 'localhost'
    DATABASE_NAME = 'tourDB'

    @classmethod
    def get_connection(cls) -> pyodbc.Connection:
        if cls.connection is None:
            cls.connection = pyodbc.connect("Driver={SQL SERVER};"
                                            "Server=localhost;"
                                            "Database=tourDB;"
                                            "Trusted_Connection=yes;")
        return cls.connection

    @classmethod
    def query(cls, query_string: str, *params: [object]) -> pyodbc.Cursor:
        cursor = cls.get_connection().cursor()
        cursor.execute(query_string, params)
        return cursor

    @classmethod
    def execute(cls, query_string: str, *params) -> pyodbc.Cursor:
        cursor = cls.get_connection().cursor()
        cursor.execute(query_string, params)
        cursor.commit()
        return cursor
