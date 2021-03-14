import discord
from discord.ext import commands
import base64 as b64
import string
from resources import morse_dict, nato_dict
from InventWithPython import vigenereCipher, transpositionEncrypt
from python_to_bf import brainfrick
import pyconverter
import textwrap


class CipherEncode(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(aliases=['e'])
    async def encode(self, ctx):
        if ctx.invoked_subcommand is None:
            e = discord.Embed(title="Encode command",
                              color=discord.Color.green())
            e.add_field(name="Affine (aff)", value='>encode affine <"text"> <1st key> <2nd key>')
            e.add_field(name="Ascii85 (a85)", value='>encode ascii85 <text>')
            e.add_field(name="Atbash (atb)", value='>encode atbash <text>')
            e.add_field(name="Base32 (b32)", value='>encode base32 <text>')
            e.add_field(name="Base64 (b64)", value='>encode base64 <text>')
            e.add_field(name="Base85 (b85)", value='>encode base85 <text>')
            e.add_field(name="Binary (bin)", value='>encode binary <text>')
            e.add_field(name='Brainfuck (bf)', value='>encode bf <text>')
            e.add_field(name="Caesar (c)", value='>encode caeser <"text"> <key>')
            e.add_field(name="Decimal (dec)", value='>encode dec <text>')
            e.add_field(name="Hexadecimal (hex)", value='>encode hex <text>')
            e.add_field(name="Morse Code (mc)", value='>encode morse <text>')
            e.add_field(name="NATO Phonetic Alphabet (nato)", value='>encode nato <text>')
            e.add_field(name="Octal (oct)", value='>encode oct <text>')
            e.add_field(name="Rot47 (r47)", value='>encode rot47 <text>')
            e.add_field(name="Monoalphabetic Substitution (mono)", value='>encode mono <text>')
            e.add_field(name="Transposition (railfence)", value=">encode rf <'text'> <key>")
            e.add_field(name="Vigenère (v)", value=">encode vigenere <'text'> <'key'>")
            await ctx.send(embed=e)
        else:
            pass

    @encode.command(aliases=['a85'])
    async def ascii85(self, ctx, *, text):
        try:
            result = b64.a85encode(bytes(text, 'utf-8'))
            e = discord.Embed(title='Ascii85 encoder',
                              color=discord.Color.green())
            e.add_field(name="Result",
                        value=result.decode('utf-8'))
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't encode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @encode.command(aliases=['atb'])
    async def atbash(self, ctx, *, text):
        try:
            result = text.translate(str.maketrans(string.ascii_uppercase, string.ascii_uppercase[::-1])) \
                .translate(str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1]))
            e = discord.Embed(title='Atbash Cipher encoder',
                              color=discord.Color.green())
            e.add_field(name='Result',
                        value=result)
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't encode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @encode.command(aliases=['aff'])
    async def affine(self, ctx, text, k1: int, k2: int):
        try:
            result = ''
            for char in text:
                if char.isupper():
                    result += chr(((k1 * (ord(char) - 65 + k2) % 26) + 65))
                elif char.islower():
                    result += chr(((k1 * (ord(char) - 97 + k2) % 26) + 97))
                else:
                    result += char
            e = discord.Embed(title='Affine Cipher encoder',
                              color=discord.Color.green())
            e.add_field(name='Result:',
                        value=result)
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't encode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @encode.command(aliases=['b32'])
    async def base32(self, ctx, *, text):
        try:
            result = b64.b32encode(bytes(text, 'utf-8'))
            e = discord.Embed(title='Base32 encoder',
                              color=discord.Color.green())
            e.add_field(name='Result:',
                        value=result.decode('utf-8'))
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't encode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @encode.command(aliases=['b64'])
    async def base64(self, ctx, *, text):
        try:
            result = b64.b64encode(bytes(text, 'utf-8'))
            e = discord.Embed(title='Base64 encoder',
                              color=discord.Color.green())
            e.add_field(name='Result:',
                        value=result.decode('utf-8'))
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't encode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @encode.command(aliases=['b85'])
    async def base85(self, ctx, *, text):
        try:
            result = b64.b85encode(bytes(text, 'utf-8'))
            e = discord.Embed(title='Base85 encoder',
                              color=discord.Color.green())
            e.add_field(name='Result:',
                        value=result.decode('utf-8'))
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't encode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @encode.command(aliases=['bin'])
    async def binary(self, ctx, *, text):
        try:
            result = pyconverter.utf8tobin(text)
            e = discord.Embed(title="Binary encoder",
                              color=discord.Color.green())
            e.add_field(name="Result: ",
                        value=' '.join(textwrap.wrap(result, 8)))
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't encode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @encode.command(aliases=['c'])
    async def caesar(self, ctx, text, key: int):
        try:
            result = ""
            for char in text:
                if char.isupper():
                    result += chr((ord(char) + key - 65) % 26 + 65)
                elif char.islower():
                    result += chr((ord(char) + key - 97) % 26 + 97)
                else:
                    result += char

            e = discord.Embed(title="Ceasar Cipher encoder",
                              color=discord.Color.green())
            e.add_field(name="Result: ",
                        value=result)
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't encode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @encode.command(aliases=['dec'])
    async def decimal(self, ctx, *, text):
        try:
            result = ' '.join([str(ord(s)) for s in text])
            e = discord.Embed(title="Decimal encoder",
                              color=discord.Color.green())
            e.add_field(name="Result: ",
                        value=result)
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't encode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @encode.command(aliases=['hex'])
    async def hexadecimal(self, ctx, *, text):
        try:
            result = pyconverter.utf8tohex(text)
            e = discord.Embed(title="Hexadecimal encoder",
                              color=discord.Color.green())
            e.add_field(name="Result: ",
                        value=" ".join(textwrap.wrap(result, 2)))
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't encode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @encode.command(aliases=['mc'])
    async def morse(self, ctx, *, text):
        try:
            result = ""
            for i in text.upper():
                result += morse_dict.get(i) + ' '
            e = discord.Embed(title="Morse Code encoder",
                              color=discord.Color.green())
            e.add_field(name="Result: ",
                        value=result)
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't encode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)
            
    @encode.command(aliases=['n'])
    async def nato(self, ctx, *, text):
        try:
            result = ""
            for i in text.upper():
                result += nato_dict.get(i) + ' '
            e = discord.Embed(title="NATO Phonetic Alphabet encoder",
                              color=discord.Color.green())
            e.add_field(name="Result: ",
                        value=result)
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't encode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)
            
    @encode.command(aliases=['oct'])
    async def octal(self, ctx, *, text):
        try:
            result = pyconverter.utf8tooct(text)
            e = discord.Embed(title="Octal encoder",
                              color=discord.Color.green())
            e.add_field(name="Result: ",
                        value=" ".join(textwrap.wrap(result, 3)))
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't encode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)
           
    @encode.command(aliases=['rf','railfence'])
    async def transposition(self,ctx,text,key:int):
        try:
            result = transpositionEncrypt.encryptMessage(key, text)  # I freaking gave up on my manual code
            e = discord.Embed(title="Transposition Cipher encoder",
                              color=discord.Color.green())
            e.add_field(name='Result:', value=result)
            e.set_footer(text=f'Requested by: {ctx.author}')
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't encode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @encode.command(aliases=['r47'])
    async def rot47(self, ctx, *, text):
        try:
            result = ''
            for i in text:
                j = ord(i)
                if 33 <= j <= 126:
                    result += chr(33+((j + 14) % 94))
                else:
                    result += i
            e = discord.Embed(title="ROT47 Cipher encoder")
            e.add_field(name='Result:',
                        value=result)
            e.set_footer(text=f'Requested by: {ctx.author}')
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't decode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @encode.command(aliases=['mono'])
    async def substitution(self, ctx, text, key):
        try:
            result = text.translate(str.maketrans(string.ascii_uppercase, key.upper())) \
                .translate(str.maketrans(string.ascii_lowercase, key))
            e = discord.Embed(title="Substitution Cipher encoder",
                              color=discord.Color.green())
            e.add_field(name='Result:',
                        value=result)
            e.set_footer(text=f'Requested by: {ctx.author}')
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't encode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @encode.command(aliases=['v'])
    async def vigenere(self, ctx, text, key):
        try:
            result = vigenereCipher.encryptMessage(key, text)  # I freaking gave up on my manual code
            e = discord.Embed(title="Vigenere Cipher decoder",
                              color=discord.Color.green())
            e.add_field(name='Result:', value=result)
            e.set_footer(text=f'Requested by: {ctx.author}')
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't encode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @encode.command(aliases=['bf'])
    async def brainfrick(self, ctx, *, text):
        try:
            result = brainfrick.BFGenerator().text_to_brainfuck(text)
            e = discord.Embed(title="BrainFuck encoder",
                              color=discord.Color.green())
            e.add_field(name='Result:', value=result)
            e.set_footer(text=f'Requested by: {ctx.author}')
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't encode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)


def setup(client):
    client.add_cog(CipherEncode(client))
