from types import resolve_bases
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
screenX = 800
screenY = 750
gameX = 450
gameY = 700
bgColor = (0, 191, 255)
boxSide = 25
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Hungry Tetris")
iconurl = resource_path(r'Assets\icon.png')
icon = pygame.image.load(iconurl)
pygame.display.set_icon(icon)
playerState = "PLACED"
gameover = False
mainScreen = True
run = True
score = 0        
playerX = gameX/2
playerY = 0
piecesArray = ["T", "L", "J", "Step", "StepR", "I", "Box"]
defaultTick = 200
switchCount = 0
ghostSwitch = False
ghostCount = 0
ghostTime = 20000
slomoSwitch = False
slomoCount = 0
slomoTime = 20000
breaklinesSwitch = False
breaklinesCount = 0
lastRandomPieceScore = 0
lastAbilityScore = 0     

#Load Images
boximgurl = resource_path(r'Assets\box.png')
boximg = pygame.image.load(boximgurl)
placedimgurl = resource_path(r'Assets\placed.png')
placedimg = pygame.image.load(placedimgurl)
placedredurl = resource_path(r'Assets\placedred.png')
placedred = pygame.image.load(placedredurl)
placedorangeurl = resource_path(r'Assets\placedorange.png')
placedorange = pygame.image.load(placedorangeurl)
placedyellowurl = resource_path(r'Assets\placedyellow.png')
placedyellow = pygame.image.load(placedyellowurl)
placedgreenurl = resource_path(r'Assets\placedgreen.png')
placedgreen = pygame.image.load(placedgreenurl)
placedblueurl = resource_path(r'Assets\placedblue.png')
placedblue = pygame.image.load(placedblueurl)
gamebgimgurl = resource_path(r'Assets\tetrisBG.png')
gamebgimg = pygame.image.load(gamebgimgurl)
fonturl = resource_path(r'Assets\GOTHIC.TTF')
logoimg = pygame.image.load(resource_path(r'Assets\Logo.png'))
pausemenuimg = pygame.image.load(resource_path(r'Assets\game.png'))
gameoverimg = pygame.image.load(resource_path(r'Assets\gameoverscreen.png'))
spriteurl = resource_path(r'Assets\Pixel\sprite.png')
spriteimg = pygame.image.load(spriteurl)
sprite1url = resource_path(r'Assets\Pixel\sprite1.png')
sprite1img = pygame.image.load(sprite1url)
sprite2url = resource_path(r'Assets\Pixel\sprite2.png')
sprite2img = pygame.image.load(sprite2url)
boxblueimg = pygame.image.load(resource_path(r'Assets\boxblue.png'))
boxyellowimg = pygame.image.load(resource_path(r'Assets\boxyellow.png'))
boxgreenimg = pygame.image.load(resource_path(r'Assets\boxgreen.png'))
boxorangeimg = pygame.image.load(resource_path(r'Assets\boxorange.png'))
boxpinkimg = pygame.image.load(resource_path(r'Assets\boxpink.png'))
boxredimg = pygame.image.load(resource_path(r'Assets\boxred.png'))
boxdarkgreenimg = pygame.image.load(resource_path(r'Assets\boxdarkgreen.png'))
mainframe1 = pygame.image.load(resource_path(r'Assets\MainScreen\1.png'))
mainframe2 = pygame.image.load(resource_path(r'Assets\MainScreen\2.png'))
mainframe3 = pygame.image.load(resource_path(r'Assets\MainScreen\3.png'))
mainframe4 = pygame.image.load(resource_path(r'Assets\MainScreen\4.png'))
mainframe5 = pygame.image.load(resource_path(r'Assets\MainScreen\5.png'))
mainframe6 = pygame.image.load(resource_path(r'Assets\MainScreen\6.png'))

#Loading Audio
music = pygame.mixer.music.load(resource_path(r'Assets\Sounds\Tetris_Theme.wav'))
gameoversfx = pygame.mixer.Sound(resource_path(r'Assets\Sounds\GameOver.wav'))
linebreaksfx = pygame.mixer.Sound(resource_path(r'Assets\Sounds\LineBreak.wav'))
abilityunlocksfx = pygame.mixer.Sound(resource_path(r'Assets\Sounds\AbilityUnlock.wav'))
randomBlockssfx = pygame.mixer.Sound(resource_path(r'Assets\Sounds\RandomBlocks.wav'))
abilityusesfx = pygame.mixer.Sound(resource_path(r'Assets\Sounds\AbilityUse.wav'))
freezesfx = pygame.mixer.Sound(resource_path(r'Assets\Sounds\freeze.wav'))
footstepsfx = pygame.mixer.Sound(resource_path(r'Assets\Sounds\footsteps.wav'))
footstepsrevsfx = pygame.mixer.Sound(resource_path(r'Assets\Sounds\footsteps.wav'))

