import random


class DicePlayer:

    name: str = ""
    health: int = 0
    items: dict = {}
    dice_thrown: list = []


    def __init__(self, name: str, health: int, items: dict) -> None:
        self.name = name
        self.health = health
        self.items = items
        self.dice_thrown = []

        return


    def throw_dice(self, dice_to_throw: dict) -> None:
        for key, value in dice_to_throw.items:
            for index in range(value):
                dice_thrown.append(random.randint(1, key))

        print(f"Dice rolled: {dice_thrown}")
        return