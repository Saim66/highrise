import os
import asyncio
from highrise import BaseBot
from highrise.__main__ import run

class Bot(BaseBot):
    async def on_start(self, session_metadata: dict) -> None:
        print("Bot is online!")

if __name__ == "__main__":
    # Get your credentials
    token = os.getenv("BOT_TOKEN")
    room_id = os.getenv("ROOM_ID")

    # Use the direct runner which accepts the Bot class and credentials
    # This bypasses the BotDefinition object entirely
    run(Bot(), room_id, token)