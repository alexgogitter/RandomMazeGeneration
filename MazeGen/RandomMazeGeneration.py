import sys

import pygame

import MazeGenAlgorithm

import random

import secrets

pygame.init()

windowDimensions = (500, 400)

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

def randomPrimAlgo(possibleRoute,):
    
    if len(possibleRoute) > 0:

        current = random.choice(possibleRoute)

        current.setTraversable(True)

        possibleRoute.remove(current)

        current.joinToParent()

        for neighbour in current.getNeighbours():
                
            if not neighbour.getVisited() and not neighbour.getEState():

                neighbour.setVisited(True)

                neighbour.setParent(current)

                possibleRoute.append(neighbour)

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            sys.exit()

    displaySurface.fill(bgColour)

    drawNodes(nodeMatrix)

    randomPrimAlgo(possibleRoute)

    mazeStart.drawNode(displaySurface)
    
    pygame.display.flip()