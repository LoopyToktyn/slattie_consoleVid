import os
import lib.utils
import re
import random

class Game:

    ADMIN_EXIT = False
    QUIT_COMMAND = "quit"
    VIDEO_EXTENSION = ".mp4"

    def __init__(self):
        self.FIRST_WORD_LIST = self.getFirstWordList()
        self.SPECIAL_WORD_LIST = self.getSpecialWordList()

    def run(self):
        while not self.ADMIN_EXIT:
            os.system("clear")
            message = input("What is it you seek?\n> ")
            words = message.split()
            specialWords = list(set(words).intersection(self.SPECIAL_WORD_LIST))

            # print ("First word: " + words[0])
            # print ("First listed: " + self.FIRST_WORD_LIST[0])
            # if words[0] == self.FIRST_WORD_LIST[0]:
            #     print ("They same word!")
            # else:
            #     print ("They not same word :(")

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
                lib.utils.pauseAnyKey()

            # SPECIAL WORD
            # Check if any words part of special words list
            elif specialWords:
                randomWord = random.choice(specialWords)
                self.playSpecialWordVid(randomWord)
                lib.utils.pauseAnyKey()

            # NON-SPECIAL WORD
            # Default behavior if no matches above
            else:
                print ("***********************************\n")
                print ("*** ERROR : MISFORTUNE IMMINENT ***\n")
                print ("***********************************\n\n")
                self.playNonSpecialWordVid()
                lib.utils.pauseAnyKey()


    def getFirstWordList(self):
        file = open(os.path.join(os.path.dirname(__file__), '..', 'conf', 'firstWordList'))
        words = file.read().splitlines()
        return words

    def getSpecialWordList(self):
        file = open(os.path.join(os.path.dirname(__file__), '..', 'conf', 'specialWordList'))
        words = file.read().splitlines()
        return words

    def playFirstWordVid(self, word):
        vidLoc = os.path.join(os.path.dirname(__file__), '..', 'vids', 'fw', word)
        vidList = os.listdir(vidLoc)
        randomVid = random.choice(vidList)
        print ("Play first word video: " + randomVid)
        os.system("omxplayer -b ./vids/fw/" + word + "/" + randomVid)

    def playSpecialWordVid(self, word):
        vidLoc = os.path.join(os.path.dirname(__file__), '..', 'vids', 'sw', word)
        vidList = os.listdir(vidLoc)
        randomVid = random.choice(vidList)
        print ("Play special word video: " + randomVid)
        os.system("omxplayer -b " + randomVid)

    def playNonSpecialWordVid(self):
        vidLoc = os.path.join(os.path.dirname(__file__), '..', 'vids', 'nsw')
        vidList = os.listdir(vidLoc)
        randomVid = random.choice(vidList)
        print ("Play non-special word video: " + randomVid)
        os.system("omxplayer -b " + randomVid)
