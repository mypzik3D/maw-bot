import discord
from discord.ext import commands
from discord import app_commands


class Cog(commands.Cog, name="debug"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='sync')
    @commands.is_owner()
    async def slash_sync(self, ctx):
        synced = await self.bot.tree.sync()
        await ctx.send(f'synced {len(synced)} slash commands')

    @app_commands.command(name="ping", description="test delay")
    async def ping(self, ctx):
        await ctx.response.send_message(f"pong! delay: {round(bot.latency * 1000)} ms")
    
    @app_commands.command(name="svinfo", description="info this server")
    async def svinfo(self, ctx):
        embed = discord.Embed(
            title=interaction.guild.name,
            description=f"Description: \n {interaction.guild.description}\nowner: {interaction.guild.owner.name}",
            colour=0xF0C43F,
        )
        embed.set_thumbnail(url=interaction.guild.icon)
        await ctx.response.send_message(embed=embed)

