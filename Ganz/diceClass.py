import random
import tkinter

class Dice():
    def __init__(self, color, score, button, buttonText, label, labelText, checkVal, count):
        self.color = color
        self.value = random.randint(1, 6)
        self.score = score
        self.dieButton = button
        self.dieButtonText = buttonText
        self.dieLabel = label
        self.dieLabelText = labelText
        self.checkVal = checkVal
        self.count = count
        self.currentScore = 0
        self.lock = False

    def roll(self):
        return random.randint(1, 6)


class DiceDisplay():
    def __init__(self):
        self.frame = diceFrame


