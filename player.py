class Player:
    def __init__(self, name, position=0):
        self.name = name
        self.position = position

    def move(self, steps):
        self.position += steps
