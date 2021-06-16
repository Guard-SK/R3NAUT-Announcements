import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
from datetime import datetime


class R3NAUTstatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="R3NAUTonline")
    @has_permissions(manage_guild=True)
    async def r3naut_online(self, ctx):
        role = discord.utils.get(ctx.guild.roles, id=793160925543661611)
        embed=discord.Embed(title="R3NAUT is online", description=f"<@817768019086016543> online", 
                            color=0x11bb33, timestamp=datetime.utcnow())
        embed.set_footer(text=f"𝓖𝓪𝓶𝓲𝓷𝓰 𝓵𝓪𝓲𝓻")
        channel = self.bot.get_channel(707869422726938694) #717812987364376640
        await channel.send(embed=embed)
        await channel.send("<@&793160925543661611>")

    @r3naut_online.error
    async def r3naut_online_error(ctx, exc):
        if isinstance(exc, CheckFailure):
            await ctx.send("Insufficient permissions to perform that task.")

    @commands.command(name="R3NAUToffline")
    @has_permissions(manage_guild=True)
    async def r3naut_offline(self, ctx):
        embed=discord.Embed(title="R3NAUT is down", 
                            description=f"<@817768019086016543> is down because I'm developing right now. <a:hackerCD:835166860239568947> \n \n <@817768019086016543> je offline pretože robím práve na ňom. <a:hackerCD:835166860239568947>", 
                            color=0xbb1111, timestamp=datetime.utcnow())
        embed.set_footer(text=f"𝓖𝓪𝓶𝓲𝓷𝓰 𝓵𝓪𝓲𝓻")
        channel = self.bot.get_channel(717812987364376640)
        await channel.send(embed=embed)
        await channel.send("<@&793160925543661611>")

    @r3naut_offline.error
    async def r3naut_offline_error(ctx, exc):
        if isinstance(exc, CheckFailure):
            await ctx.send("Insufficient permissions to perform that task.")

    @commands.command(name="R3NAUThostdown")
    @has_permissions(manage_guild=True)
    async def r3naut_hostdown(self, ctx):
        role = discord.utils.get(ctx.guild.roles, id=793160925543661611)
        embed=discord.Embed(title="R3NAUT is down", 
                            description=f"<@817768019086016543> is down because of hosting servers are down. Sorry \n \n <@817768019086016543> je offline pretože hosting servery sú dole. Sorry", 
                            color=0xbb1111, timestamp=datetime.utcnow())
        embed.set_footer(text=f"𝓖𝓪𝓶𝓲𝓷𝓰 𝓵𝓪𝓲𝓻")
        channel = self.bot.get_channel(717812987364376640)
        await channel.send(embed=embed)
        await channel.send("<@&793160925543661611>")

    @r3naut_hostdown.error
    async def r3naut_hostdown_error(ctx, exc):
        if isinstance(exc, CheckFailure):
            await ctx.send("Insufficient permissions to perform that task.")

    @commands.command(name="workingonR3NAUT")
    @has_permissions(manage_guild=True)
    async def working_on_r3naut(self, ctx):
        embed = discord.Embed(title="Working on R3NAUT", 
                            description="Right now I'm working on R3NAUT, unexpected shut-downs, errors or features may happen.",
                            color=0xba7526, timestamp=datetime.utcnow())
        embed.set_footer(text="𝓖𝓪𝓶𝓲𝓷𝓰 𝓵𝓪𝓲𝓻")
        
        channel = self.bot.get_channel(717812987364376640)
        await channel.send(embed=embed)
        await channel.send("<@&793160925543661611>")
    

def setup(bot):
    bot.add_cog(R3NAUTstatus(bot))
