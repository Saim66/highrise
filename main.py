import os
import sys
from highrise.__main__ import run
# Import your bot class
# Assuming your bot class is named 'Bot' and is in this file
from highrise import BaseBot

class Bot(BaseBot):
    async def on_start(self, session_metadata: dict) -> None:
        print("Bot connected!")

if __name__ == "__main__":
    token = os.getenv("BOT_TOKEN")
    room_id = os.getenv("ROOM_ID")
    
    # Bypass BotDefinition and run directly
    # This is the safest way to avoid the '3 values' error
    run(Bot(), room_id, token)