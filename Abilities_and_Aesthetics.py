# AESTHETICS

# Draw all placed blocks and check for filled row
def placeAndBreak() :
    import TetrisPieces as TP
    import random
    spriteY = TP.boxSide - 23
    spriteX = TP.gameX + TP.boxSide*1.5
    for arrY in range(len(TP.mainArray)) :
        for arrX in range(len(TP.mainArray[arrY])) :
            if TP.mainArray[arrY][arrX] : TP.screen.blit(random.choice(TP.colorArray),(arrX*TP.boxSide, (arrY+1)*TP.boxSide))
    for arrY in range(len(TP.mainArray)) :
        if TP.mainArray[arrY] == [True for x in range(int(TP.gameX/TP.boxSide))] :
            if (arrY*TP.boxSide - spriteY > 5*TP.boxSide) : TP.footstepsfx.play()
            while spriteY < arrY*TP.boxSide :
                TP.screen.blit(TP.sprite2img, (spriteX, spriteY))
                TP.pygame.display.update()
                TP.pygame.time.wait(1)
                TP.pygame.draw.rect(TP.screen, TP.bgColor, TP.pygame.Rect([spriteX, spriteY], TP.sprite2img.get_size()))
                spriteY += 5
            TP.screen.blit(TP.sprite1img, (spriteX, spriteY))
            TP.mainArray.insert(0, [False for x in range(int(TP.gameX/TP.boxSide))])
            TP.mainArray.pop(arrY+1)
            TP.score += 1    
            if (TP.score > TP.lastAbilityScore and TP.score%6 == 0) : 
                giveAbilities()
                TP.lastAbilityScore = TP.score
            TP.linebreaksfx.play()
            for x in range(len(TP.mainArray[0])) :
                TP.screen.blit(TP.placedimg, (x*TP.boxSide, (arrY+1)*TP.boxSide))
                if TP.playerState == "FALLING" : TP.piece.drawer()
                TP.pygame.display.update()
                TP.pygame.time.wait(30)
            TP.screen.blit(TP.placedimg, (TP.gameX,(arrY+1)*TP.boxSide))
            TP.screen.blit(TP.sprite2img, (spriteX, spriteY))
            TP.pygame.time.wait(40)
        else :
            TP.screen.blit(TP.sprite2img, (spriteX, spriteY))
    if (spriteY - TP.boxSide - 23 > 5*TP.boxSide) : TP.footstepsrevsfx.play()
    while spriteY > TP.boxSide-23 :
        TP.screen.blit(TP.sprite2img, (spriteX, spriteY))
        TP.pygame.display.update()
        TP.pygame.time.wait(1)
        TP.pygame.draw.rect(TP.screen, TP.bgColor, TP.pygame.Rect([spriteX, spriteY], TP.sprite2img.get_size()))
        spriteY -= 5
    else :
        TP.screen.blit(TP.sprite2img, (spriteX, spriteY))


def giveAbilities() :
    import TetrisPieces as TP
    import random
    lst = ["Switch", "Fill", "SlowMo", "Ghost"]
    res = lst[random.randint(0, 3)]
    if res == "Switch" : TP.switchCount += 1
    if res == "Fill" : TP.breaklinesCount += 1
    if res == "SlowMo" : TP.slomoCount += 1
    if res == "Ghost" : TP.ghostCount += 1
    TP.abilityunlocksfx.play()

def hungryBar() :
    import TetrisPieces as TP
    font = TP.pygame.font.Font(TP.fonturl, 24)
    TP.screen.blit(font.render("TUMMY", True, (0,0,0)), (TP.gameX+7.5*TP.boxSide, TP.gameY-12*TP.boxSide-5))
    TP.pygame.draw.rect(TP.screen, (0,0,0), TP.pygame.Rect([TP.gameX+8*TP.boxSide, TP.gameY - 11*TP.boxSide], (2*TP.boxSide, 5*TP.boxSide)))
    n = TP.score%6
    if (n >= 1) : TP.screen.blit(TP.pygame.transform.scale(TP.boxblueimg, (2*TP.boxSide, TP.boxSide)), (TP.gameX+8*TP.boxSide, TP.gameY - 7*TP.boxSide))
    if (n >= 2) : TP.screen.blit(TP.pygame.transform.scale(TP.boxyellowimg, (2*TP.boxSide, TP.boxSide)), (TP.gameX+8*TP.boxSide, TP.gameY - 8*TP.boxSide))
    if (n >= 3) : TP.screen.blit(TP.pygame.transform.scale(TP.boxgreenimg, (2*TP.boxSide, TP.boxSide)), (TP.gameX+8*TP.boxSide, TP.gameY - 9*TP.boxSide))
    if (n >= 4) : TP.screen.blit(TP.pygame.transform.scale(TP.boxorangeimg, (2*TP.boxSide, TP.boxSide)), (TP.gameX+8*TP.boxSide, TP.gameY - 10*TP.boxSide))
    if (n >= 5) : TP.screen.blit(TP.pygame.transform.scale(TP.boxredimg, (2*TP.boxSide, TP.boxSide)), (TP.gameX+8*TP.boxSide, TP.gameY - 11*TP.boxSide))
    TP.screen.blit(font.render("ABILITIES", True, (0,0,0)), (TP.gameX + 7*TP.boxSide, TP.gameY - 18*TP.boxSide))
    TP.screen.blit(font.render("Switch Pieces [S] : "+str(TP.switchCount), True, (0,0,0)), (TP.gameX + 4.5*TP.boxSide, TP.gameY - 17*TP.boxSide))
    TP.screen.blit(font.render("Slow Motion [D] : "+str(TP.slomoCount), True, (0,0,0)), (TP.gameX + 4.5*TP.boxSide, TP.gameY - 16*TP.boxSide))
    TP.screen.blit(font.render("Fill 5 Pieces [F] : "+str(TP.breaklinesCount), True, (0,0,0)), (TP.gameX + 4.5*TP.boxSide, TP.gameY - 15*TP.boxSide))
    TP.screen.blit(font.render("Ghost Piece [G] : "+str(TP.ghostCount), True, (0,0,0)), (TP.gameX + 4.5*TP.boxSide, TP.gameY - 14*TP.boxSide))




# ABILITIES

# Switch with next piece
def switchPiece() :
    import TetrisPieces as TP
    TP.abilityusesfx.play()
    TP.piece, TP.nextPiece = TP.nextPiece, TP.piece


def drawGhostPiece(indY) :
    import TetrisPieces as TP
    ghostplacedimg = TP.placedimg.convert_alpha()
    ghostplacedimg.set_alpha(128)
    for y in range(0, len(TP.piece.pieceArray)) :
        for x in range(0, len(TP.piece.pieceArray[0])) :
            if TP.piece.pieceArray[y][x] :
                TP.screen.blit(ghostplacedimg, (TP.playerX + TP.playerXchange + x*TP.boxSide, (indY+y+1)*TP.boxSide))\

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
    TP.randomBlockssfx.play()
    while switch :
        for playerNo in workXList :
            if TP.indYList[playerNo] >= len(TP.mainArray) - 1 or TP.mainArray[TP.indYList[playerNo]+1][TP.indXList[playerNo]] : 
                TP.mainArray[TP.indYList[playerNo]][TP.indXList[playerNo]] = True
                workXList.remove(playerNo)
            TP.screen.blit(TP.placedimg, (TP.indXList[playerNo] * TP.boxSide, (TP.indYList[playerNo]+1) * TP.boxSide))
            TP.indYList[playerNo] += 1
        if len(workXList) == 0 : switch = False
        TP.pygame.time.wait(10)
        TP.pygame.display.update()