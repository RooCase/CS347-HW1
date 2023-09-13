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