colorArray = [placedred, placedorange, placedyellow, placedgreen, placedblue]

#Array to Remember Placed Objects
mainArray = [[False for x in range(int(gameX/boxSide))] for y in range(int(gameY/boxSide))]



#Game Over Screen
def gameOver():
    global score, fonturl
    screen.blit(gameoverimg, (0,0))
    font = pygame.font.Font(fonturl, 40)
    finalScore = font.render("Score : "+str(score), True, (255,255,255))
    screen.blit(finalScore, ((screenX-finalScore.get_size()[0]) / 2, 400))
    EscapeToExit = font.render("Press <escape> to Exit", True, (255,255,255))
    screen.blit(EscapeToExit, ((screenX - EscapeToExit.get_size()[0])/2, 450))
    EnterToRestart = font.render("Press <enter> to Restart", True, (255,255,255))
    screen.blit(EnterToRestart, ((screenX - EnterToRestart.get_size()[0])/2, 500))
    pygame.display.update()


#Score Display
def scoreKeep():
    global score, fonturl
    font = pygame.font.Font(fonturl, 24)
    scoreText = font.render("Score : "+str(score), True, (0,0,0))
    screen.blit(scoreText, (gameX+7*boxSide, 8*boxSide))

#Pause Menu
def pauseMenu() :
    overlayimg = pausemenuimg.convert_alpha()
    overlayimg.set_alpha(128)
    screen.blit(overlayimg, (0, 0))
    font = pygame.font.Font(fonturl, 40)
    PausedText = font.render("GAME PAUSED", True, (0,0,0))
    screen.blit(PausedText, ((gameX-PausedText.get_size()[0])/2, gameY/2 - boxSide))
    font1 = pygame.font.Font(fonturl, 24)
    EnterToContinue = font1.render("Press <enter> to Continue", True, (0,0,0))
    screen.blit(EnterToContinue, ((gameX - EnterToContinue.get_size()[0])/2, gameY/2 + 2*boxSide))
    EscapeToExit = font1.render("Press <escape> to Exit", True, (0,0,0))
    screen.blit(EscapeToExit, ((gameX - EscapeToExit.get_size()[0])/2, gameY/2 + 3*boxSide))
    pygame.display.update()
    pauseSwitch = True
    while pauseSwitch :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE : 
                    pygame.quit()
                    sys.exit()
                    break
                if event.key == pygame.K_RETURN : pauseSwitch = False
    return

#Get next piece for the start only
nextPiece = Pieces.pieceClass(piecesArray[random.randint(0, len(piecesArray)-1)])


#Print next piece
def whatsNext() :
    font = pygame.font.Font(fonturl, 24)
    nextText = font.render("Next Piece", True, (0,0,0))
    screen.blit(nextText, (gameX+7*boxSide, gameY - 5*boxSide))
    for y in range(len(nextPiece.pieceArray)):
        for x in range(len(nextPiece.pieceArray[0])) :
            if nextPiece.pieceArray[y][x] :
                screen.blit(nextPiece.img, (gameX + 9.5*boxSide + (x-len(nextPiece.pieceArray[0])/2)*boxSide,  gameY + (y-1.25-(len(nextPiece.pieceArray)/2))*boxSide))

