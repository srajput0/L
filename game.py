
from .player import Player
from .dice import roll_dice
from .board import Board

class LudoGame:
    def __init__(self):
        self.players = []
        self.board = Board()
        self.turn = 0

    def add_player(self, name):
        if len(self.players) >= 4:
            return "Maximum 4 players allowed."
        if any(p.name == name for p in self.players):
            return f"{name} already joined."
        self.players.append(Player(name))
        return f"{name} joined the game."

    def roll_dice(self):
        if not self.players:
            return "No players in game."
        current_player = self.players[self.turn]
        dice = roll_dice()
        current_player.move(dice)
        status = f"{current_player.name} rolled 🎲 {dice}, now at position {current_player.position}."
        if self.board.check_winner(current_player):
            return f"🎉 {current_player.name} has won the game!"
        self.turn = (self.turn + 1) % len(self.players)
        return status
