"""
Class for AI that makes moves opposite to the player.
"""

import random

class Ai(object):
    def __init__(self, currboard):
        self.player = ""
        self.board = currboard

    def move(self):
        """
        Calls a Board function to make a move as an AI
        """
        while True: # generates a random position until it encounters an empty one
            x, y = random.randint(0, 18), random.randint(0, 18)
            if self.board.pos_is_empty(x + (19 * y) - 1):
                break
        self.board.make_move(self.player, x, y) # calls the board to make a move
        return
