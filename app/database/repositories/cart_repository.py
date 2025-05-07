from app.database.db import get_connection

def add_to_cart(user_id: int, product_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT quantity FROM cart_items
        WHERE user_id = %s AND product_id = %s
    """, (user_id, product_id))
    result = cursor.fetchone()

    if result:
        cursor.execute("""
            UPDATE cart_items
            SET quantity = quantity + 1
            WHERE user_id = %s AND product_id = %s
        """, (user_id, product_id))
    else:
        cursor.execute("""
            INSERT INTO cart_items (user_id, product_id, quantity)
            VALUES (%s, %s, 1)
        """, (user_id, product_id))

    conn.commit()
    conn.close()


def get_cart_items(user_id: int) -> list[dict]:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT
            p.id AS product_id,
            p.name,
            p.price,
            c.quantity,
            (p.price * c.quantity) AS total_price
        FROM cart_items c
        JOIN products p ON p.id = c.product_id
        WHERE c.user_id = %s
    """, (user_id,))

    items = cursor.fetchall()
    conn.close()
    return items