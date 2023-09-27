import random


class DicePlayer:

    name: str = ""
    health: int = 0
    items: dict = {}

    dice_thrown_dict: dict = {}
    dice_value: int = 0


    def __init__(self, name: str, health: int, items: dict) -> None:
        self.name = name
        self.health = health
        self.items = items
        self.dice_thrown_dict = {}
        self.dice_value = 0

        return


    def throw_dice(self, dice_to_throw: dict) -> None:
        self.dice_thrown_dict = {}
        for key, value in dice_to_throw.items():
            for index in range(value):
                result: int = random.randint(1, key)
                if result in self.dice_thrown_dict.keys():
                    self.dice_thrown_dict[result] += 1
                else:
                    self.dice_thrown_dict[result] = 1

        print(f"Dice rolled: {self.dice_thrown_dict}")
        self.calculate_dice_value()
        print(f"Value: {self.dice_value}")
        return
    
    
    def calculate_dice_value(self) -> None:
        self.dice_value = 0
        for die_value, occurence in self.dice_thrown_dict.items():
            if occurence == 2:
                for die_value2 in self.dice_thrown_dict.keys():
                    if die_value != die_value2:
                        self.dice_value = die_value2
                        return
                
            elif occurence == 3:
                self.dice_value = die_value * 2
                return

        return