from random import randint

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
            return randint(1, self.sides)

    def roll_x_times(self, x):
        i = 0
        rolls = []
        while i < x:
            rolls.append(self.roll())
            i += 1
        return rolls
            

class DiceSet:
    def __init__(self):
        self.d4 = getDice(4)
        self.d6 = getDice(6)
        self.d8 = getDice(8)
        self.d10 = getDice(10)
        self.d12 = getDice(12)
        self.d20 = getDice(20)

    def rollSet(self, d4, d6, d8, d10, d12, d20):
        d4rolls = self.d4.roll_x_times(d4)
        d6rolls = self.d6.roll_x_times(d6)
        d8rolls = self.d8.roll_x_times(d8)
        d10rolls = self.d10.roll_x_times(d10)
        d12rolls = self.d12.roll_x_times(d12)
        d20rolls = self.d20.roll_x_times(d20)

        return [d4rolls, d6rolls, d8rolls, d10rolls, d12rolls, d20rolls]