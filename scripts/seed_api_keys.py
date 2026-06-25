#!/usr/bin/env python3
"""Seed a development API key. Run from project root: python scripts/seed_api_keys.py"""

import asyncio
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from app.db.models import ApiKey, Base
from app.db.session import get_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


DEV_KEY = "isil_dev_key_change_in_production"
DEV_NAME = "development"


async def main() -> None:
    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    key_hash = hashlib.sha256(DEV_KEY.encode()).hexdigest()

    async with factory() as session:
        from sqlalchemy import select

        existing = await session.execute(
            select(ApiKey).where(ApiKey.key_hash == key_hash)
        )
        if existing.scalar_one_or_none():
            print("Dev API key already exists.")
        else:
            session.add(ApiKey(key_hash=key_hash, name=DEV_NAME, tenant_id=DEV_NAME))
            await session.commit()
            print("Created dev API key.")

    print(f"\n  X-API-Key: {DEV_KEY}\n  Tenant:    {DEV_NAME}\n")
    print("Master key from .env: ISIL_MASTER_API_KEY")


if __name__ == "__main__":
    asyncio.run(main())
