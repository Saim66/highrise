import os
import asyncio
from highrise import BaseBot, Highrise

class Bot(BaseBot):
    async def on_start(self, session_metadata: dict) -> None:
        print("Bot is connected!")

async def main():
    token = os.getenv("BOT_TOKEN")
    room_id = os.getenv("ROOM_ID")
    
    # Use the connection manager directly
    bot = Bot()
    bot.room_id = room_id
    bot.api_key = token
    
    # This uses the underlying connection logic without the 'run' command wrapper
    await bot.run(room_id, token)

if __name__ == "__main__":
    asyncio.run(main())