import os
import lib.utils
import re
import random
import time

class Game:

    ADMIN_EXIT = False
    QUIT_COMMAND = "quit"
    VIDEO_EXTENSION = ".mp4"

    def __init__(self):
        self.FIRST_WORD_LIST = self.getFirstWordList()
        self.SPECIAL_WORD_LIST = self.getSpecialWordList()

    def run(self):
        self.ADMIN_EXIT = False
        while not self.ADMIN_EXIT:
            os.system("clear")
            message = input("What is it you seek?\n> ")
            self.log(message)
            words = message.lower().split()
            specialWords = list(set(words).intersection(self.SPECIAL_WORD_LIST))

            # Did they not type anything?
            if not words:
                print ("You seek nothing?")
                lib.utils.pauseAnyKey()

            # Administrative back door to freedom
            elif words[0] == self.QUIT_COMMAND:
                self.ADMIN_EXIT = True
                break

            # FIRST WORD
            # Check if the first word of response is a special word
            elif words[0] in self.FIRST_WORD_LIST:
                self.playFirstWordVid(words[0])
                # lib.utils.pauseAnyKey()

            # SPECIAL WORD
            # Check if any words part of special words list
            elif specialWords:
                randomWord = random.choice(specialWords)
                self.playSpecialWordVid(randomWord)
                # lib.utils.pauseAnyKey()

            # NON-SPECIAL WORD
            # Default behavior if no matches above
            else:
                self.playNonSpecialWordVid()
                # lib.utils.pauseAnyKey()


    def initializeFolders(self):

        # Create directories for words in word lists
        # Also removes directories for deprecated words/videos
        for word in self.FIRST_WORD_LIST:
            fwLoc = os.path.join(os.path.dirname(__file__), '..', 'vids', 'fw', word)
            if not os.path.isdir(fwLoc):
                os.system("mkdir " + fwLoc)

        fwDirList = os.listdir(os.path.join(os.path.dirname(__file__), '..', 'vids', 'fw'))
        for directory in fwDirList:
            if directory not in self.FIRST_WORD_LIST:
                try:
                    os.rmdir(os.path.join(os.path.dirname(__file__), '..', 'vids', 'fw', directory))
                except:
                    print ("Skipping < %s >: Not a directory . . .\n", directory)

        for word in self.SPECIAL_WORD_LIST:
            swLoc = os.path.join(os.path.dirname(__file__), '..', 'vids', 'sw', word)
            if not os.path.isdir(swLoc):
                os.system("mkdir " + swLoc)

        swDirList = os.listdir(os.path.join(os.path.dirname(__file__), '..', 'vids', 'sw'))
        for directory in swDirList:
            if directory not in self.SPECIAL_WORD_LIST:
                try:
                    os.rmdir(os.path.join(os.path.dirname(__file__), '..', 'vids', 'sw', directory))
                except:
                    print ("Skipping < %s >: Not a directory . . .\n", directory)

        # lib.utils.pauseAnyKey()

    def log(self, message):
        logLoc = os.path.join(os.path.dirname(__file__), '..', 'conf', 'prompt_response.log')
        f = open(logLoc, 'a+')
        f.write(time.strftime("%x %H:%M:%S") + " >> " + message + "\n")
        f.close()

    def getFirstWordList(self):
        file = open(os.path.join(os.path.dirname(__file__), '..', 'conf', 'first_word_list'))
        words = file.read().lower().splitlines()
        return words

    def getSpecialWordList(self):
        file = open(os.path.join(os.path.dirname(__file__), '..', 'conf', 'special_word_list'))
        words = file.read().lower().splitlines()
        return words

    def playFirstWordVid(self, word):
        vidLoc = os.path.join(os.path.dirname(__file__), '..', 'vids', 'fw', word)
        vidList = os.listdir(vidLoc)
        randomVid = random.choice(vidList)
        #print ("Play first word video: " + randomVid)
        os.system("omxplayer -b ./vids/fw/" + word + "/" + randomVid)

    def playSpecialWordVid(self, word):
        vidLoc = os.path.join(os.path.dirname(__file__), '..', 'vids', 'sw', word)
        vidList = os.listdir(vidLoc)
        randomVid = random.choice(vidList)
        #print ("Play special word video: " + randomVid)
        os.system("omxplayer -b ./vids/sw/" + word + "/" + randomVid)

    def playNonSpecialWordVid(self):
        vidLoc = os.path.join(os.path.dirname(__file__), '..', 'vids', 'nsw')
        vidList = os.listdir(vidLoc)
        randomVid = random.choice(vidList)
        #print ("Play non-special word video: " + randomVid)
        os.system("omxplayer -b ./vids/nsw/" + randomVid)
