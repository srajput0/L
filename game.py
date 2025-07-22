from player import Player
from dice import roll_dice
from board import Board
from db import save_game, load_game, delete_game

class LudoGame:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        data = load_game(chat_id)
        if data:
            self.players = [Player(p["name"], p["position"]) for p in data["players"]]
            self.turn = data["turn"]
        else:
            self.players = []
            self.turn = 0
        self.board = Board()

    def save(self):
        save_game(self.chat_id, {
            "chat_id": self.chat_id,
            "players": [{"name": p.name, "position": p.position} for p in self.players],
            "turn": self.turn
        })

    def add_player(self, name):
        if len(self.players) >= 4:
            return "Maximum 4 players allowed."
        if any(p.name == name for p in self.players):
            return f"{name} already joined."
        self.players.append(Player(name))
        self.save()
        return f"{name} joined the game."

    def roll_dice(self):
        if not self.players:
            return "No players in game."
        current_player = self.players[self.turn]
        dice = roll_dice()
        current_player.move(dice)
        status = f"{current_player.name} rolled 🎲 {dice}, now at position {current_player.position}."
        if self.board.check_winner(current_player):
            delete_game(self.chat_id)
            return f"🎉 {current_player.name} has won the game!"
        self.turn = (self.turn + 1) % len(self.players)
        self.save()
        return status
