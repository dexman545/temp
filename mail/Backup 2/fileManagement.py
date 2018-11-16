import datetime
from .constants import constants
from tempfile import mkstemp
from shutil import move
from os import fdopen,remove

class feedFilesystem:

  # Updates the file and gives the last updated time back 
  def getLastUpdated(self, feedType):
    currentDate = datetime.datetime.now().strftime("%a, %d %b %Y %X GMT")
    updatedDate = feedType + " : " + currentDate + "\n" # the line how it needs to be updated
    returnDate = None # the value that will be returned

    temporaryFile, abstractPath = mkstemp() # temporary paths, for a new cached file
    with fdopen(temporaryFile,'w') as newFeedSaveFile: # creates a writeable file on the temporary path, that will become the main file later
      try: # checks if the file exists
        with open(constants.FEED_SAVEFILE,"r") as oldFeedSaveFile: # reads the old file
          for line in oldFeedSaveFile: # checks if it can find the feedType in the feedSavefile
            if(line.startswith(feedType)):
              dividedLine = line.split(" : ")
              newFeedSaveFile.write(updatedDate) 
              returnDate = dividedLine[1] # sets the date found to the value that will be returned
            else:
              newFeedSaveFile.write(line)
        remove(constants.FEED_SAVEFILE) # removes the old file 
      except FileNotFoundError: 
        pass
      if(returnDate is None): # checks if the feedType was found
            newFeedSaveFile.write(updatedDate) # writes the feedType to the end with current Date it was not found
    move(abstractPath,constants.FEED_SAVEFILE) # makes the temporary file to the real feedSaveFile
    return returnDate