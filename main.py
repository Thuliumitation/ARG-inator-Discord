import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TOKEN')
client = commands.Bot(command_prefix='>',intents=discord.Intents.all())


@client.event
async def on_ready():
    print('Bot is ready')


extensions = ["cipherdecode",'cipherencode','otherciphertools']

if __name__ == "__main__":
    for ext in extensions:
        client.load_extension(ext)

client.run(token)