import board
import ai
from flask import Flask
from random import randint

app = Flask(__name__)
gameDict = {}

class Game:
    def __init__(self):
        self.gameID = randint(1000, 9999)
        self.gameBoard = board.Board()
        self.gameState = self.gameBoard.nextPlayer + "#" + self.gameBoard.boardState + "#" + self.gameBoard.capturedX + "#" + self.gameBoard.capturedO
        self.gameDict.update(self.gameID, self)
        self.ai = ai(self.gameBoard)

    def update(self):
        """
        updates game state
        :return: nothing
        """
        self.gameState = self.gameBoard.nextPlayer + "#" + self.gameBoard.boardState + "#" + self.gameBoard.capturedX + "#" + self.gameBoard.capturedO


@app.route('/newgame/<player>')
def newGame(player):
    """

    :param player: what the player is (x or o)
    :return: JSON value that notifies the game ID, and the active state of the board
    """
    activeGame = Game()
    Game.gameState = activeGame.gameState
    return {
        'id': activeGame.gameID,
        'state': activeGame.gameState
    }

@app.route('/nextmove/<gameID>/<int:row>/<int:col>')
def nextMove(gameID, row, col):
    """

    :param gameID: the ID for game
    :param row: what row to add a player stone
    :param col: what column to add a player stone
    :return: the updated game state
    """
    activeGame = gameDict[gameID]
    board = activeGame.gameBoard
    board.make_move(board.next_player, row, col)
    activeGame.ai.move()
    activeGame.update()

    return {
        'ID': gameID,
        'row': row,
        'column': col,
        'state': activeGame.gameState,
    }
