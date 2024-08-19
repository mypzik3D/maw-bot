import discord
from discord.ext import commands

bot_status   = discord.Status.online
bot_activity = discord.Game("/msgame")  # or discord.Streaming("text stream")

class Cog(commands.Cog, name="activity"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.wait_until_ready()
        await self.bot.change_presence(status=bot_status, activity=bot_activity)

