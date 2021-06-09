import discord
from discord.ext import commands
from datetime import datetime
import os

intents = discord.Intents.default()
intents.members = True
prefix = "a3"
bot = commands.Bot(command_prefix = prefix, intents=intents)

OWNER_IDS = [544573811899629568]

@bot.command(name="R3NAUTonline")
async def r3naut_online(ctx):
    role = discord.utils.get(ctx.guild.roles, id=793160925543661611)
    embed=discord.Embed(title="R3NAUT is online", description=f"<@817768019086016543> online", 
                        color=0x11bb33, timestamp=datetime.utcnow())
    embed.set_footer(text=f"<@&793160925543661611>|𝓖𝓪𝓶𝓲𝓷𝓰 𝓵𝓪𝓲𝓻")
    channel = bot.get_channel(717812987364376640)
    await channel.send(embed=embed)

@bot.command(name="R3NAUToffline")
async def r3naut_offline(ctx):
    embed=discord.Embed(title="R3NAUT is down", 
                        description=f"<@817768019086016543> is down because I'm developing right now. <a:hackerCD:835166860239568947> \n \n <@817768019086016543> je offline pretože robím práve na ňom. <a:hackerCD:835166860239568947>", 
                        color=0xbb1111, timestamp=datetime.utcnow())
    embed.set_footer(text=f"<@&793160925543661611>|𝓖𝓪𝓶𝓲𝓷𝓰 𝓵𝓪𝓲𝓻")
    channel = bot.get_channel(717812987364376640)
    await channel.send(embed=embed)

@bot.command(name="R3NAUThostdown")
async def r3naut_offline(ctx):
    role = discord.utils.get(ctx.guild.roles, id=793160925543661611)
    embed=discord.Embed(title="R3NAUT is down", 
                        description=f"<@817768019086016543> is down because of hosting servers are down. Sorry \n \n <@817768019086016543> je offline pretože hosting servery sú dole. Sorry", 
                        color=0xbb1111, timestamp=datetime.utcnow())
    embed.set_footer(text=f"<@&793160925543661611>|𝓖𝓪𝓶𝓲𝓷𝓰 𝓵𝓪𝓲𝓻")
    channel = bot.get_channel(717812987364376640)
    await channel.send(embed=embed)

@bot.command()
async def test(ctx):
    role = discord.utils.get(ctx.guild.roles, id=793160925543661611)
    await ctx.send(f"<@&793160925543661611>")

@bot.event
async def on_ready():
    print("R3NAUT Announcements!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="https://github.com/Guard-SK/"))

bot.run("ODUyMjM5MjQyNjgzNDgyMTEy.YMD7pQ.VKNpi1jyN0k9GbeXYRp0slRTmuc") #taking token from Heroku os.environ['DISCORD_TOKEN']