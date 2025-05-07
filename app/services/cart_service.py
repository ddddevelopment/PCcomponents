import asyncio

from app.database.repositories import cart_repository

async def add_to_cart(user_id : int, product_id : int):
    await asyncio.to_thread(cart_repository.add_to_cart,user_id, product_id)