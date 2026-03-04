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

        while roll_count > 0:
            self.roll_result = self.roll_result + rd.randint(1, self.faces)
            self.roll_text = f"({self.roll_result}" if self.roll_text == "" else self.roll_result + f" + {self.roll_result}"
            roll_count = roll_count -1

        self.roll_text = f"{self.roll_text})"




    