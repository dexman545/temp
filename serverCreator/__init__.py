from .serverCreator import serverCreator

def setup(bot):
    bot.add_cog(serverCreator())
