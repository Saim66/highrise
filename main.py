import os
from highrise.__main__ import main
import sys

if __name__ == "__main__":
    # We feed the arguments as if they were typed into the terminal
    token = os.getenv("BOT_TOKEN")
    room_id = os.getenv("ROOM_ID")
    
    # We are manually setting the arguments the SDK expects
    sys.argv = ["highrise", "main:Bot", room_id, token]
    
    # This calls the internal SDK entry point directly
    main()