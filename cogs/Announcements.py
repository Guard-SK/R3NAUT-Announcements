import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
from datetime import datetime


class Announcements(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(manage_guild=True)
    async def test(self, ctx):
        embed=discord.Embed(title="TEST", description=f"test", 
                            color=0xbb1111, timestamp=datetime.utcnow())
        embed.set_footer(text=f"𝓖𝓪𝓶𝓲𝓷𝓰 𝓵𝓪𝓲𝓻")
        await ctx.send(embed=embed)
        await ctx.send("<@&793160925543661611>")

    @test.error
    async def test_error(ctx, exc):
        if isinstance(exc, CheckFailure):
            await ctx.send("Insufficient permissions to perform that task.")

    @commands.command()
    @has_permissions(manage_guild=True)
    async def Nitroembed(self, ctx):
        embed=discord.Embed(title="Server boost perks", description=f"Welcome to Server boost perks list. \n Looks like you would want to support our server if you reading this. First of all, thanks if you'll support this server by boosting and second of all, these perks you will get, if you'll boost our server:", 
                            color=0xbb1111, timestamp=datetime.utcnow())
        embed.add_field(name="1. External emojies!", value="You can use emojies from other server if you'll boost", inline=False)
        embed.add_field(name="2. Custom nickname color!", value="Just DM staff or above with color request and you'll get custom role with that color!", inline=False)
        embed.add_field(name="3. Modmail priority", value="If you'll DM R3NAUT with request, problem, report or modapplication, your message will be higher priority than others!", inline=False)
        embed.add_field(name="4. You'll get server booster role!", value="Server booster role is something what you can flex to your friends with. And it has some special permissions to it too.", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/629382706299666432/853375256067309608/6494-discord-boost.gif")
        embed.set_footer(text=f"If something goes wrong and you won't get your perks, contact the Owner or Admin of the server \n \n𝓖𝓪𝓶𝓲𝓷𝓰 𝓵𝓪𝓲𝓻")
        channel = self.bot.get_channel(853382232152735764)
        await channel.send(embed=embed)
        await channel.send("<@&793160925543661611><@&750690578722717727>")

    @Nitroembed.error
    async def test_error(ctx, exc):
        if isinstance(exc, CheckFailure):
            await ctx.send("Insufficient permissions to perform that task.")

    @commands.command()
    @has_permissions(manage_guild=True)
    async def Lvlembed(self, ctx):
        embed=discord.Embed(title="Level perks", description=f"Welcome to Level perks list. \n As you could saw, we have leveling system on this server. It this embed you'll find out everything you need to know about leveling system and preks that comes with it:", 
                            color=0xbb1111, timestamp=datetime.utcnow())
        embed.add_field(name="How does it works?", value="The public bot arcane is doing it for us. Just text with someone in text channels to ", inline=False)
        embed.add_field(name="2. Custom nickname color!", value="Just DM staff or above with color request and you'll get custom role with that color!", inline=False)
        embed.add_field(name="3. Modmail priority", value="If you'll DM R3NAUT with request, problem, report or modapplication, your message will be higher priority than others!", inline=False)
        embed.add_field(name="4. You'll get server booster role!", value="Server booster role is something what you can flex to your friends with. And it has some special permissions to it too.", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/629382706299666432/853375256067309608/6494-discord-boost.gif")
        embed.set_footer(text=f"If something goes wrong and you won't get your perks, contact the Owner or Admin of the server \n \n𝓖𝓪𝓶𝓲𝓷𝓰 𝓵𝓪𝓲𝓻")
        channel = self.bot.get_channel(853382232152735764)
        await channel.send(embed=embed)
        await channel.send("<@&793160925543661611><@&750690578722717727>")

    @Lvlembed.error
    async def test_error(ctx, exc):
        if isinstance(exc, CheckFailure):
            await ctx.send("Insufficient permissions to perform that task.")

def setup(bot):
    bot.add_cog(Announcements(bot))
