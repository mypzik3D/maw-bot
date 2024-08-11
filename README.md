# MaW-bot
minimalistic and weird bot for discord
> ### How to use:
> for work need install discord.py:
> example: `pip install discord`
> create token.txt and write it in bot token
> and run: `python bot.py`

> ### How to create your module:
> minimal:
```python
import discord
from discord.ext import commands

def load(bot: commands.Bot): # function called 1 time
    # there write default bot code example:

    @bot.tree.command(name="ping", description="test delay")
    async def ping(interaction: discord.Interaction):
        await interaction.response.send_message(f"pong! delay: {round(bot.latency * 1000)} ms")

```
> with cycle:
```python
import discord
from discord.ext import commands
from discord.ext import tasks

bot: commands.Bot # global definition 

def load(bot: commands.Bot): # function called 1 time
    bot = bot
    # there write default bot code

@tasks.loop(seconds=1) # for example this cycle will be repeated 1 time per second
async def loop():
    # there write code for cycle
```
