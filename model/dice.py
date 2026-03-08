import random as rd

class Dice:
    dices = []

    def __init__(self, type, quantity, faces):
        self.type = type
        self.quantity = quantity
        self.faces = faces
        self.roll_result = 0
        self.roll_text = ""
        self.dices.append(self)

    def roll_dice(self):
        roll_count = self.quantity
        roll = 0

        while roll_count > 0:
            roll = rd.randint(1, self.faces)
            self.roll_result += roll
            self.roll_text = f"{self.type}({roll}" if self.roll_text == "" else self.roll_text + f" + {roll}"
            roll_count = roll_count -1

        self.roll_text = f"{self.roll_text})"




    