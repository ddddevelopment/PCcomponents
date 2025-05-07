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