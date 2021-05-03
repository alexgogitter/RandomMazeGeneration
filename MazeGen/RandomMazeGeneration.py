import sys
import pygame
import MazeGenAlgorithm
import random
import secrets
from operator import attrgetter, pos

pygame.init()

windowDimensions = (200, 200)
bgColour = (8, 8, 8)

edges = []
mazeList = []
openList = []
closedList = []
possibleRoute = []
path = []
mazeEnd = []

displayName = ("Random Maze Generation Version 0")

displaySurface = pygame.display.set_mode(windowDimensions)

pygame.display.set_caption(displayName)

running = True
mazeComplete = False
mazeStart = None
mazeEndSel = False
pathFound = False

maxWilsonPathLength = 10



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


def aStarSearch(openList, closedList):

    pathState = False

    if len(openList) is not 0:

        currentNode = min(openList, key=attrgetter('totalDist'))

        posTemp = currentNode.getPosition()

        pygame.draw.rect(displaySurface, (255, 0, 0), (posTemp[0]*10, posTemp[1]*10, 10, 10,), 0,)
        
        currentNode.setVisitedByPath(True)

        closedList.append(currentNode)

        openList.remove(currentNode)

        if currentNode == mazeEnd[0]:


            
            pathState = True

            while currentNode is not mazeStart:

                path.append(currentNode)

                currentNode.setPath(True)

                currentNode = currentNode.getParent()

            return pathState
        else:

            for node in currentNode.getJoinedTo():

                if not node.getEState():

                    if not node.getVisitedByPath():

                        node.setVisitedByPath(True)

                    if node in closedList:

                        continue

                    openList.append(node)
    else:

        pathState = True

        openList.clear()

        closedList.clear()

        print("No Path Found")

        return pathState


mazeStart = randEdge()


possibleRoute.append(mazeStart)


def selectEndNode(mousePosition):

    openList.clear()

    closedList.clear()

    
    openList.append(mazeStart)

    if mazeComplete == True:

        if len(mazeEnd) > 0:

            for i in mazeEnd:

                i.setEnd(False)

        mazeEnd.clear()

        normalisedMousePosition = mousePosition[0]//10, mousePosition[1]//10

        node = nodeMatrix[normalisedMousePosition[0]][normalisedMousePosition[1]]

        if mazeComplete:
            
            node.setEnd(True)

            mazeEnd.append(node)

        else:
            pass

        
pathStack = []

spanningTree = []

nodeBuffer = []

spanningTree.append(mazeStart)

walking = False

unvisitedNodes = []

for i in nodeMatrix:

    for node in i:

        if not node.getEState():

            unvisitedNodes.append(node)

pathLen = 0

pathStack.append(mazeStart)

def walk(fromNode, through, maxLen):

    walking = True

    current = fromNode

    iteration = 0

    while walking:

        iteration += 1

        if iteration == maxLen:

            return False

        else:

            currentNeigh = secrets.choice(current.getNeighbours())

            if currentNeigh.getInSpanningTree():
                pass

            else:

                continue               
 

def randomBactraceAlgo(mazeState, pathStack):

    if len(pathStack) is not 0:

        currentCell = pathStack[len(pathStack) - 1]

        neighboursUnvisited = []

        pathStack.pop()

        MazeGenAlgorithm.getNeighbour(nodeMatrix, currentCell)

        for neighbour in currentCell.getNeighbours():
            
            if not neighbour.getVisited() and not neighbour.getEState() and not neighbour.getTraversable():

                neighboursUnvisited.append(neighbour)

        if len(neighboursUnvisited) is not 0:
            
            pathStack.append(currentCell)

            randomCellChoice = secrets.choice(neighboursUnvisited)
            
            randomCellChoice.setParent(currentCell)

            randomCellChoice.setVisited(True)

            randomCellChoice.setTraversable(True)

            randomCellChoice.joinToParent()

            pathStack.append(randomCellChoice)

    else:
        
        mazeState = not mazeState
        
        return True


def randomPrimAlgo(possibleRoute, mazeState):


    if len(possibleRoute) != 0:

        current = secrets.choice(possibleRoute)

        current.setTraversable(True)

        possibleRoute.remove(current)

        current.joinToParent()

        MazeGenAlgorithm.getNeighbour(nodeMatrix, current)

        for neighbour in current.getNeighbours():
                
            if not neighbour.getVisited() and not neighbour.getEState():

                neighbour.setVisited(True)

                neighbour.setParent(current)

                possibleRoute.append(neighbour)

    else:

        mazeState = not mazeState

        return mazeState


def wilsonsAlgo(mazeState, spanningTree, verts, isWalking, buffer):

    if len(verts) is not 0:

        if not isWalking:

            buffer.clear()

            point = secrets.choice(unvisitedNodes)

            buffer.append(point)

            isWalking = True

        else:

            point = buffer[0]
    else:

        return not mazeState





while running:

    displaySurface.fill(bgColour)

    drawNodes(nodeMatrix)

    if not mazeComplete:

        ##mazeComplete = randomBactraceAlgo(mazeComplete, pathStack)

        mazeComplete = randomPrimAlgo(possibleRoute, mazeComplete)

    else:

        checkPos(pygame.mouse.get_pos())

    if mazeEndSel and mazeComplete and not pathFound:

        pathFound = aStarSearch(openList, closedList)

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
                selectEndNode(pygame.mouse.get_pos())

                pathFound = False

                for i in path:
                    i.setPath(False)

                path.clear()

                for x in range(len(nodeMatrix)):
                    for y in range(len(nodeMatrix[x])):
                        if mazeComplete:
                            nodeMatrix[x][y].findDistances(mazeStart, mazeEnd[0])

                mazeEndSel = True
            
    
    pygame.display.flip()