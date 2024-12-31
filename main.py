import os
from bot import Bot

if __name__ == '__main__':
    # Get the port from the environment variable, default to 5000 if not set
    port = int(os.environ.get('PORT', 5000))

    # Initialize and run the bot
    app = Bot()
    app.run(host='0.0.0.0', port=port)
