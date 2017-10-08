#!/usr/bin/env python3

import lib.utils
import lib.getch
from lib.Game import Game
import menu
import sys


global FIRSTRUN

FIRSTRUN = True

# def refreshHandler():
  #Kill keyboard/mouse
  # KeyboardLocker.turn_off()


Menu = menu.Menu
utils = lib.utils
Game = Game()

# main = Menu(title = "Main Menu", prompt = ">", refresh = refreshHandler)
main = Menu(title = "Main Menu", prompt = ">")

main.set_options([
  ("Begin Game", Game.run),
  ("Initialize Game", Game.initializeFolders),
  ("Exit", main.close)
])

# sub = Menu(title = "Submenu")
# sub.set_options([
# ("Return to main menu", sub.close)
# ])


main.open()