while (True) :
    #Initialize
    playerState = "PLACED"
    gameover = False
    mainScreen = True
    run = True
    score = 0        
    playerX = gameX/2
    playerY = 0
    defaultTick = 200
    switchCount = 0
    ghostSwitch = False
    ghostCount = 0
    ghostTime = 20000
    slomoSwitch = False
    slomoCount = 0
    slomoTime = 20000
    breaklinesSwitch = False
    breaklinesCount = 0
    lastRandomPieceScore = 0
    lastAbilityScore = 0                
    mainArray = [[False for x in range(int(gameX/boxSide))] for y in range(int(gameY/boxSide))]

    i = 1
    pygame.mixer.music.play(-1)
    while mainScreen:
        screen.blit(logoimg, ((screenX-logoimg.get_size()[0])/2, 5*boxSide))
        if i == 1 : screen.blit(mainframe1, (0,0))
        if i == 2 : screen.blit(mainframe2, (0,0))
        if i == 3 : screen.blit(mainframe3, (0,0))
        if i == 4 : screen.blit(mainframe4, (0,0))
        if i == 5 : screen.blit(mainframe5, (0,0))
        if i == 6 : 
            screen.blit(mainframe6, (0,0))
            i = 0
        i += 1
        pygame.time.wait(250)
        pygame.display.update()
        font = pygame.font.Font(fonturl, 30)
        enterText = font.render("<press any key to continue>", True, (255,255,255))
        screen.blit(enterText, ((screenX - enterText.get_size()[0])/2, 20*boxSide))
        pygame.time.wait(250)
        pygame.display.update()
        for event in pygame.event.get() :
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) :
                mainScreen = False
                run = False
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.KEYDOWN :
                mainScreen = False
                break

    #Game Loop
    while run:

        #DEFAULTS
        tickdelay = Abilities_and_Aesthetics.getTick()
        if tickdelay < 100 : tickdelay = 100
        playerXchange = 0
        playerYchange = boxSide
        screen.fill(bgColor)
        if playerState == "PLACED" :
            piece = nextPiece
            nextPiece = Pieces.pieceClass(piecesArray[random.randint(0, len(piecesArray)-1)])
            playerX = gameX/2
            playerY = 0
            playerState = "FALLING"
        screen.blit(gamebgimg, (0,0))
        screen.blit(pygame.transform.scale(logoimg, (8*boxSide,8*boxSide*300/524)), (gameX+5*boxSide, 3*boxSide))
        pauseSwitch = False
        breaklinesSwitch = False


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
                if event.key == pygame.K_s : 
                    if switchCount > 0 : 
                        Abilities_and_Aesthetics.switchPiece()
                        switchCount -= 1
                if event.key == pygame.K_ESCAPE : pauseSwitch = True
                if event.key == pygame.K_g : 
                    if ghostCount > 0 :
                        ghostSwitch = True
                        abilityusesfx.play()
                        ghostCount -= 1
                if event.key == pygame.K_d : 
                    if slomoCount > 0 : 
                        slomoSwitch = True
                        abilityusesfx.play()
                        slomoCount -= 1
                if event.key == pygame.K_f : breaklinesSwitch = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: playerXchange = 0-boxSide
        if keys[pygame.K_RIGHT]: playerXchange = boxSide
        if keys[pygame.K_DOWN] : tickdelay = tickdelay/2




        #Check if colliding with walls of game or horizontal collision with other blocks
        piece.collisionCheck()

        if slomoSwitch:
            if (slomoTime > 0) :
                Abilities_and_Aesthetics.SloMo()
                slomoTime -= tickdelay
            else :
                slomoSwitch = False
                slomoTime = 20000

    
        if ghostSwitch : 
            if (ghostTime > 0) :
                Abilities_and_Aesthetics.ghostPiece()
                ghostTime -= tickdelay
            else : 
                ghostSwitch = False
                ghostTime = 20000


        #Set New Coords
        playerX += playerXchange
        playerY += playerYchange




        #Gameover
        for x in range(len(mainArray[0])):
            if mainArray[0][x] : 
                gameover = True
                run = False
                pygame.mixer.music.stop()
                gameoversfx.play()
                break
        if run == False : break



        if breaklinesSwitch and breaklinesCount > 0 :
            abilityusesfx.play()
            Abilities_and_Aesthetics.breakLines()
            breaklinesSwitch = False
            breaklinesCount -= 1

        #Draw piece and check vertical collisions to solidify
        piece.drawer()
        piece.checker()


    
        #UPDATE
        whatsNext()
        scoreKeep()
        Abilities_and_Aesthetics.hungryBar()
        Abilities_and_Aesthetics.placeAndBreak()
    
        if score >= lastRandomPieceScore + 2 and playerState == "PLACED" :
            noOfBlocks = 8
            indXList = [random.randint(0, len(mainArray[0])-1) for x in range(noOfBlocks)]
            indYList = [0 for x in range(noOfBlocks)]
            Abilities_and_Aesthetics.randomPieceDrop()
            lastRandomPieceScore = score


    
        if pauseSwitch :
            pygame.mixer.music.pause()
            pauseMenu()
            pygame.mixer.music.unpause()
        pygame.display.update()
        pygame.time.wait(int(tickdelay))


    while gameover : 
        gameOver()
        for event in pygame.event.get() :
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) :
               gameover = False
               pygame.display.quit()
               pygame.quit()
               sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN :
               gameover = False
               break