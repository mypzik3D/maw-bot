import os
import importlib
import sys

prefix = '>' # for commands
modules_directory = 'mods'

import discord
from discord.ext import tasks
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)

class bot_module:
    def __init__(self, module, name):
        self.module = module
        self.name = name
    def __repr__(self):
        return f"bot_module(module={self.module}, name={self.name})"

def load_modules_from_directory(directory):
    modules = []
    files = os.listdir(directory)
    for file in files:
        if file.endswith(".py") and file != "__init__.py":
            module_name = file[:-3]
            module_path = f"{directory.replace('/', '.')}.{module_name}"
            module = importlib.import_module(module_path)
            modules.append(bot_module(module, module_name))
            print(f"[v] finded module: {module_name}")
    return modules

modules = load_modules_from_directory(modules_directory)

async def load():
    sys.path.insert(0, os.path.abspath('.')) 
    for module in modules:
        flag = 0
        if hasattr(module.module, 'noload'):
            flag = module.module.noload
        if flag == 0:
            if hasattr(module.module, 'Cog'):
                await bot.add_cog(module.module.Cog(bot))
                print(f"[i] module {module.name}: is loading")
        else:
            print(f"[i] module {module.name} not loaded, he is noload")

@bot.event
async def on_ready():
    await load()
    await bot.tree.sync()
    print(f"[v] bot ready! he is: {bot.user.name}")

def load_token(file):
    f = open(file,'r')
    token = f.read()
    token.replace("\n", "")
    return(token)

if __name__ == "__main__":
    bot.run(load_token("token.txt"))
