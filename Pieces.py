class pieceClass:
    #init
    def __init__(self, pieceName):
        import random
        import TetrisPieces as TP
        self.pieceArray = [[]]
        self.pieceName = pieceName
        self.orientation = 0
        self.maxorientation = 1
        self.img = TP.boximg
        if self.pieceName == "T" : self.maxorientation = 3; self.img = TP.boxblueimg
        if self.pieceName == "Step" : self.maxorientation = 1; self.img = TP.boxyellowimg
        if self.pieceName == "StepR" : self.maxorientation = 1; self.img = TP.boxdarkgreenimg
        if self.pieceName == "L" : self.maxorientation = 3; self.img = TP.boxorangeimg
        if self.pieceName == "J" : self.maxorientation = 3; self.img = TP.boxpinkimg
        if self.pieceName == "I" : self.maxorientation = 1; self.img = TP.boxredimg
        if self.pieceName == "Box" : self.maxorientation = 0; self.img = TP.boxgreenimg
        self.orientation = random.randint(0, self.maxorientation)
        self.checkOrient()


    #Update pieceArray according to orientation
    def checkOrient(self) :
        if self.pieceName == "T":
            if self.orientation == 0 :
                self.pieceArray = [
                                    [1, 1, 1],
                                    [0, 1, 0]
                                  ]
            if self.orientation == 1 :
                self.pieceArray = [
                                    [0, 1],
                                    [1, 1],
                                    [0, 1]
                                  ]
            if self.orientation == 2 :
                self.pieceArray = [
                                    [0, 1, 0],
                                    [1, 1, 1]
                                  ]
            if self.orientation == 3 :
                self.pieceArray = [
                                    [1, 0],
                                    [1, 1],
                                    [1, 0]
                                  ]
        if self.pieceName == "Step":
            if self.orientation == 0 :
                self.pieceArray = [
                                    [0, 1, 1],
                                    [1, 1, 0]
                                    ]
            if self.orientation == 1 :
                self.pieceArray = [
                                    [1, 0],
                                    [1, 1],
                                    [0, 1]
                                    ]
        if self.pieceName == "StepR":
            if self.orientation == 0 :
                self.pieceArray = [
                                    [1, 1, 0],
                                    [0, 1, 1]
                                    ]       
            if self.orientation == 1 :
                self.pieceArray = [
                                    [0, 1],
                                    [1, 1],
                                    [1, 0]
                                    ]
        if self.pieceName == "L":
            if self.orientation == 0 :
                self.pieceArray = [
                                    [1, 1, 1],
                                    [1, 0, 0]
                                    ]
            if self.orientation == 1 :
                self.pieceArray = [
                                    [1, 1],
                                    [0, 1],
                                    [0, 1]
                                    ]
            if self.orientation == 2 :
                self.pieceArray = [
                                    [0, 0, 1],
                                    [1, 1, 1]
                                    ]
            if self.orientation == 3 :
                self.pieceArray = [
                                    [1, 0],
                                    [1, 0],
                                    [1, 1]
                                    ]
        if self.pieceName == "J":
            if self.orientation == 0 :
                self.pieceArray = [
                                    [1, 0, 0],
                                    [1, 1, 1]
                                    ]
            if self.orientation == 1 :
                self.pieceArray = [
                                    [1, 1],
                                    [1, 0],
                                    [1, 0]
                                    ]
            if self.orientation == 2 :
                self.pieceArray = [
                                    [1, 1, 1],
                                    [0, 0, 1]
                                    ]
            if self.orientation == 3 :
                self.pieceArray = [
                                    [0, 1],
                                    [0, 1],
                                    [1, 1]
                                    ]
        if self.pieceName == "I":
            if self.orientation == 0 :
                self.pieceArray = [
                                    [1, 1, 1, 1, 1]
                                    ]
            if self.orientation == 1 :
                self.pieceArray = [
                                    [1],
                                    [1],
                                    [1],
                                    [1],
                                    [1]
                                    ]
        if self.pieceName == "Box":
            self.pieceArray = [
                                [1, 1],
                                [1, 1]
                                ]


    #Blits pieces and species pieceArray
    def drawer(self):
        import TetrisPieces as TP
        while TP.playerX + len(self.pieceArray[0])*TP.boxSide > TP.gameX : TP.playerX -= TP.boxSide
        for y in range(len(self.pieceArray)) :
            for x in range(len(self.pieceArray[0])) :
                if self.pieceArray[y][x] :
                    TP.screen.blit(self.img, (TP.playerX + x*TP.boxSide, TP.playerY + y*TP.boxSide))


    #Change orientation and check if rotation is feasible
    def rotate(self) :
        import TetrisPieces as TP
        if self.orientation == self.maxorientation : self.orientation = 0
        else : self.orientation += 1
        self.checkOrient()
        confirm = True
        if TP.playerY + len(self.pieceArray)*TP.boxSide > TP.gameY : confirm = False
        while TP.playerX + len(self.pieceArray[0])*TP.boxSide > TP.gameX : TP.playerX -= TP.boxSide
        for y in range(len(self.pieceArray)) :
            if not confirm : break
            for x in range(len(self.pieceArray[0])) :
                if TP.mainArray[int(TP.playerY/TP.boxSide)+ y][int(TP.playerX/TP.boxSide) + x] : confirm = False
        if not confirm :
            if self.orientation == 0 : self.orientation = self.maxorientation
            else : self.orientation -= 1
            self.checkOrient()



    #First time blit placed object and enter that in mainArray for further rounds
    def solidify(self) :
        import TetrisPieces as TP
        for x in range(len(self.pieceArray[0])) :
            for y in range(len(self.pieceArray)) :
                if self.pieceArray[y][x] : 
                    #TP.screen.blit(TP.placedimg, (TP.playerX + x*TP.boxSide, TP.playerY + y*TP.boxSide))
                    TP.mainArray[int(TP.playerY/TP.boxSide) + y - 1][int(TP.playerX/TP.boxSide) + x] = True
    


    #Check if colliding with walls of game or horizontal collision with other blocks
    def collisionCheck(self) :
        import TetrisPieces as TP
        if TP.playerX+TP.playerXchange+TP.boxSide <= 0 : TP.playerXchange = 0
        if TP.playerX+TP.playerXchange+(len(self.pieceArray[0]))*TP.boxSide > TP.gameX : TP.playerXchange = 0
        if TP.playerXchange < 0 and TP.playerX+TP.playerXchange >= 0 :
            for i in range(len(self.pieceArray)):
                x = 0
                while (self.pieceArray[i][x] == False) : x += 1
                if TP.mainArray[int(TP.playerY/TP.boxSide) + i][int((TP.playerX+TP.playerXchange)/TP.boxSide) + x] : TP.playerXchange = 0
        if TP.playerXchange > 0 and TP.playerX+TP.playerXchange+(len(self.pieceArray[0]))*TP.boxSide <= TP.gameX :
            for i in range(len(self.pieceArray)):
                x = len(self.pieceArray[0]) - 1
                while (self.pieceArray[i][x] == False) : x -= 1
                if TP.mainArray[int(TP.playerY/TP.boxSide) + i][int((TP.playerX+TP.playerXchange)/TP.boxSide) + x] : TP.playerXchange = 0



    #Check vertical contact
    def checker(self) :
        import TetrisPieces as TP
        for x in range(len(self.pieceArray[0])) :
            for y in range(len(self.pieceArray)) :
                if self.pieceArray[y][x] and ((TP.playerY + TP.boxSide*(len(self.pieceArray)) > TP.gameY) or TP.mainArray[int(TP.playerY/TP.boxSide) + y][int(TP.playerX/TP.boxSide) + x]) :
                    TP.freezesfx.play()
                    self.solidify()
                    TP.playerState = "PLACED"
                    return