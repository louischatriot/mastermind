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


    def test(self, _answer):
        self.try_count += 1

        answer = [c for c in _answer]

        ok = [c == answer[i] for i, c in enumerate(self.target)].count(True)
        near = - ok
        for c in self.target:
            if c in answer:
                near += 1
                answer.remove(c)

        if ok == len(self.target):
            self.success = True

        return ok, near

    # answer as raw input
    def is_legal_raw_input(self, answer):
        for c in answer:
            if c not in self.colors:
                return False

        if len(answer) != len(self.target):
            return False

        return True



