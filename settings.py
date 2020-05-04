import os

DB = {
    "drivername": "postgres",
    "host": os.environ.get("DB_HOST"),
    "port": os.environ.get("DB_PORT"),
    "username": os.environ.get("DB_USERNAME"),
    "password": os.environ.get("DB_PASSWORD"),
    "database": os.environ.get("DB_DBNAME"),
}
