import discord
from discord.ext import commands
from datetime import datetime
from discord.ext.commands import has_permissions, CheckFailure
import os

intents = discord.Intents.default()
intents.members = True
prefix = "a3"
bot = commands.Bot(command_prefix = prefix, intents=intents)
AlistIDs = [431116940568952842, 544573811899629568]

OWNER_ID = 544573811899629568

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
        print("Cog loaded")

@bot.event
async def on_ready():
    print("R3NAUT Announcements!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="https://github.com/Guard-SK/R3NAUT-Announcements"))

bot.run("ODUyMjM5MjQyNjgzNDgyMTEy.YMD7pQ.jgZahaBnAQj5L9QcL2pRdVcqWhs") #taking token from Heroku os.environ['DISCORD_TOKEN']