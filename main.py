import board
from ai import Ai
from flask import Flask
from random import randint

app = Flask(__name__)
gameDict = {}

class Game:
    def __init__(self):
        self.gameID = randint(1000, 9999)
        self.gameBoard = board.Board()
        self.gameState = self.update()
        self.AI = Ai(self.gameBoard)
        dictADD = {self.gameID: self}
        gameDict.update(dictADD)

    def update(self):
        """
        updates game state
        :return: nothing
        """
        self.gameState = str(self.gameBoard.next_player) + "#" + str(self.gameBoard.boardState) + "#" + str(self.gameBoard.capturedX) + "#" + str(self.gameBoard.capturedO)


@app.route('/newgame/<player>')
def newGame(player):
    """
    :param player: what the player is (x or o)
    :return: JSON value that notifies the game ID, and the active state of the board
    """
    activeGame = Game()
    if player == "X" or player == "x":
        activeGame.gameBoard.next_player = "X"
        activeGame.AI.player = "O"
    elif player == "O" or player == "o":
        activeGame.AI.player = "X"
        activeGame.gameBoard.next_player = "X"
        activeGame.AI.move()

    else:
        raise Exception("Player must be either X or O!")
    activeGame.update()
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
    activeGame = gameDict[int(gameID)]
    board = activeGame.gameBoard
    board.make_move(board.next_player, row, col)
    activeGame.AI.move()
    activeGame.update()

    return {
        'ID': gameID,
        'row': row,
        'column': col,
        'state': activeGame.gameState,
    }

app.run()