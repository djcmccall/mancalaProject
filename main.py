from playerFile import Player
from boardFile import GameBoard
from gameFile import Game

boar1 = GameBoard()
p1 = Player(0)
p2 = Player(0)
game1 = Game(boar1)
game1.startGame(boar1, p1, p2)
