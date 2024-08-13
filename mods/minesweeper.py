import discord
from discord.ext import commands
from discord import app_commands
import random

# config
max_size = 9 # max sells 99 => max_max_size 9
nums = [
':zero:',
':one:',
':two:',
':three:',
':four:',
':five:',
':six:',
':seven:',
':eight:',
':boom:']

def check_sell(field,x,y,size):
    count = 0
    for xp in range(3):
        if x+xp-1 >= 0 or x+xp-1 < size:
            for yp in range(3):
                if y+yp-1 >= 0 or y+yp-1 < size :
                    if field[x+xp-1][y+yp-1] == 9:
                        count+=1
    return count

class Cog(commands.Cog, name="minesweeper"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="msgame", description="cool mini game")
    async def ms_game(self, ctx, size: int, bomb_count: int):
        if bomb_count > size*size:
            await ctx.response.send_message("too much bomb :<")
        elif size <= 0:
            await ctx.response.send_message("size field <= 0")
        elif size > max_size:
            await ctx.response.send_message(f"size > {max_size}")
        else:
            field = []

            for i in range(size+1):
                field.append([0] * (size+1))
            for i in range(bomb_count):
                while 1:
                    x = random.randint(0, size-1)
                    y = random.randint(0, size-1)
                    if field[x][y] != 9 :
                        field[x][y] = 9
                        break
            mes = "minesweeper!\n"
            for x in range(size):
                for y in range(size):
                    if field[x][y] != 9:
                        field[x][y] = check_sell(field=field,x=x,y=y,size=size)
            for x in range(size):
                for y in range(size):
                    mes = mes+f'||{nums[field[x][y]]}||'
                mes += '\n'
            await ctx.response.send_message(mes)
