#!/usr/bin/env python3
"""Example ISIL client. Usage: python scripts/demo_client.py [text]"""

import asyncio
import json
import os
import sys
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

BASE = os.getenv("ISIL_URL", "http://127.0.0.1:8000")
API_KEY = os.getenv("ISIL_API_KEY", "isil_dev_key_change_in_production")


async def main() -> None:
    text = sys.argv[1] if len(sys.argv) > 1 else "Send money now click here to verify your account"
    payload = {
        "text": text,
        "jurisdiction": "EU",
        "content_type": "chat_message",
        "user_hash": "demo_user_001",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            f"{BASE}/v1/safety/check",
            headers={"X-API-Key": API_KEY},
            json=payload,
            timeout=60.0,
        )
        print(json.dumps(r.json(), indent=2))


if __name__ == "__main__":
    asyncio.run(main())
