import discord
from discord.ext import commands
from datetime import datetime
import os

intents = discord.Intents.default()
intents.members = True
prefix = "!"
bot = commands.Bot(command_prefix = prefix, intents=intents)

OWNER_IDS = [544573811899629568]
COGS = [path[:-3] for path in os.listdir('./cogs') if path[-3:] == '.py']
Announcements = bot.get_channel(717812987364376640)

@bot.command()
async def load(ctx, extension):
    if ctx.message.author.id == 544573811899629568:
        bot.load_extension(f"cogs.{extension}")
        await ctx.send("Cog(s) loaded.")

    else:
        await ctx.send(f"You are not the owner of the bot!!! GET OUT OF HERE!!! <:akaliNani:848283879826784286>")

@bot.command()
async def unload(ctx, extension):
    if ctx.message.author.id == 544573811899629568:
        bot.unload_extension(f"cogs.{extension}")
        await ctx.send("Cog(s) unloaded.")

    else:
        await ctx.send(f"You are not the owner of the bot!!! GET OUT OF HERE!!! <:akaliNani:848283879826784286>")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

@bot.command(name="R3NAUTonline")
async def r3naut_online():
    embed=discord.Embed(title="R3NAUT is online", description=f"<@817768019086016543> online", 
                        color=0x11bb33, timestamp=datetime.utcnow())
    embed.set_footer(text="𝓖𝓪𝓶𝓲𝓷𝓰 𝓵𝓪𝓲𝓻")
    await Announcements.send(embed=embed)

@bot.command(name="R3NAUTonline")
async def r3naut_offline():
    embed=discord.Embed(title="R3NAUT is down", 
                        description=f"<@817768019086016543> is down because I'm developing right now. <a:hackerCD:835166860239568947> \n \n <@817768019086016543> je offline pretože robím práve na ňom. <a:hackerCD:835166860239568947>", 
                        color=0xbb1111, timestamp=datetime.utcnow())
    embed.set_footer(text="𝓖𝓪𝓶𝓲𝓷𝓰 𝓵𝓪𝓲𝓻")
    await Announcements.send(embed=embed)

@bot.command(name="R3NAUThostdown")
async def r3naut_offline():
    embed=discord.Embed(title="R3NAUT is down", 
                        description=f"<@817768019086016543> is down because of hosting servers are down. Sorry \n \n <@817768019086016543> je offline pretože hosting servery sú dole. Sorry", 
                        color=0xbb1111, timestamp=datetime.utcnow())
    embed.set_footer(text="𝓖𝓪𝓶𝓲𝓷𝓰 𝓵𝓪𝓲𝓻")
    await Announcements.send(embed=embed)

@bot.event
async def on_ready():
    print("ZAlpha ready!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="https://github.com/Guard-SK/"))

bot.run(os.environ['DISCORD_TOKEN']) #taking token from Heroku os.environ['DISCORD_TOKEN']