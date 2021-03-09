import discord
from discord.ext import commands
import base64 as b64
import string
from resources import morse_dict, invmod
from InventWithPython import vigenereCipher
import brainfuck


class CipherDecode(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(aliases=['d'])
    async def decode(self, ctx):
        if ctx.invoked_subcommand is None:
            e = discord.Embed(title="Decode command",
                              colour=discord.Color.green())
            e.add_field(name="Affine (aff)", value='>decode affine <"text"> <1st key> <2nd key>')
            e.add_field(name="Ascii85 (a85)", value='>decode ascii85 <text>')
            e.add_field(name="Atbash (atb)", value='>decode atbash <text>')
            e.add_field(name="Base32 (b32)", value='>decode base32 <text>')
            e.add_field(name="Base64 (b64)", value='>decode base64 <text>')
            e.add_field(name="Base85 (b85)", value='>decode base85 <text>')
            e.add_field(name="Binary (bin)", value='>decode binary <text>')
            e.add_field(name='Brainfuck (bf)', value='>decode bf <text>')
            e.add_field(name="Caesar (c)", value='>decode caeser <"text"> <key>')
            e.add_field(name="Decimal (dec)", value='>decode dec <text>')
            e.add_field(name="Hexadecimal (hex)", value='>decode hex <text>')
            e.add_field(name="Morse Code (mc)", value='>decode morse <text>')
            e.add_field(name="Octal (oct)", value='>decode oct <text>')
            e.add_field(name="Rot47 (r47)", value='>decode rot47 <text>')
            e.add_field(name="Monoalphabetic Substitution (mono)", value='>decode mono <text>')
            e.add_field(name="Transposition (railfence)", value=">decode rf <'text'>")
            e.add_field(name="Vigenère (v)", value=">decode vigenere <'text'> <'key'>")
            await ctx.send(embed=e)
        else:
            pass

    @decode.command(aliases=['a85'])
    async def ascii85(self, ctx, *, text):
        try:
            e = discord.Embed(title='Ascii85 decoder',
                              colour=discord.Color.green())
            e.add_field(name="Result",
                        value=b64.a85decode(text).decode('utf-8'))
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't decode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @decode.command(aliases=['atb'])
    async def atbash(self, ctx, *, text):
        try:
            result = text.translate(str.maketrans(string.ascii_uppercase, string.ascii_uppercase[::-1])) \
                .translate(str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1]))
            e = discord.Embed(title='Atbash Cipher decoder',
                              colour=discord.Color.green())
            e.add_field(name='Result',
                        value=result)
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't decode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @decode.command(aliases=['aff'])
    async def affine(self, ctx, text, k1: int, k2: int):
        try:
            result = ''
            for char in text:
                if char.isupper():
                    result += chr(((invmod(k1, 26) * (ord(char) - 65 - k2)) % 26) + 65)
                elif char.islower():
                    result += chr(((invmod(k1, 26) * (ord(char) - 97 - k2)) % 26) + 97)
                else:
                    result += char
            e = discord.Embed(title='Affine Cipher decoder',
                              colour=discord.Color.green())
            e.add_field(name='Result:',
                        value=result)
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't decode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @decode.command(aliases=['b32'])
    async def base32(self, ctx, *, text):
        try:
            result = b64.b32decode(text).decode("utf-8")
            e = discord.Embed(title='Base32 decoder',
                              colour=discord.Color.green())
            e.add_field(name='Result:',
                        value=result)
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't decode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @decode.command(aliases=['b64'])
    async def base64(self, ctx, *, text):
        try:
            result = b64.b64decode(text).decode("utf-8")
            e = discord.Embed(title='Base64 decoder',
                              colour=discord.Color.green())
            e.add_field(name='Result:',
                        value=result)
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't decode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @decode.command(aliases=['b85'])
    async def base85(self, ctx, *, text):
        try:
            result = b64.b85decode(text).decode("utf-8")
            e = discord.Embed(title='Base85 decoder',
                              colour=discord.Color.green())
            e.add_field(name='Result:',
                        value=result)
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't decode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @decode.command(aliases=['bin'])
    async def binary(self, ctx, *, text):
        try:
            ascii_string = ""
            for binary_value in text.split():
                ascii_string += chr(int(binary_value, 2))
            e = discord.Embed(title="Binary decoder",
                              colour=discord.Color.green())
            e.add_field(name="Result: ",
                        value=ascii_string)
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't decode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @decode.command(aliases=['c'])
    async def caesar(self, ctx, text, key: int):
        try:
            result = ""
            for char in text:
                if char.isupper():
                    result += chr((ord(char) - key - 65) % 26 + 65)
                elif char.islower():
                    result += chr((ord(char) - key - 97) % 26 + 97)
                else:
                    result += char

            e = discord.Embed(title="Ceasar Cipher decoder",
                              colour=discord.Color.green())
            e.add_field(name="Result: ",
                        value=result)
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't decode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @decode.command(aliases=['dec'])
    async def decimal(self, ctx, *, text):
        try:
            ascii_string = ""
            for decimal_value in text.split(" "):
                ascii_string += chr(int(decimal_value, 10))
            e = discord.Embed(title="Decimal decoder",
                              colour=discord.Color.green())
            e.add_field(name="Result: ",
                        value=ascii_string)
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't decode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @decode.command(aliases=['hex'])
    async def hexadecimal(self, ctx, *, text):
        try:
            ascii_string = ""
            for hexadecimal_value in text.split(" "):
                ascii_string += chr(int(hexadecimal_value, 16))
            e = discord.Embed(title="Hexadecimal decoder",
                              colour=discord.Color.green())
            e.add_field(name="Result: ",
                        value=ascii_string)
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't decode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @decode.command(aliases=['mc'])
    async def morse(self, ctx, *, text):
        try:
            result = ""
            for i in text.split(" "):
                result += list(morse_dict.keys())[list(morse_dict.values()).index(i)]
            e = discord.Embed(title="Morse Code decoder",
                              colour=discord.Color.green())
            e.add_field(name="Result: ",
                        value=result)
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't decode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @decode.command(aliases=['oct'])
    async def octal(self, ctx, *, text):
        try:
            ascii_string = ""
            for octal_value in text.split(" "):
                ascii_string += chr(int(octal_value, 8))
            e = discord.Embed(title="Octal decoder",
                              colour=discord.Color.green())
            e.add_field(name="Result: ",
                        value=ascii_string)
            e.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't decode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)
    
    @decode.command(aliases=['rf','railfence'])
    async def transposition(self,ctx,text,key:int):
        try:
            result = transpositionEncrypt(key, text)  # I freaking gave up on my manual code
            e = discord.Embed(title="Transposition Cipher decoder",
                              color=discord.Color.green())
            e.add_field(name='Result:', value=result)
            e.set_footer(text=f'Requested by: {ctx.author}')
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't decode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)
    
    @decode.command(aliases=['r47'])
    async def rot47(self, ctx, *, text):
        try:
            result = ''
            for i in range(len(text)):
                j = ord(text[i])
                if 33 <= j <= 126:
                    result += chr(33 + ((j + 14) % 94))
                else:
                    result += text[i]
            e = discord.Embed(title="ROT47 Cipher decoder",
                              colour=discord.Color.green())
            e.add_field(name='Result:',
                        value=result)
            e.set_footer(text=f'Requested by: {ctx.author}')
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't decode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @decode.command(aliases=['mono'])
    async def substitution(self, ctx, text, key):
        try:
            result = text.translate(str.maketrans(string.ascii_uppercase, key.upper())) \
                .translate(str.maketrans(string.ascii_lowercase, key))
            e = discord.Embed(title="Substitution Cipher decoder",
                              colour=discord.Color.green())
            e.add_field(name='Result:',
                        value=result)
            e.set_footer(text=f'Requested by: {ctx.author}')
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't decode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @decode.command(aliases=['v'])
    async def vigenere(self, ctx, text, key):
        try:
            result = vigenereCipher.decryptMessage(key, text)  # I freaking gave up on my manual code
            e = discord.Embed(title="Vigenere Cipher decoder",
                              colour=discord.Color.green())
            e.add_field(name='Result:', value=result)
            e.set_footer(text=f'Requested by: {ctx.author}')
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't decode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)

    @decode.command(aliases=['bf'])
    async def brainfrick(self, ctx, *, text):
        try:
            result = brainfuck.to_function(text)()
            e = discord.Embed(title="BrainFuck decoder",
                              colour=discord.Color.green())
            e.add_field(name='Result:', value=result)
            e.set_footer(text=f'Requested by: {ctx.author}')
            await ctx.send(embed=e)
        except:
            e = discord.Embed(title='Oops!',
                              description="Sorry we couldn't decode your text :(",
                              color=discord.Color.red())
            await ctx.send(embed=e)


def setup(client):
    client.add_cog(CipherDecode(client))
