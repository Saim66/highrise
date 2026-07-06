import os
from highrise import BaseBot
from highrise.__main__ import run

class Bot(BaseBot):
    async def on_start(self, session_metadata: dict) -> None:
        print("Bot is connected!")

if __name__ == "__main__":
    # Get your credentials
    token = os.getenv("f258c8b8e7fffeadcc664f19e48de75d9cd9e04568415b2dd61752fc2eb1d7e4")
    room_id = os.getenv("6597b36528f627c4f470784c")
    
    # This is the standard way to run the SDK in 25.1.0
    # The 'run' function handles the connection and Bot instantiation
    run(Bot, room_id, token)