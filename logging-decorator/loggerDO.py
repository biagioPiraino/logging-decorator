import psycopg2
from user import User


class LoggerDO:
    def __init__(self, host, port, dbname, user, password):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password

    def __enter__(self):
        self.conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            dbname=self.dbname,
            user=self.user,
            password=self.password
        )
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()

    def LogMethodCall(self, user: User, method_name: str) -> None:
        self.cursor.callproc(
            "log_method_call",
            (method_name, user.username, user.authenticated))
        self.conn.commit()
