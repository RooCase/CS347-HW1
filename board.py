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
        Updates the next player in the board.
        """
        if player == "X":
            self.next_player = "O"
        else:
            self.next_player = "X"
    
    def has_won(self, capturedX, capturedO, player, row, col):
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
            return self.is_five_in_row(player, row, col)
        
    def make_move(self, player, row, col):
        """
        Updates player's move in boardState.
        posX: play position of the player in X coordinate, value between 1 and 19
        posY: play position of the player in Y coordinate, value between 1 and 19

        """
        pos = (19 * row) + col - 1 #-1 to adjust for indexing
        if not self.pos_is_empty(pos):
            return ("Invalid move! Position is already occupied.")
        self.boardState[pos] = player
        self.update_player(player)
        return
        
    def check_horizontally(self, player, row, col):
        """
        Checks for five-in-row horizontally given the player and position
        """
        count = 1
        for i in range(max(col-4, 1), min(col+5, 20)): # taking into account board bounds when calculating the range
            if self.boardState[(19 * row) + i - 1] == player:
                count += 1
            else:
                break
        return count == 5 # returns if the count is five
    
    def check_vertically(self, player, row, col):
        """
        Checks for five-in-row vertically given the player and position
        """
        count = 1
        for i in range(max(row-4, 1), min(row+5, 20)): # taking into account board bounds when calculating the range
            if self.boardState[(19 * i) + col - 1] == player:
                count += 1
            else:
                break
        return count == 5 # returns if the count is five

    def check_diagonally(self, player, row, col):
        """
        Checks for five-in-row diagonally given the player and position
        """
        count = 1
        for i in range(max(-row, -col, -4), min(row+5, col+5, 20)): # taking board bounds for both rows and cols
            if self.boardState[(19 * row + i) + col + i - 1] == player: # moving diagonal-wise
                count += 1
            else:
                break
        return count == 5 # returns if the count is five
    
    def check_antidiagonally(self, player, row, col):
        """
        Checks for five-in-row antidiagonally given the player and position
        """
        count = 1
        for i in range(max(-col, -4), min(row+5, 20)): # taking board bounds for both rows and cols
            if self.boardState[(19 * row + i) + col - i - 1] == player: # moving antidiagonal-wise
                count += 1
            else:
                break
        return count == 5 # returns if the count is five

    def is_five_in_row(self, player, row, col):
        """
        Check if 5-in-a-row in either direction
        """
        return self.check_horizontally(player, row, col) or self.check_vertically(player, row, col) \
            or self.check_diagonally(player, row, col) or self.check_antidiagonally(player, row, col)
        
    def pos_is_empty(self, pos):
        """Checks if a given position on the board is empty"""
        if self.boardState[pos] != "-":
            return False
        else:
            return True
    
    def check_captured(self, player, row, col):
        """
        Check if any captures are possible. If so, capture.
        """
        return self.capture_hor(player, row, col) and self.capture_ver(player, row, col) \
            and self.capture_dia(player, row, col) and self.capture_antidia(player, row, col)

    def capture_hor(self, player, row, col):
        capture = False     
        for i in range(max(col-4, 1), min(col+5, 20)): # taking into account board bounds when calculating the range
            if self.boardState[(19 * row) + i - 1] == player:
                count += 1
            else:
                break
        
        # check if direction is valid for left and right
        # if valid check capture, forward loop for 2 times
        #     keep track of capture stones
        #     if can capture, change capture to True and change board items
        return
    
    def capture_ver(self, player, row, col):
        return
    
    def capture_dia(self, player, row, col):
        return
    
    def capture_antidia(self, player, row, col):
        return