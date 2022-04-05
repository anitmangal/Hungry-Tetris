import pygame
import Pieces
import random
import sys
import os
import Abilities_and_Aesthetics

#For compiling into a single exe
def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.init()

#Initialize
screenX = 700
screenY = 750
gameX = 450
gameY = 700
boxSide = 25
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Tetris")
iconurl = resource_path('Assets/icon.png')
icon = pygame.image.load(iconurl)
pygame.display.set_icon(icon)
playerState = "PLACED"
gameover = False
run = True
score = 0        
playerX = gameX/2
playerY = 0
piecesArray = ["T", "L", "J", "Step", "StepR", "I", "Box"]
defaultTick = 200
ghostSwitch = False
ghostTime = 5000
slomoSwitch = False
slomoTime = 5000
breaklinesSwitch = False
lastRandomPieceScore = 0


#Load Images
boximgurl = resource_path('Assets/box.png')
boximg = pygame.image.load(boximgurl)
placedimgurl = resource_path('Assets/placed.png')
placedimg = pygame.image.load(placedimgurl)
placedredurl = resource_path('Assets/placedred.png')
placedred = pygame.image.load(placedredurl)
placedorangeurl = resource_path('Assets/placedorange.png')
placedorange = pygame.image.load(placedorangeurl)
placedyellowurl = resource_path('Assets/placedyellow.png')
placedyellow = pygame.image.load(placedyellowurl)
placedgreenurl = resource_path('Assets/placedgreen.png')
placedgreen = pygame.image.load(placedgreenurl)
placedblueurl = resource_path('Assets/placedblue.png')
placedblue = pygame.image.load(placedblueurl)
gamebgimgurl = resource_path('Assets/game.png')
gamebgimg = pygame.image.load(gamebgimgurl)
gothicfonturl = resource_path('Assets/GOTHIC.TTF')


colorArray = [placedred, placedorange, placedyellow, placedgreen, placedblue]

#Array to Remember Placed Objects
mainArray = [[False for x in range(int(gameX/boxSide))] for y in range(int(gameY/boxSide))]



#Game Over Screen
def gameOver():
    global score, gothicfonturl
    screen.fill((0,0,0))
    font = pygame.font.Font(gothicfonturl, 40)
    overText = font.render("GAME OVER", True, (255,255,255))
    screen.blit(overText, (200,270))
    finalScore = font.render("Score : "+str(score), True, (255,255,255))
    screen.blit(finalScore, (250, 400))
    pygame.display.update()


#Score Display
def scoreKeep():
    global score, gothicfonturl
    font = pygame.font.Font(gothicfonturl, 24)
    scoreText = font.render("Score : "+str(score), True, (255,255,255))
    screen.blit(scoreText, (gameX+75, gameY/2))

#Pause Menu
def pauseMenu() :
    overlayimg = gamebgimg.convert_alpha()
    #alpha = 128
    #overlayimg.fill((255,255,255, alpha), None, pygame.BLEND_RGBA_MULT)
    overlayimg.set_alpha(128)
    screen.blit(overlayimg, (0, boxSide))
    pygame.display.update()
    pauseSwitch = True
    while pauseSwitch :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE : 
                    pygame.quit()
                    quit()
                if event.key == pygame.K_RETURN : pauseSwitch = False
    return

#Get next piece for the start only
nextPiece = Pieces.pieceClass(piecesArray[random.randint(0, len(piecesArray)-1)])


#Print next piece
def whatsNext() :
    font = pygame.font.Font(gothicfonturl, 24)
    nextText = font.render("Next Piece", True, (255,255,255))
    screen.blit(nextText, (gameX+50, gameY/2 + 150))
    for y in range(len(nextPiece.pieceArray)):
        for x in range(len(nextPiece.pieceArray[0])) :
            if nextPiece.pieceArray[y][x] :
                screen.blit(boximg, (gameX + 100 + (x-len(nextPiece.pieceArray[0])//2)*boxSide,  gameY/2 + 200 + y*boxSide))
                
                
#Game Loop
while run:

    #DEFAULTS
    tickdelay = Abilities_and_Aesthetics.getTick()
    if tickdelay < 100 : tickdelay = 100
    playerXchange = 0
    playerYchange = boxSide
    screen.fill((0,0,0))
    if playerState == "PLACED" :
        piece = nextPiece
        nextPiece = Pieces.pieceClass(piecesArray[random.randint(0, len(piecesArray)-1)])
        playerX = gameX/2
        playerY = 0
        playerState = "FALLING"
    screen.blit(gamebgimg, (0,boxSide))
    pauseSwitch = False




    #INPUTS
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            run = False
            pygame.display.quit()
            pygame.quit()
            sys.exit()
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT : playerXchange = 0-boxSide
            if event.key == pygame.K_RIGHT : playerXchange = boxSide
            if event.key == pygame.K_DOWN : tickdelay = tickdelay/2
            if event.key == pygame.K_SPACE : piece.rotate()
            if event.key == pygame.K_s : Abilities_and_Aesthetics.switchPiece()
            if event.key == pygame.K_ESCAPE : pauseSwitch = True
            if event.key == pygame.K_g : ghostSwitch = not ghostSwitch
            if event.key == pygame.K_f : slomoSwitch = not slomoSwitch
            if event.key == pygame.K_d : breaklinesSwitch = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: playerXchange = 0-boxSide
    if keys[pygame.K_RIGHT]: playerXchange = boxSide
    if keys[pygame.K_DOWN] : tickdelay = tickdelay/2




    #Check if colliding with walls of game or horizontal collision with other blocks
    piece.collisionCheck()

    if slomoSwitch :
        if slomoTime > 0 :
            Abilities_and_Aesthetics.SloMo()
            slomoTime -= tickdelay
        else :
            slomoSwitch = False
            slomoTime = 5000

    
    if ghostSwitch : 
        if (ghostTime > 0) :
            Abilities_and_Aesthetics.ghostPiece()
            ghostTime -= tickdelay
        else : 
            ghostSwitch = False
            ghostTime = 5000


    #Set New Coords
    playerX += playerXchange
    playerY += playerYchange




    #Gameover
    for x in range(len(mainArray[0])):
        if mainArray[0][x] : 
            gameover = True
            run = False
            break
    if run == False : break



    if breaklinesSwitch :
        Abilities_and_Aesthetics.breakLines()
        breaklinesSwitch = False

    #Draw piece and check vertical collisions to solidify
    piece.drawer()
    piece.checker()


    
    #UPDATE
    whatsNext()
    scoreKeep()

    Abilities_and_Aesthetics.placeAndBreak()

    
    if score == lastRandomPieceScore + 5 and playerState == "PLACED" :
        noOfBlocks = 8
        indXList = [random.randint(0, len(mainArray[0])-1) for x in range(noOfBlocks)]
        indYList = [0 for x in range(noOfBlocks)]
        Abilities_and_Aesthetics.randomPieceDrop()
        lastRandomPieceScore = score


    
    if pauseSwitch : pauseMenu()
    pygame.display.update()
    pygame.time.wait(int(tickdelay))


while gameover : 
    gameOver()
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
           gameover = False
           pygame.display.quit()
           pygame.quit()
           sys.exit()