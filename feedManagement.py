import feedparser
from .fileManagement import feedFilesystem
import re
from .constants import constants
from datetime import datetime
from time import mktime

class FeedManager():

	# Gets the feed and returns it after passing it through a filter
	def getFeed(self, feedURL, feedType):
		feedText = feedparser.parse(feedURL)
		lastUpdated = feedFilesystem().getLastUpdated(feedType)

		if(lastUpdated is not None):
			lastUpdated = datetime.strptime(lastUpdated, "%c")

		feedText = self.entries_with_dates_after(feedText, lastUpdated)
		return feedFilter().feedFilterByType(feedText, feedType)

	def entries_with_dates_after(self, feed, date):
		response = []
		for entry in feed.entries:
			publishedTime = datetime.fromtimestamp(mktime(entry.get('published_parsed')))
			# print(publishedTime.strftime("%c") + "    " + date.strftime("%c"))
			if (date is None) or (publishedTime > date):
				response.append(entry)
		return response 

class feedFilter():

	# Passes the feedText to the filter matching the feedType
	def feedFilterByType(self, feed, feedType):
		if(feedType is "Anime"):
			return self.filterBasic(feed)
		elif(feedType is "Manga"):
			return self.filterBasic(feed)
		elif(feedType is "disGame"):
			return self.regExFilter(constants.REGEX_FREE_GAMES, feed)
		elif(feedType is "freeGame"):
			return self.regExFilter(constants.REGEX_FREE_GAMES, feed)
		else:
			return feed

	# A default filter that uses basic entry values to build a String to post
	def filterBasic(self, feedText):
		m = []
		filteredText = ""
		for entry in feedText:
			filteredText = filteredText + entry.title + "\n" + entry.link + "\n\n"
			filteredText = filteredText + "-========- \n\n"
			m.insert(0, filteredText)
		return m

	# A filter that uses Regular Expressions for selecting Text
	def regExFilter(self, regAlgorithm, feedText):
		filteredText = ""
		m = []
		reg = re.compile(regAlgorithm)
		# priceTag = re.compile(r"(USD|EUR|€|\$\s?\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2}))")
		for feedEntry in feedText: # Uses Regular Expressions on every feed Entry
			filteredText = filteredText + feedEntry.title + ":\n"
			filteredTexts = reg.findall(feedEntry.summary)
			for textpart in filteredTexts:
				# print(textpart)
				filteredText = filteredText + textpart + "\n"
			filteredText = filteredText + "\n\n"
			filteredText = filteredText + "-========- \n\n"
			m.insert(0, filteredText)
		return m
