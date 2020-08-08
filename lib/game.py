from lib.constants import colors
from random import randrange

class Game():
    def __init__(self, n_spots, n_colors):
        if n_colors <= n_spots:
            raise Error("Not enough colors")

        self.colors = [colors[i] for i in range(0, n_colors)]
        self.target = [self.colors[randrange(0, n_colors)] for i in range(0, n_spots)]

        self.try_count = 0
        self.success = False


    def test(self, answer):
        self.try_count += 1

        used = [False] * len(self.target)
        res = [""] * len(self.target)

        for i, c in enumerate(self.target):
            if c == answer[i]:
                res[i] = "B"
                used[i] = True

        for i, c in enumerate(answer):
            if res[i] == "B":
                continue

            try:
                idx = [c if not used[i] else "" for i, c in enumerate(self.target)].index(c)
            except ValueError:
                continue

            if idx:
                res[i] = "W"
                used[idx] = True

        return res




