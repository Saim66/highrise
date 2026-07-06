import os
from highrise import BaseBot
from highrise.__main__ import run

class Bot(BaseBot):
    async def on_start(self, session_metadata: dict) -> None:
        print("Bot is successfully connected!")

if __name__ == "__main__":
    # We use the raw SDK run function that is guaranteed to exist
    run(Bot, os.getenv("ROOM_ID"), os.getenv("BOT_TOKEN"))