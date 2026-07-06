import os
from highrise import BaseBot
from highrise.__main__ import run

class Bot(BaseBot):
    async def on_start(self, session_metadata: dict) -> None:
        print("Bot is online!")

if __name__ == "__main__":
    token = os.getenv("BOT_TOKEN")
    room_id = os.getenv("ROOM_ID")
    run(Bot(), room_id, token)