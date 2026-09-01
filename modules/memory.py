import sqlite3
import os


DB_PATH = "memory/conversations.db"


def create_database():
    os.makedirs("memory", exist_ok=True)

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            message TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_message(role, message):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO conversations (role, message) VALUES (?, ?)",
        (role, message)
    )

    connection.commit()
    connection.close()


def get_recent_messages(limit=10):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT role, message
        FROM conversations
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    )

    rows = cursor.fetchall()
    connection.close()

    rows.reverse()

    return [
        {
            "role": role,
            "content": message
        }
        for role, message in rows
    ]