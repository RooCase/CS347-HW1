def has_won(capturedX, capturedO):
    if capturedX >= 10:
        return print("X has won!")
    elif capturedO >= 10:
        return print("O has won!")
    #check if five in a row


    
class board:
    def __init__(self):
        boardState = "-------------------"*19
        capturedX = 0
        capturedY = 0


    def updatePoints(self, player):
        if player == "x":
            self.capturedX += 2
        elif player == "y":
            self.capturedy += 2
        else:
            raise Exception("Invalid playerID provided")
