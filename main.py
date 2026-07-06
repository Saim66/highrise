import asyncio
import os
from highrise import BaseBot
from highrise.__main__ import run

class Bot(BaseBot):
    async def on_start(self, session_metadata: dict) -> None:
        print("Bot is successfully connected!")

if __name__ == "__main__":
    token = os.getenv("BOT_TOKEN")
    room_id = os.getenv("ROOM_ID")
    
    # Change 'Bot()' to 'Bot' (remove the parentheses)
    run(Bot, room_id, token)