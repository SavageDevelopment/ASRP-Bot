from pydoc import cli
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import os

client = commands.Bot('?')
client.remove_command('help')






for fn in os.listdir('./cogs'):
    if fn.endswith('.py'):
        client.load_extension(f'cogs.{fn[:-3]}')

client.run(os.environ["BOTTOKEN"])