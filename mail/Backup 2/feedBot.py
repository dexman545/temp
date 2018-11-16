import discord
import asyncio
import logging
from redbot.core import Config, commands, checks
from redbot.core.bot import Red
from .feedManagement import FeedManager
from .constants import constants

# Start Logging at the very beginning
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
filename=constants.LOGFILE, encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
'%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

Cog = getattr(commands, "Cog", object)


class BotClient(Cog):

	# Init for the bot
	def __init__(self, bot: Red):
		self.bot = bot
		default_guild = {"channelid": None}
		# self.task = bot.loop.create_task(feedBot.background_feed_update())

	# This function will run, once the bot is succesfully connected and started

	# Updates the feeds in the background
	async def background_feed_update(self):

		while True:
			# resizing because discord doesnt allow more than sending of 2000 letters
			animeFeed = FeedManager().getFeed(
			constants.FEED_ANIME, "Anime")[:2000]
			mangaFeed = FeedManager().getFeed(
			constants.FEED_MANGA, "Manga")[:2000]
			disGameFeed = FeedManager().getFeed(
			constants.FEED_DIS_GAME, "disGame")[:2000]
			freeGame = FeedManager().getFeed(
			constants.FEED_FREE_GAME, "freeGame")[:2000]
		
			print("test")
		
			try:
				await self.bot.get_channel(constants.CHANNELID_ANIME).send(animeFeed)
			except:
				print("failed Anime")
			try:
				await self.bot.get_channel(constants.CHANNELID_MANGA).send(mangaFeed)
			except:
				print("failed Manga")
			try:
				await self.bot.get_channel(constants.CHANNELID_DIS_GAME).send(disGameFeed)
			except:
				print("failed disGame")
			try:
				await self.bot.get_channel(constants.CHANNELID_FREE_GAME).send(freeGame)
			except:
				print("failed freeGame")
			await asyncio.sleep(60*63)
	

	
	def __unload(self, bot):
		bot.task.cancel()