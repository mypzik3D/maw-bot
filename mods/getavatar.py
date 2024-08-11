import discord
from discord.ext import commands

def load(bot: commands.Bot):
    @bot.tree.command(name="avatar", description="get avatar")
    async def avatar(interaction: discord.Interaction, member: discord.Member):
        embed = discord.Embed(
            title="user avatar",
            description=f"this is avatar\n{member.name}",
            colour=member.accent_colour,
        )
        embed.set_thumbnail(url=member.avatar)
        await interaction.response.send_message(embed=embed)
