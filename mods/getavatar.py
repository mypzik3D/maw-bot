import discord
from discord.ext import commands

class Cog(commands.Cog, name="getavatar"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(name="avatar", description="get avatar")
    async def avatar(self, ctx, member: discord.Member):
        embed = discord.Embed(
            title="user avatar",
            description=f"this is avatar\n{member.name}",
            colour=member.accent_colour,
        )
        embed.set_thumbnail(url=member.avatar)
        await ctx.response.send_message(embed=embed)

