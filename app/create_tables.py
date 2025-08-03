import asyncio
from app.database import engine, Base
from app.models import task  # ensure Task model is imported and registered


async def create_all():
    async with engine.begin() as conn:
        print("Creating tables...")
        await conn.run_sync(Base.metadata.create_all)
        print("Done.")

asyncio.run(create_all())
