import os
import lib.utils
import re

class Game:

    ADMIN_EXIT = False
    QUIT_COMMAND = "quit"

    def __init__(self):
        self.FIRST_WORD_LIST = self.getFirstWordList()
        self.SPECIAL_WORD_LIST = self.getSpecialWordList()

    def run(self):
        while not self.ADMIN_EXIT:
            os.system("clear")
            message = input("What is it you seek?\n> ")
            words = message.split()

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

            # Check if the first word of response is a special word
            elif words[0] in self.FIRST_WORD_LIST:
                for word in self.FIRST_WORD_LIST:
                    print (word)
                lib.utils.pauseAnyKey()

            # Check if any words part of special words list
            elif (set(words).intersection(self.SPECIAL_WORD_LIST)):
                for word in set(words).intersection(self.SPECIAL_WORD_LIST):
                    print (word)
                lib.utils.pauseAnyKey()

            # Default behavior if no matches above somehow
            else:
                print ("***********************************\n")
                print ("*** ERROR : MISFORTUNE IMMINENT ***\n")
                print ("***********************************\n\n")
                lib.utils.pauseAnyKey()


    def getFirstWordList(self):
        file = open(os.path.join(os.path.dirname(__file__), '..', 'conf', 'firstWordList'))
        words = file.read().splitlines()
        return words

    def getSpecialWordList(self):
        file = open(os.path.join(os.path.dirname(__file__), '..', 'conf', 'specialWordList'))
        words = file.read().splitlines()
        return words


    def printtest(self):
        print ("Test success!")
