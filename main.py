import disnake
import os
from online import keep_alive
from disnake.ext import commands

intents = disnake.Intents.default()
intents.members = True
intents.reactions = True
bot = commands.Bot(command_prefix='!',intents=intents,activity=disnake.Game(name='em desenvolvimento'))

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


keep_alive()
key = os.getenv('thetoken')
bot.run(key)