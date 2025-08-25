import random

class direction:
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    LEFT = 4

    @classmethod
    def random(cls):
        return random.randint(1, 4)