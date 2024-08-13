# MaW-bot
minimalistic and weightless bot for discord
> ### How to use:
> for work need install discord.py:\
> example: `pip install discord`\
> create token.txt and write it in bot token\
> and run: `python bot.py`

> ### How to create your module:
> this bot load discord Cogs and in it write default discord code
> example:
```python
import discord
from discord import app_commands # for slash commands
from discord.ext import commands

class Cog(commands.Cog, name="example_cog"): # name must be unique
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="test delay") # for slash_commands
    async def sl_ping(self, ctx):
        await ctx.response.send_message(f"pong! delay: {round(bot.latency * 1000)} ms")
    
    @commands.Cog.listener() # for event = @bot.event
    async def on_ready(self):
        print("bot is ready, name {self.bot.user.name")

    @commands.command(name="ping") # for default commands
    async def com_ping(self, ctx):
        synced = await self.bot.tree.sync()
        await ctx.send("pong!")

```
> module may have variable `noload`\
> if `noload = 1` then `def load` wont start
