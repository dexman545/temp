from redbot.core.bot import Red

from .feedBot import BotClient



def setup(bot):
    feedBot = BotClient(bot)
    bot.add_cog(feedBot)
    bot.loop.create_task(feedBot.background_feed_update())