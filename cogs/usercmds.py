import nextcord
from nextcord.ext import commands

class UserCmds(commands.Cog):
    def __init__(self, client):
        self.client = client
    

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

def setup(client):
    client.add_cog(UserCmds(client))
