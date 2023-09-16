#gamestate is in the format of player#board#capturedX#capturedO
 
class Board:
    def __init__(self):
        next_player = ""
        boardState = "-------------------"*19
        capturedX = 0
        capturedY = 0

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
    
    def has_won(capturedX, capturedO, playerX, playerY):
        if capturedX >= 10:
            return print("X has won!")
        elif capturedO >= 10:
            return print("O has won!")
        else:
            return self.is_five_in_row(playerX, playerY)
        
    def is_five_in_row(self, playerX, playerY):
        pos = playerX + (19 * playerY)
        dir_dic = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [-1,-1], [1,-1], [-1,1]]
        for dir in dir_dic:
            return self.check_five_in_row_in_dir(pos, 1, dir[0], dir[1])
    
    # n is the nth row on the board where 0 <= n <= 8
    # dirX and dirY are the direction in which 5-in-a-row is formed. Their values: -1, 0, 1
    def check_five_in_row_in_dir(pos, n, dirX, dirY):
        nxt = pos + (dirX * 19 * n) + (dirY * n)
        if nxt > 361:
            return False
        if n == 4:
            return True
        else:
            return self.check_five_in_row_in_dir(nxt, n+1)
    
