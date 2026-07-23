import os

import mysql.connector
from dotenv import load_dotenv
from flask import Flask, jsonify

load_dotenv()

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "127.0.0.1"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER", "app_user"),
        password=os.getenv("MYSQL_PASSWORD", "app_password"),
        database=os.getenv("MYSQL_DATABASE", "hello_world"),
    )


@app.get("/")
def hello_world():
    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT 'MySQL działa!' AS message")
        db_message = cursor.fetchone()[0]

        return jsonify(
            message="Hello, World!",
            database=db_message,
        )
    except mysql.connector.Error as error:
        return jsonify(error="Nie udało się połączyć z MySQL", details=str(error)), 500
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()


@app.get("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("FLASK_PORT", "5000")), debug=True)
