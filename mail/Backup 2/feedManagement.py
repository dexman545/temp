import feedparser
from .fileManagement import feedFilesystem
import re
from .constants import constants


class FeedManager():

	# Gets the feed and returns it after passing it through a filter
	def getFeed(self, feedURL, feedType):
		lastUpdated = feedFilesystem().getLastUpdated(feedType)
		feedText = feedparser.parse(feedURL, lastUpdated)
		return feedFilter().feedFilterByType(feedText, feedType)


class feedFilter():

	# Passes the feedText to the filter matching the feedType
	def feedFilterByType(self, feed, feedType):
		if(feedType is "Anime"):
			return self.filterBasic(feed)
		elif(feedType is "Manga"):
			return self.filterBasic(feed)
		elif(feedType is "disGame"):
			return self.regExFilter(constants.REGEX_FREE_GAMES,feed)
		elif(feedType is "freeGame"):
			return self.regExFilter(constants.REGEX_FREE_GAMES,feed)
		else:
			return feed

	# A default filter that uses basic entry values to build a String to post
	def filterBasic(self, feedText):
		filteredText = ""
		for entry in feedText.entries:
			filteredText = filteredText + entry.title + "\n" + entry.link + "\n\n"
		return filteredText

	# A filter that uses Regular Expressions for selecting Text
	def regExFilter(self, regAlgorithm, feedText):
		filteredText = ""
		for feedEntry in feedText.entries: # Uses Regular Expressions on every feed Entry
			filteredText = filteredText + feedEntry.title + "\n"
			filteredTexts = re.findall(regAlgorithm, feedEntry.summary)		  
			for textparts in filteredTexts:
				for textchars in textparts:
					filteredText = filteredText + textchars
				filteredText = filteredText + "\n"
			filteredText = filteredText + "\n\n"
		return filteredText