# AESTHETICS

# Draw all placed blocks and check for filled row
def placeAndBreak() :
    import TetrisPieces as TP
    import random
    for arrY in range(len(TP.mainArray)) :
        for arrX in range(len(TP.mainArray[arrY])) :
            if TP.mainArray[arrY][arrX] : TP.screen.blit(random.choice(TP.colorArray),(arrX*TP.boxSide, (arrY+1)*TP.boxSide))
    for arrY in range(len(TP.mainArray)) :
        if TP.mainArray[arrY] == [True for x in range(int(TP.gameX/TP.boxSide))] :
            TP.mainArray.insert(0, [False for x in range(int(TP.gameX/TP.boxSide))])
            TP.mainArray.pop(arrY+1)
            TP.score += 1
            #TP.whatsNext()
            #TP.scoreKeep()
            for x in range(len(TP.mainArray[0])) :
                TP.screen.blit(TP.placedimg, (x*TP.boxSide, (arrY+1)*TP.boxSide))
                if TP.playerState == "FALLING" : TP.piece.drawer()
                TP.pygame.display.update()
                TP.pygame.time.wait(30)



# ABILITIES

# Switch with next piece
def switchPiece() :
    import TetrisPieces as TP
    TP.piece, TP.nextPiece = TP.nextPiece, TP.piece


def drawGhostPiece(indY) :
    import TetrisPieces as TP
    for y in range(0, len(TP.piece.pieceArray)) :
        for x in range(0, len(TP.piece.pieceArray[0])) :
            if TP.piece.pieceArray[y][x] :
                TP.screen.blit(TP.placedimg, (TP.playerX + TP.playerXchange + x*TP.boxSide, (indY+y+1)*TP.boxSide))
    TP.pygame.display.update()

# Ghost holo
def ghostPiece() :
    import TetrisPieces as TP
    arrY = int(TP.playerY/TP.boxSide-1)
    while (arrY >= -1 and arrY + len(TP.piece.pieceArray) <= len(TP.mainArray)) :
        for indY in range(arrY, arrY + len(TP.piece.pieceArray)) :
            for indX in range(int((TP.playerX + TP.playerXchange)/TP.boxSide), int((TP.playerX+TP.playerXchange)/TP.boxSide + len(TP.piece.pieceArray[0]))) :
                if (TP.piece.pieceArray[indY-arrY][indX-int((TP.playerX+TP.playerXchange)/TP.boxSide)] and TP.mainArray[indY][indX])  :
                    drawGhostPiece(arrY-1)
                    return
        arrY += 1
    else :
        drawGhostPiece(len(TP.mainArray) - len(TP.piece.pieceArray))

# Slow Motion
def SloMo() :
    import TetrisPieces as TP
    TP.tickdelay *= 2

# Break 2 bottom lines
def breakLines () :
    import TetrisPieces as TP
    maxPlace = 5
    for y in range(len(TP.mainArray)-1,  0, -1) :
        for x in range(0, len(TP.mainArray[0])) :
            if maxPlace > 0 and TP.mainArray[y][x] == False :
                TP.mainArray[y][x] = True
                maxPlace -= 1
    


# DIFFICULTIES

# Decrease in Time Delay
def getTick() :
    import TetrisPieces as TP
    return (TP.defaultTick - (TP.score // 5) * 12.5)

def randomPieceDrop() :
    import TetrisPieces as TP
    switch = True
    workXList = [x for x in range(0, len(TP.indXList))]
    while switch :
        for playerNo in workXList :
            if TP.indYList[playerNo] >= len(TP.mainArray) - 1 or TP.mainArray[TP.indYList[playerNo]+1][TP.indXList[playerNo]] : 
                TP.mainArray[TP.indYList[playerNo]][TP.indXList[playerNo]] = True
                workXList.remove(playerNo)
            TP.screen.blit(TP.boximg, (TP.indXList[playerNo] * TP.boxSide, (TP.indYList[playerNo]+1) * TP.boxSide))
            TP.indYList[playerNo] += 1
        if len(workXList) == 0 : return
        TP.pygame.time.wait(5)
        TP.pygame.display.update()