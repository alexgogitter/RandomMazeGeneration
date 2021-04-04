import sys

import pygame

import MazeGenAlgorithm

import random

import secrets

pygame.init()

windowDimensions = (1000, 900)

bgColour = (8, 8, 8)

edges = []

mazeList = []

possibleRoute = []

displayName = ("Random Maze Generation Version 0")

displaySurface = pygame.display.set_mode(windowDimensions)

pygame.display.set_caption(displayName)

running = True

mazeComplete = False

nodeMatrix = MazeGenAlgorithm.generateMazeBase(windowDimensions, 10, edges,)




def checkPos(mousePosition):
    
    normalisedMousePosition = mousePosition[0]//10, mousePosition[1]//10

    if not nodeMatrix[normalisedMousePosition[0]][normalisedMousePosition[1]].getEState():

        pygame.draw.rect(displaySurface, (255, 91, 69), (normalisedMousePosition[0] * 10, normalisedMousePosition[1] * 10, 10, 10), 0,)




def selectEndNode(mousePosition):

    normalisedMousePosition = mousePosition[0]//10, mousePosition[1]//10




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




mazeStart = randEdge()

possibleRoute.append(mazeStart)



def randomPrimAlgo(possibleRoute, mazeState):


    if len(possibleRoute) != 0:

        current = secrets.choice(possibleRoute)

        current.setTraversable(True)

        possibleRoute.remove(current)

        current.joinToParent()

        for neighbour in current.getNeighbours():
                
            if not neighbour.getVisited() and not neighbour.getEState():

                neighbour.setVisited(True)

                neighbour.setParent(current)

                possibleRoute.append(neighbour)

    else:
        mazeState = not mazeState

        return mazeState




while running:


    print(len(possibleRoute))


    displaySurface.fill(bgColour)

    drawNodes(nodeMatrix)

    if not mazeComplete:

        mazeComplete = randomPrimAlgo(possibleRoute, mazeComplete,)

    else:

        checkPos(pygame.mouse.get_pos())

    mazeStart.drawNode(displaySurface)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
            
    
    pygame.display.flip()