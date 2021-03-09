import discord
from discord.ext import commands
import os
token = os.environ('TOKEN')
client = commands.Bot(command_prefix='>',intents=discord.Intents.all(),help_command=None)

@client.event
async def on_ready():
    print('Bot is ready')


extensions = ["cipherdecode",'cipherencode','otherciphertools']

if __name__ == "__main__":
    for ext in extensions:
        client.load_extension(ext)

client.run(token)
