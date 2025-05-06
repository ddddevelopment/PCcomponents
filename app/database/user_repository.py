from app.database.db import get_connection

def get_user_by_telegram_id(telegram_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE telegram_id = %s", (telegram_id,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()
    return user

def create_user(telegram_id: int, name: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (telegram_id, name) VALUES (%s, %s)",
        (telegram_id, name)
    )
    conn.commit()

    cursor.close()
    conn.close()
