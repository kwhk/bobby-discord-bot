import discord
import os
from bot import BobbyBot
import logging
import sys

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True

description = 'If you want to contribute: https://github.com/kwhk/bobby-discord-bot'
activity = discord.Activity(type=discord.ActivityType.listening, name="-help")
bot = BobbyBot(command_prefix='-', intents=intents, activity=activity)

token_file = os.environ.get('API_TOKEN_FILE')
# used for testing purposes
token_env = os.environ.get('API_TOKEN')

if token_file and os.path.exists(token_file):
    print("Using API token file")
    with open(token_file, 'r') as f:
        api_token = f.read().strip()  # .strip() removes newline
        print("TOKEN IS " + api_token)
        bot.run(api_token, log_handler=handler)
elif token_env:
    print(f"Using API token: {token_env}")
    bot.run(token_env, log_handler=handler)
else:
    print("ERROR: API_TOKEN_FILE not set or file not found")
    sys.exit(1)
