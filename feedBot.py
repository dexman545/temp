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
			constants.FEED_ANIME, "Anime")
			mangaFeed = FeedManager().getFeed(
			constants.FEED_MANGA, "Manga")
			disGameFeed = FeedManager().getFeed(
			constants.FEED_DIS_GAME, "disGame")
			freeGame = FeedManager().getFeed(
			constants.FEED_FREE_GAME, "freeGame")
		
			print("Preparing to send to channels!")
			print(animeFeed)
			try:
				for msg in animeFeed:
					await self.bot.get_channel(constants.CHANNELID_ANIME).send(msg)
          await asyncio.sleep(1)
			except:
				print("failed Anime")
			try:
				for msg in mangaFeed:
					await self.bot.get_channel(constants.CHANNELID_MANGA).send(msg)
          await asyncio.sleep(1)
			except:
				print("failed Manga")
			try:
				for msg in disGame:
					await self.bot.get_channel(constants.CHANNELID_DIS_GAME).send(msg)
          await asyncio.sleep(1)
			except:
				print("failed disGame")
			try:
				for msg in freeGame:
					await self.bot.get_channel(constants.CHANNELID_FREE_GAME).send(msg)
          await asyncio.sleep(1)
			except:
				print("failed freeGame")
			await asyncio.sleep(constants.FEED_REFRESH_TIME)
	

	
	def __unload(self, bot):
		bot.task.cancel()