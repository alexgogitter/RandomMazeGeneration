import sys
import pygame
import MazeGenAlgorithm
import secrets
from operator import attrgetter, pos

pygame.init()

windowDimensions = (800, 600)
bgColour = (8, 8, 8)

edges = []
openList = []
closedList = []
possibleRoute = []
path = []

displayName = ("Random Maze Generation Version 0")

displaySurface = pygame.display.set_mode(windowDimensions)

pygame.display.set_caption(displayName)

running = True
mazeComplete = False
mazeStart = None
mazeEndSel = False
pathFound = False


nodeMatrix = MazeGenAlgorithm.generateMazeBase(windowDimensions, 10, edges,)



def checkPos(mousePosition):
    
    normalisedMousePosition = mousePosition[0]//10, mousePosition[1]//10

    if not nodeMatrix[normalisedMousePosition[0]][normalisedMousePosition[1]].getEState():

        pygame.draw.rect(displaySurface, (255, 91, 69, 10), (normalisedMousePosition[0] * 10, normalisedMousePosition[1] * 10, 10, 10), 2,)


def drawNodes(nodeMat):

    matrix = nodeMat

    for x in matrix:

        for y in x:

            y.drawNode(displaySurface)


def randEdge():

    mazeEdgeNode = secrets.choice(edges)

    mazeEdgeNode.setStart(True)

    mazeEdgeNode.setEState(False)

    edges.remove(mazeEdgeNode)

    return mazeEdgeNode


def randNode():
    matX = secrets.choice(nodeMatrix)

    node = secrets.choice(matX)

    node.setStart(True)

    return node


mazeStart = randEdge()


possibleRoute.append(mazeStart)
        
pathStack = []

nodeBuffer = []

walking = False

unvisitedNodes = []

pathStack.append(mazeStart)  
 

while running:

    displaySurface.fill(bgColour)

    drawNodes(nodeMatrix)

    if not mazeComplete:

        print("maze creation loop")

        ##place the maze generation algorithms in here.

        pass

    else:

        checkPos(pygame.mouse.get_pos())

    if mazeEndSel and mazeComplete and not pathFound:

        for i in openList:

            posTemp = i.getPosition()

            pygame.draw.rect(displaySurface, (16, 16, 240), ((posTemp[0]*10) + 1, (posTemp[1]*10) + 1 , 8, 8,), 0,)

        for n in closedList:

            posTemp = n.getPosition()

            pygame.draw.rect(displaySurface, (255, 118, 64), ((posTemp[0]*10) + 1, (posTemp[1]*10) + 1 , 8, 8,), 0,)


    mazeStart.drawNode(displaySurface)

    for node in pathStack:

        node.drawAsFrontier(displaySurface)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and mazeComplete:
            if pygame.mouse.get_pressed(num_buttons=3)[0] == True:

                pathFound = False

                for i in path:
                    i.setPath(False)

                path.clear()

                mazeEndSel = True
            
    
    pygame.display.flip()