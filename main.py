import json
from lib.game import Game

print("=====================")

game = Game(4, 6)

print(game.target)

test = ["Y", "Y", "R", "W"]

print(test)


game.test(test)



t = input("Your move:")

t = json.loads(t)

print(t)

print(type(t))


while True:
    t = input("Your move:")


