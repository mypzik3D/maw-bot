import discord
from discord.ext import tasks
from discord.ext import commands

def load(bot: commands.Bot):
    @bot.tree.command(name="ping", description="test delay")
    async def ping(interaction: discord.Interaction):
        await interaction.response.send_message(f"pong! delay: {round(bot.latency * 1000)} ms")
    
    @bot.tree.command(name="svinfo", description="info this server")
    async def svinfo(interaction: discord.Integration):
        embed = discord.Embed(
            title=interaction.guild.name,
            description=f"Description: \n {interaction.guild.description}\nowner: {interaction.guild.owner.name}",
            colour=0xF0C43F,
        )
        embed.set_thumbnail(url=interaction.guild.icon)
        await interaction.response.send_message(embed=embed)
    
# this code for cycle commands 
#@tasks.loop(seconds=5)
#async def loop():
#    print("a")
