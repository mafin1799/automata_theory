import random


class NumberGenerator:
    def __init__(self, bitness=4):
        self.bitness = bitness

    def generate_number(self):
        return random.randint(2 ** (self.bitness - 1) + 1, 2 ** self.bitness - 1)
