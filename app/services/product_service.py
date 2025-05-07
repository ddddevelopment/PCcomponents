import asyncio

from app.database.repositories import product_repository


async def get_products() -> list[dict]:
    return await asyncio.to_thread(product_repository.get_all_products)