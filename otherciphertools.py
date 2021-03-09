import discord
from discord.ext import commands
import string
from collections import Counter


class OtherTools(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['h'])
    async def help(self,ctx):
        e = discord.Embed(title="ARG-inator's help desk",color=discord.Color.darker_grey())
        e.add_field(name='Decode', value='`>decode` or `>d`',inline=False)
        e.add_field(name='Encode', value='`>encode` or `>e`',inline=False)
        e.add_field(name='Others', value='`>other` or `>misc` or `o`',inline=False)
        await ctx.send(embed=e)

    @commands.command(aliases=['o'])
    async def other(self, ctx):
        e = discord.Embed(title="Other command",color=discord.Color.green())
        e.add_field(name='Frequency', value='Calculates the frequency of the given text\n`>freq <text>`')
        e.add_field(name='Bi-gram', value='Calculates the Bi-gram of the given text\n`>bi <text>`')
        e.add_field(name='Tri-gram', value='Calculates the Tri-gram of the given text\n`>tri <text>`')
        e.add_field(name='Index of Coincidence',value='Calculates the Index of Coincidence of a given text\n`>ioc <text>`')
        await ctx.send(embed=e)

    @commands.command(aliases=['freq'])
    async def frequency_test(self, ctx, *, text):
        try:
            text = ''.join([s for s in text if s.isalpha()]).lower()
            freq = dict(Counter(text[x] for x in range(len(text) - 1)))
            sort = sorted(freq.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
            e = discord.Embed(title='Frequency Analysis')
            for key, value in sort:
                e.add_field(name=key,
                            value=value)
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't calculate your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @commands.command(aliases=['bi'])
    async def bigram(self,ctx,*,text):
        try:
            text = ''.join([s for s in text if s.isalpha()]).lower()
            bgram = dict(Counter(text[x:x+2] for x in range(len(text) - 1)))
            sort = sorted(bgram.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
            e = discord.Embed(title='Bi-gram Frequency Analysis')
            for key,value in sort:
                e.add_field(name=key,
                            value=value)
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't calculate your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)
    @commands.command(aliases=['tri'])
    async def trigram(self, ctx, *, text):
        try:
            text = ''.join([s for s in text if s.isalpha()]).lower()
            bgram = dict(Counter(text[x:x + 3] for x in range(len(text) - 1)))
            sort = sorted(bgram.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
            e = discord.Embed(title='Tri-gram Frequency Analysis')
            for key, value in sort:
                e.add_field(name=key,
                            value=value)
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't calculate your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @commands.command(aliases=['ioc'])
    async def index_of_coincidence(self,ctx, *, text):
        try:
            text = ''.join([s for s in text if s.isalpha()]).lower()
            freq = dict(Counter(text[x:x] for x in range(len(text) - 1)))
            n = 0.0
            N = 0.0
            for key in freq.keys():
                for i in str(freq.get(key)):
                    n += int(i)
                    N += int(i) * (int(i) - 1)
            try:
                ioc = N / (n * (n - 1))
            except ZeroDivisionError:
                return "Couldn't Detect :/"
            e = discord.Embed(title='Index of Coincidence calculator')
            e.add_field(name='Result:',
                        value=str(ioc))
            e.set_footer(text=f'Requested by {ctx.author}')
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't calculate your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

def setup(client):
    client.add_cog(OtherTools(client))
