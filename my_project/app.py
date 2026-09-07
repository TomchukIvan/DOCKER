import os
import time
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "db")
DB_NAME = os.environ.get("POSTGRES_DB", "mydb")
DB_USER = os.environ.get("POSTGRES_USER", "myuser")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "mysecretpassword")


def get_db_connection():
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                port=5432,
            )
            return conn
        except psycopg2.OperationalError:
            retries -= 1
            time.sleep(2)
    raise Exception("Не удалось подключиться к базе данных")


def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS visits (id SERIAL PRIMARY KEY, ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
    )
    conn.commit()
    cur.close()
    conn.close()


@app.route("/")
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    # Записываем новое посещение
    cur.execute("INSERT INTO visits DEFAULT VALUES;")
    conn.commit()

    # Читаем количество посещений
    cur.execute("SELECT COUNT(*) FROM visits;")
    count = cur.fetchone()[0]

    cur.close()
    conn.close()

    return jsonify(
        {
            "message": "Привет! Приложение работает с PostgreSQL.",
            "total_visits": count,
        }
    )


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
