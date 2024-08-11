import discord
from discord.ext import tasks
from discord.ext import commands

bot: commands.Bot

def load(bot: commands.Bot):
    bot = bot
    @bot.tree.command(name="emoget", description="emotes from bot")
    async def emoget(interaction: discord.Interaction, emoji_name: str):
        emojis = [emoji for emoji in bot.emojis]
        matching_emojis = [emoji for emoji in emojis if emoji.name == emoji_name]
    
        if matching_emojis:
            result = '\n'.join([f"{bot.get_emoji(emoji.id)}" for emoji in matching_emojis])
            await interaction.response.send_message(f"{result}")
        else:
            await interaction.response.send_message(f"No emoji found with the name {emoji_name}")
