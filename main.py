import asyncio
from highrise import BaseBot
from highrise.__main__ import run

class Bot(BaseBot):
    async def on_start(self, session_metadata: dict) -> None:
        print("Bot is successfully connected!")

if __name__ == "__main__":
    # Hardcode these temporarily to rule out environment variable issues
    token = "f258c8b8e7fffeadcc664f19e48de75d9cd9e04568415b2dd61752fc2eb1d7e4"
    room_id = "6597b36528f627c4f470784c"
    
    run(Bot(), room_id, token)