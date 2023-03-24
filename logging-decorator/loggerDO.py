import psycopg2
import os
from user import User


class LoggerDO:
  def __init__(self):
    self.host     = os.environ.get("HOST")
    self.port     = os.environ.get("PORT")
    self.dbname   = os.environ.get("DB_NAME")
    self.user     = os.environ.get("USER")
    self.password = os.environ.get("PASSWORD")

  def __enter__(self):
    self.conn  = psycopg2.connect(
      host     = self.host,
      port     = self.port,
      dbname   = self.dbname,
      user     = self.user,
      password = self.password
    )
    self.cursor = self.conn.cursor()
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.cursor.close()
    self.conn.close()

  def LogMethodCall(self, method_name: str, user: User) -> None:
    self.cursor.callproc(
        "log_method_call",
        (method_name, user.username, user.authenticated))
    self.conn.commit()
