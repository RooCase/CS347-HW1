#gamestate is in the format of player#board#capturedX#capturedO
 
class Board:
    def __init__(self):
        self.next_player = ""
        self.boardState = "-------------------"*19
        self.capturedX = 0
        self.capturedO = 0

    def update_points(self, player):
        if player == "X":
            self.capturedX += 2
        elif player == "O":
            self.capturedO += 2
        else:
            raise Exception("Invalid playerID provided")
    
    def update_player(self, player):
        if player == "X":
            self.next_player = "O"
        else:
            self.next_player = "X"
    
    def has_won(self, capturedX, capturedO, player, playerX, playerY):
        if capturedX >= 10:
            return print("X has won!")
        elif capturedO >= 10:
            return print("O has won!")
        else:
            return self.is_five_in_row(player, playerX, playerY)
        
    def is_five_in_row(self, player, playerX, playerY):
        pos = playerX + (19 * playerY) - 1 #-1 to adjust for indexing
        dir_dic = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [-1,-1], [1,-1], [-1,1]]
        for dir in dir_dic:
            has_won = self.check_five_in_row_in_dir(player, pos, 1, dir[0], dir[1])
            if has_won:
                return has_won
        return has_won
    
    # n is the nth row on the board where 0 <= n <= 8
    # dirX and dirY are the direction in which 5-in-a-row is formed. Their values: -1, 0, 1
    def check_five_in_row_in_dir(self, player, pos, n, dirX, dirY):
        nxt = pos + (dirX * 19 * n) + (dirY * n) - 1 #-1 to adjust for indexing
        if nxt > 361:
            return False
        if self.boardState[nxt] != player:
            return False
        if n == 4:
            return True
        else:
            return self.check_five_in_row_in_dir(player, nxt, n+1)
    