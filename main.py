import board
from flask import Flask
from random import randint

app = Flask(__name__)
gameDict = {}

class game:
    def __init__(self):
        gameID = randint(1000, 9999)
        gameBoard = board()
        playerState = "x"
        gameDict.update(gameID, self)

@app.route('/newgame/player')
def newGame():
    activeGame = game()
    return {
        'id': activeGame.gameID,
        'state': activeGame.playerState
    }

