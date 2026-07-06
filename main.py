import os
from highrise import BaseBot, BotDefinition
from highrise.__main__ import main

# Your bot class
class Bot(BaseBot):
    async def on_start(self, session_metadata: dict) -> None:
        print("Bot is successfully connected!")

if __name__ == "__main__":
    # Get your credentials
    token = os.getenv("BOT_TOKEN")
    room_id = os.getenv("ROOM_ID")
    
    # Create the definition object required by the latest SDK
    bot_def = BotDefinition(Bot(), room_id, token)
    
    # Pass the list of definitions to main
    main([bot_def])