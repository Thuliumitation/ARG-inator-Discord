import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TOKEN')
client = commands.Bot(command_prefix=commands.when_mentioned_or(">"),intents=discord.Intents.all(),help_command=None)

@client.event
async def on_ready():
    print('Bot is ready')
    
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong: {round(client.latency*1000,1)}')

extensions = ["cipherdecode",'cipherencode','otherciphertools']

if __name__ == "__main__":
    for ext in extensions:
        client.load_extension(ext)
    client.run(token)
