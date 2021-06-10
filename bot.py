import discord
from discord.ext import commands
from datetime import datetime
from discord.ext.commands import has_permissions, CheckFailure
import os

intents = discord.Intents.default()
intents.members = True
prefix = "a3"
bot = commands.Bot(command_prefix = prefix, intents=intents)

OWNER_IDS = [544573811899629568]

@bot.command(name="R3NAUTonline")
@has_permissions(manage_guild=True)
async def r3naut_online(ctx):
    role = discord.utils.get(ctx.guild.roles, id=793160925543661611)
    embed=discord.Embed(title="R3NAUT is online", description=f"<@817768019086016543> online", 
                        color=0x11bb33, timestamp=datetime.utcnow())
    embed.set_footer(text=f"<@&793160925543661611>|𝓖𝓪𝓶𝓲𝓷𝓰 𝓵𝓪𝓲𝓻")
    channel = bot.get_channel(717812987364376640)
    await channel.send(embed=embed)

@r3naut_online.error
async def ban_command_error(ctx, exc):
    if isinstance(exc, CheckFailure):
        await ctx.send("Insufficient permissions to perform that task.")

@bot.command(name="R3NAUToffline")
@has_permissions(manage_guild=True)
async def r3naut_offline(ctx):
    embed=discord.Embed(title="R3NAUT is down", 
                        description=f"<@817768019086016543> is down because I'm developing right now. <a:hackerCD:835166860239568947> \n \n <@817768019086016543> je offline pretože robím práve na ňom. <a:hackerCD:835166860239568947>", 
                        color=0xbb1111, timestamp=datetime.utcnow())
    embed.set_footer(text=f"<@&793160925543661611>|𝓖𝓪𝓶𝓲𝓷𝓰 𝓵𝓪𝓲𝓻")
    channel = bot.get_channel(717812987364376640)
    await channel.send(embed=embed)

@r3naut_offline.error
async def ban_command_error(ctx, exc):
    if isinstance(exc, CheckFailure):
        await ctx.send("Insufficient permissions to perform that task.")

@bot.command(name="R3NAUThostdown")
@has_permissions(manage_guild=True)
async def r3naut_hostdown(ctx):
    role = discord.utils.get(ctx.guild.roles, id=793160925543661611)
    embed=discord.Embed(title="R3NAUT is down", 
                        description=f"<@817768019086016543> is down because of hosting servers are down. Sorry \n \n <@817768019086016543> je offline pretože hosting servery sú dole. Sorry", 
                        color=0xbb1111, timestamp=datetime.utcnow())
    embed.set_footer(text=f"<@&793160925543661611>|𝓖𝓪𝓶𝓲𝓷𝓰 𝓵𝓪𝓲𝓻")
    channel = bot.get_channel(717812987364376640)
    await channel.send(embed=embed)

@r3naut_hostdown.error
async def ban_command_error(ctx, exc):
    if isinstance(exc, CheckFailure):
        await ctx.send("Insufficient permissions to perform that task.")

@bot.command()
@has_permissions(manage_guild=True)
async def test(ctx):
    role = discord.utils.get(ctx.guild.roles, id=793160925543661611)
    await ctx.send(f"<@&793160925543661611>")

@bot.event
async def on_ready():
    print("R3NAUT Announcements!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="https://github.com/Guard-SK/R3NAUT-Announcements"))

bot.run(os.environ['DISCORD_TOKEN']) #taking token from Heroku os.environ['DISCORD_TOKEN']