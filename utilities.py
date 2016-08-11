import sys, pygame
from pygame.locals import *
from constants import *


def mainMenu():
    #  Title variables
    fontObjTitle = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObjTitle = fontObjTitle.render('PyRPG', True, RED, WHITE)
    textRectObjTitle = textSurfaceObjTitle.get_rect()
    textRectObjTitle.center = (CENTERX, 50)

    #  Subtitle variables
    fontObjSubitle = pygame.font.Font('freesansbold.ttf', 18)
    textSurfaceObjSubtitle = fontObjSubitle.render('Press Space to Start, H for help, ESC to exit the game', True, BLUE, WHITE)
    textRectObjSubtitle = textSurfaceObjSubtitle.get_rect()
    textRectObjSubtitle.center = (CENTERX, 120)

    menuAppeared = False
    while True:  # the main menu loop
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(textSurfaceObjTitle, textRectObjTitle)
        if menuAppeared:
            DISPLAYSURF.blit(textSurfaceObjSubtitle, textRectObjSubtitle)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE and menuAppeared:
                    DISPLAYSURF.fill(WHITE)
                    return
                elif event.key == K_h:
                    helpMenu()
                elif event.key == K_ESCAPE:
                    terminate()
                if not menuAppeared:
                    menuAppeared = True

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def helpMenu():
    fontObjHelp = pygame.font.Font('freesansbold.ttf', 18)
    textSurfaceObjHelp = fontObjHelp.render('Press esc to go back in main menu,', True, BLACK, WHITE)
    textRectObjHelp = textSurfaceObjHelp.get_rect()
    textRectObjHelp.x = 10
    textRectObjHelp.y = 10 

    while True:  # the main menu loop
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(textSurfaceObjHelp, textRectObjHelp)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    DISPLAYSURF.fill(WHITE)
                    return

        pygame.display.update()
        FPSCLOCK.tick(FPS)		

def convertMap(filepath):
    with open(filepath, "r") as ins:
        lineArray = []
        for line in ins:
            lineArray.append(line)
    return zip(*lineArray)

def convertMapToTile(mapArray):
    tileArray = []
    for column in mapArray:
        for char in column:
            if char == ' ':
                tileArray.append(tiles['grass'])
            elif char == 'W':
                tileArray.append(tiles['water'])
            elif char == 'T':
                tileArray.append(tiles['tree'])
            elif char == '#':
                tileArray.append(tiles['wall'])
        tileArray.append('\n')

    return tileArray

def drawMap(tileArray):
    x = OFFSETX
    y = OFFSETY
    for tile in tileArray:
        if tile == '\n':
            x += TILESIDE
            y = OFFSETY
        else:
            DISPLAYSURF.blit(tile, (x, y))
            y += TILESIDE

def setPlayerStartingPoint(mapArray):
    playerPos = []
    for i,column in enumerate(mapArray):
        for j,char in enumerate(column):
            if char == ' ':
                playerPos.append(i)
                playerPos.append(j)
                return playerPos

    return playerPos

def createWalkabilityMap(mapArray):
    mapToReturn = []
    columnToAppend = []
    print mapArray
    for column in mapArray:
        for char in column:
            if char == ' ':
                columnToAppend.append(True)
            else:
                columnToAppend.append(False)
        mapToReturn.append(columnToAppend)
        columnToAppend = []
    return mapToReturn
                
def terminate():
	pygame.quit()
	sys.exit()