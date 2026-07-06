import os
import asyncio
from highrise import BaseBot, Highrise

class Bot(BaseBot):
    async def on_start(self, session_metadata: dict) -> None:
        print("Bot is successfully connected!")

async def main():
    token = os.getenv("BOT_TOKEN")
    room_id = os.getenv("ROOM_ID")
    
    # Initialize the bot instance
    bot = Bot()
    
    # Initialize the Highrise connection object
    hr = Highrise()
    
    # Run the bot with the room_id and token passed here
    await hr.run(room_id, token, bot)

if __name__ == "__main__":
    asyncio.run(main())