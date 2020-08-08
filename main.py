import json
from lib.game import Game
from lib.utils import clear
from lib.constants import colors, color_names
from termcolor import colored


game = Game(4, 6)

tries = []
tests = []


while True:
    clear()

    for i, l in enumerate(tries):
        ok, near = tests[i]
        res = ["\u25cf"] * ok + ["\u25d0"] * near + ["\u25cb"] * (len(game.target) - ok - near)
        line = "  ".join(res) + "    -    " + "  ".join([colored("\u25cf", color_names[it]) for it in l])
        print(line)
        print("")

    print("")
    print("")
    print("")

    print("                                      Available colors: " + "  ".join(colors))

    if game.success:
        print(f"Game won in {game.try_count} moves")
        break

    t = input("Your move: ")
    if not game.is_legal_raw_input(t):
        continue

    t = list(t)
    tries = [t] + tries
    tests = [game.test(t)] + tests





