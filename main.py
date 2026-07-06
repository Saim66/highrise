import os
import asyncio
import logging
from highrise import BaseBot, Position, User
from highrise.__main__ import run
from highrise.models import BotDefinition
from commands import CommandHandler
from emotes import EMOTE_LIST

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Bot(BaseBot):
    def __init__(self):
        super().__init__()
        self.cmd = CommandHandler(self)
        self.data_cache = self.cmd.load_data()
        self._api_lock = asyncio.Semaphore(1)

    async def on_start(self, session_metadata):
        self.bot_id = session_metadata.user_id
        logger.info(f"✅ Bot Online in: {session_metadata.room_info.room_name}")
        asyncio.create_task(self.emote_engine())

    async def safe_api_call(self, coro):
        async with self._api_lock:
            try:
                return await coro
            except Exception as e:
                logger.warning(f"API call skipped: {e}")
                return None

    async def emote_engine(self):
        while True:
            if hasattr(self.cmd, 'looping_users') and self.cmd.looping_users:
                for user_id, official_id in list(self.cmd.looping_users.items()):
                    await self.safe_api_call(self.highrise.send_emote(official_id, user_id))
                    await asyncio.sleep(2)
            await asyncio.sleep(1)

    async def on_chat(self, user: User, message: str) -> None:
        await self.cmd.execute(user, message)
        self.data_cache = self.cmd.load_data()

    async def on_user_join(self, user: User, position: Position):
        await asyncio.sleep(2)
        try:
            if user.id in self.data_cache.get("restricted", []):
                await self.safe_api_call(self.highrise.teleport(user.id, Position(0, 0, 0, "FrontLeft")))
                return
            if user.id in self.data_cache.get("vips", []):
                await self.safe_api_call(self.highrise.chat(f"Welcome back, VIP @{user.username}!"))
                return
            welcomes = self.data_cache.get("welcomes", {})
            msg = welcomes.get(user.username.lower())
            if msg:
                await self.safe_api_call(self.highrise.chat(f"@{user.username}, {msg}"))
        except Exception as e:
            logger.error(f"Join logic error: {e}")

    async def on_user_leave(self, user: User) -> None:
        if hasattr(self.cmd, 'looping_users'):
            self.cmd.looping_users.pop(user.id, None)

    async def on_tip(self, sender, receiver, tip):
        await self.cmd.on_tip(sender, receiver, tip)

if __name__ == "__main__":
    import os
    from highrise.__main__ import run

    # Get credentials
    token = os.getenv("BOT_TOKEN")
    room_id = os.getenv("ROOM_ID")
    
    if not token or not room_id:
        print("Missing BOT_TOKEN or ROOM_ID")
        exit(1)
        
    # Instead of manual BotDefinition, let run handle the initialization
    # If this fails with 3 arguments, try removing 'token' here
    run(Bot(), room_id, token)