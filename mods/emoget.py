import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional

class Cog(commands.Cog, name="emoget"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="emoget", description="emotes from bot")
    async def emoget(self, ctx, emoji_name: str, number: Optional[int] = 1):
        emojis = [emoji for emoji in self.bot.emojis]
        matching_emojis = [emoji for emoji in emojis if emoji.name == emoji_name] 
        
        if matching_emojis:
            if number >= len(matching_emojis):
                number = len(matching_emojis)
            if number <= 0:
                number = 1
            result = '\n'.join([f"{self.bot.get_emoji(emoji.id)}" for emoji in matching_emojis])
            await ctx.response.send_message(f"{self.bot.get_emoji(matching_emojis[number-1].id)}")
        else:
            await ctx.response.send_message(f"No emoji found with the name {emoji_name}")
