import board
from flask import Flask
from random import randint

app = Flask(__name__)
gameDict = {}

class Game:
    def __init__(self):
        gameID = randint(1000, 9999)
        gameBoard = board.Board()
        playerState = ""
        gameDict.update(gameID, self)

@app.route('/newgame/<player>')
def newGame(player):
    activeGame = Game()
    Game.playerState = player
    return {
        'id': activeGame.gameID,
        'state': activeGame.playerState
    }

