import nextcord
from nextcord.ext import commands

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('[Logs] Bot Online!')

def setup(client):
    client.add_cog(Events(client))