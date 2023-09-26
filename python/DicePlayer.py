class DicePlayer:

    name: str = ""
    health: int = 0
    items: dict = {}

    def DicePlayer(self, name: str, health: int, items: dict):
        self.name = name
        self.health = health
        self.items = items