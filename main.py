import os
from highrise import BaseBot, Highrise
import asyncio

class Bot(BaseBot):
    async def on_start(self, session_metadata: dict) -> None:
        print("Bot is connected!")

async def main():
    token = os.getenv("BOT_TOKEN")
    room_id = os.getenv("ROOM_ID")
    
    bot = Bot()
    # Connect manually
    await Highrise(room_id, token).run(bot)

if __name__ == "__main__":
    asyncio.run(main())