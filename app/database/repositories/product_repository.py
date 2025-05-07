from app.database.db import get_connection

def get_all_products() -> list[dict]:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT id, name, price, category
        FROM products
        ORDER BY id
    """)
    products = cursor.fetchall()
    conn.close()
    return products