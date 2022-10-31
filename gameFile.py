from boardFile import GameBoard
class Game:
    def __init__(self, board1):
        self.gameBoard = board1

    def startGame(self, board1, p1, p2):
        print(board1.getGB())
        if board1.getSum():
            print("There are  pieces on the board")
        else:
            print("There are no pieces on the board and ")
        while board1.getSum():

            goAgainO = True
            while goAgainO == True:
                playerOnePit = int(input("Enter pit for player one indexes (1-6)inclusive, top row:"))
                playerOneRow = int(input("Enter '0' if player one:"))
                goAgainO = board1.altMove(playerOneRow, playerOnePit)

            goAgainT = True
            while goAgainT == True:
                playertwoPit = int(input("Enter pit for player two indexes (0-5 inclusive bottom row):"))
                playertwoRow = int(input("Enter '1' if player two:"))
                goAgainT = board1.altMove(playertwoRow, playertwoPit)

        if board1.GB[0][0] > board1.GB[1][6]:
            print("Player one wins with score of:" , str(board1.GB[0][0]))
        else:
            print("Player two wins with score of:", str(board1.GB[1][6]))
