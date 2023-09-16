#gamestate is in the format of player#board#capturedX#capturedO
 
class Board:
    def __init__(self):
        self.next_player = ""
        self.boardState = "-------------------"*19
        self.capturedX = 0
        self.capturedO = 0

    def update_points(self, player):
        """
        Updates point for player after capturing stone.
        """
        if player == "X":
            self.capturedX += 2
        elif player == "O":
            self.capturedO += 2
        else:
            raise Exception("Invalid playerID provided")
    
    def update_player(self, player):
        """
        Updates the next year in the board.
        """
        if player == "X":
            self.next_player = "O"
        else:
            self.next_player = "X"
    
    def has_won(self, capturedX, capturedO, player, posX, posY):
        """
        Checks if either player has won 
            1) after capturing at least 2 pairs of stones (10 pieces)
            2) after at least one 5-in-a-row
        """
        if capturedX >= 10:
            return print("X has won!")
        elif capturedO >= 10:
            return print("O has won!")
        else:
            return self.is_five_in_row(player, posX, posY)
        
    def make_move(self, player, posX, posY):
        """
        Updates player's move in boardState.
        """
        pos = (19 * posX) + posY - 1 #-1 to adjust for indexing
        if not self.pos_is_empty(pos):
            return print("Invalid move! Position is already occupied.")
        self.boardState[pos] = player
        self.update_player(player)
        return
        
    def check_horizontally(self, player, posX, posY):
        """
        Checks for five-in-row horizontally given the player and position
        """
        count = 0
        for i in range(max(posY-4, 0), min(posY+5, 20)): # taking into account board bounds when calculating the range
            if self.boardState[(19 * posX) + i - 1] == player:
                count += 1
            else:
                break
        return count == 5 # returns if the count is five
    
    def check_vertically(self, player, posX, posY):
        """
        Checks for five-in-row vertically given the player and position
        """
        count = 0
        for i in range(max(posX-4, 0), min(posX+5, 20)): # taking into account board bounds when calculating the range
            if self.boardState[(19 * i) + posY - 1] == player:
                count += 1
            else:
                break
        return count == 5 # returns if the count is five

    def check_diagonally(self, player, posX, posY):
        """
        Checks for five-in-row diagonally given the player and position
        """
        count = 0
        for i in range(max(-posX, -posY, -4), min(posX+5, posY+5, 20)): # taking board bounds for both rows and cols
            if self.boardState[(19 * posX + i) + posY + i - 1] == player: # moving diagonal-wise
                count += 1
            else:
                break
        return count == 5 # returns if the count is five
    
    def check_antidiagonally(self, player, posX, posY):
        """
        Checks for five-in-row antidiagonally given the player and position
        """
        count = 0
        for i in range(max(-posY, -4), min(posX+5, 20)): # taking board bounds for both rows and cols
            if self.boardState[(19 * posX + i) + posY - i - 1] == player: # moving antidiagonal-wise
                count += 1
            else:
                break
        return count == 5 # returns if the count is five

    def is_five_in_row(self, player, posX, posY):
        """
        Check if 5-in-a-row in either direction
        """
        return self.check_horizontally(player, posX, posY) or self.check_vertically(player, posX, posY) \
            or self.check_diagonally(player, posX, posY) or self.check_antidiagonally(player, posX, posY)
        
    def pos_is_empty(self, pos):
        """Checks if a given position on the board is empty"""
        if self.boardState[pos] != "":
            return False
        else:
            return True
        
    