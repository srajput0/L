class Board:
    def __init__(self):
        self.finish_line = 50  # Simplified board finish

    def check_winner(self, player):
        return player.position >= self.finish_line
