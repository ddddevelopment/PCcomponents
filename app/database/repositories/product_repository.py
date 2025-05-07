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


def get_product_by_id(product_id: int) -> dict | None:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT id, name, price, category
        FROM products
        WHERE id = %s
    """, (product_id,))
    product = cursor.fetchone()
    conn.close()
    return product
