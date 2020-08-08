import json
from lib.game import Game

print("=====================")

game = Game(4, 6)

print(game.target)



while True:
    t = input("Your move: ")
    t = list(t)

    print(t)



