import json
from lib.game import Game
from lib.utils import clear
from lib.constants import colors, color_names
from termcolor import colored


game = Game(4, 6)

tries = []


while True:
    clear()

    for l in tries:
        ok, near = game.test(l)
        res = ["\u25cf"] * ok + ["\u25cb"] * near + [" "] * (len(game.target) - ok - near)
        line = "  ".join(res) + "    -    " + "  ".join([colored("\u25cf", color_names[it]) for it in l])
        print(line)
        print("")

    print("")
    print("")
    print("")

    print("                                      Available colors: " + "  ".join(colors))

    t = input("Your move: ")
    t = list(t)

    tries = [t] + tries





