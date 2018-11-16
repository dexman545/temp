from redbot.core import commands
import discord

class Mycog:
    """My custom cog"""

    @commands.command()
    async def makeserver(self):
        name = "Trash Staff"
        discord.create_guild(name, region=None, icon=None)
        await ctx.send("I can do stuff!")
