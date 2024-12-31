import os
from bot import Bot

if __name__ == '__main__':
    # Get the port from the environment variable, default to 5000 if not set
    port = int(os.environ.get('PORT', 5000))

    # Run the bot (no host/port arguments passed)
    Bot().run()
