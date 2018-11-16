"""
....................../´¯/) 
....................,/¯../ 
.................../..../ 
............./´¯/'...'/´¯¯`·¸ 
........../'/.../..../......./¨¯\ 
........('(...´...´.... ¯~/'...') 
.........\.................'...../ 
..........''...\.......... _.·´ 
............\..............( 
..............\.............\...
#Make sure to look into constant and configuration files"""

class constants():
	#Channel Configuration
  """
	CHANNELID_FREE_GAME = 512478081081147392
	CHANNELID_DIS_GAME = 512478107567915018
	CHANNELID_MANGA = 512478141592240129
	CHANNELID_ANIME = 512478152530984967
  """
  # Temp channel for testing
  
	CHANNELID_FREE_GAME = 513059448701452308
	CHANNELID_DIS_GAME = 513059448701452308
	CHANNELID_MANGA = 513059448701452308
	CHANNELID_ANIME = 513059448701452308


	#Feed Configuration
	FEED_REFRESH_TIME = 60*63 # Amount of time the Bot waits before refreshing the Feed in Seconds  
	FEED_FREE_GAME = "https://isthereanydeal.com/rss/deals/us/?filter=amazonus%2Cbattlenet%2Cdiscord%2Cgog%2Chumblestore%2Citchio%2Cmicrosoft%2Cwingamestore%2Cuplay%2Csteam%2Csquenix%2Crazer%2Corigin%2C%26regular%2F9%2Fmax%2C%26price%2F0%2F0&options=strict"
	FEED_DIS_GAME = "https://isthereanydeal.com/rss/deals/us/?filter=amazonus%2Cbattlenet%2Cdiscord%2Cgog%2Chumblestore%2Citchio%2Cmicrosoft%2Cwingamestore%2Cuplay%2Csteam%2Csquenix%2Crazer%2Corigin%2C%26regular%2F9%2Fmax%2C%26cut%2F50%2F100%2C-price%2F0%2F0%2C%26pl%2Fwindows%2C%26pl%2Flinux&options=strict"
	FEED_MANGA = "https://mangadex.org/rss/fDEsnM6NTh59FUa7WmY2cerHwtVSvbCZ"
	FEED_ANIME = "https://www.watchcartoononline.com/feed"


	#File Congiguration
	FEED_SAVEFILE = "testing.txt"
	LOGFILE = "feedBot.log"
	FEED_SAVEFILE_SPLITVALUE = "---"

	#Filter Configuration
	REGEX_FREE_GAMES = r"""(((?<=>)[\w\d\s]+(?=<)))|(USD|EUR|€|\$)\s?(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2}))|((?:(?:https?|ftp):\/\/|\b(?:[a-z\d]+\.))(?:(?:[^\s()<>]+|\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))?\))+(?:\((?:[^\s()<>]+|(?:\(?:[^\s()<>]+\)))?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))?)"""
