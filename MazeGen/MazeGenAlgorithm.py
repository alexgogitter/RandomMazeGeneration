##Maze Generation
import pygame

print("importing Maze Generation Version 0")


class node:
    def __init__(self, position, width,):

        self.parent = None

        self.width = width

        self.neighbours = []

        self.parent = None

        self.position = position

        self.traversable = False

        self.visited = False

        self.edge = False

        self.start = False

        self.end = False

        self.rectang = [(self.position[0]*10) + 1, (self.position[1]*10) + 1, (self.width - 2), (self.width - 2)]

        self.traversableCol = (255, 255, 255)

        self.nonTraversableCol = (64, 64, 64)

    def joinToParent(self,):

        if self.parent != None:

            parentPosition = self.parent.getPosition()

            currentPosition = self.position

            deltaPosition = (currentPosition[0] - parentPosition[0]), (currentPosition[1] - parentPosition[1])
            
            if deltaPosition[0] < 0:

                self.rectang[2] += 2

            if deltaPosition[0] > 0:

                self.rectang[0] -= 2

                self.rectang[2] += 2

            if deltaPosition[1] > 0:

                self.rectang[1] -= 2

                self.rectang[3] += 2

            if deltaPosition[1] < 0:

                self.rectang[3] += 3

        
    def drawNode(self, screen):

        if self.start:
    
            pygame.draw.rect(screen, (32, 255, 32), self.rectang, 0,)

        elif self.traversable:
            
            pygame.draw.rect(screen, self.traversableCol, self.rectang, 0,)

        elif not self.traversable:

            pygame.draw.rect(screen, self.nonTraversableCol, self.rectang, 0,)

        if self.edge:
            pygame.draw.rect(screen, (0, 0, 0), self.rectang, 0,)
    
    def getPosition(self,):
        return(self.position)

    def setEState(self, state,):
        self.edge = state


    def setEnd(self, state,):
        self.end = state


    def getEState(self,):
        
        return self.edge

    def getVisited(self,):

        return self.visited

    def setVisited(self, data,):

        self.visited = data

    def setNeighbours(self, listData,):
        self.neighbours = list(listData)


    def addNeighbours(self, data,):

        self.neighbours.append(data)

    def setTraversable(self, data,):
        self.traversable = data

    def getNeighbours(self,):
        
        return self.neighbours


    def setStart(self, state,):

        self.start = state

    def getStart(self,):

        return self.start

    def getStartorFinish(self):

        return self.start

    def setParent(self, data):
        self.parent = (data)

    def getParent(self, ):
        
        return self.parent


def removeRepeats(data):
    if len(data) >= 1:
        
        return data

    else:

        for i in data:

            for j in data:

                if data[j] == data[i]:

                    data.remove(data[j])

    return data 


def getNeighbour(nodeMatrix):
    for x in range(len(nodeMatrix)):
        
        for y in range(len(nodeMatrix[x])):

            xIncr = 1

            yIncr = 1

            if x == (0 or (len(nodeMatrix))):

                xIncr = 0

            elif y == (0 or (len(nodeMatrix[x]))):

                yIncr = 0

            possibleNeighbours = [

                ((x - xIncr), y),

                ((x + xIncr), y),

                (x, (y - yIncr)),

                (x, (y + yIncr))

            ]
            
            possibleNeighbours = removeRepeats(possibleNeighbours)

            for position in possibleNeighbours:

                try:
                
                    nodeMatrix[x][y].addNeighbours(nodeMatrix[abs(position[0])][abs(position[1])])

                    neighboursUnsorted = nodeMatrix[x][y].getNeighbours()

                    neighboursUnsorted = removeRepeats(neighboursUnsorted)
                
                except IndexError:

                    continue

def generateMazeBase(windowDimensions, nodeWidth, edges,):

    navWidth = windowDimensions[0]//nodeWidth

    navHeight = windowDimensions[1]//nodeWidth

    xList = []
    yList = []

    for xNode in range(0, (navWidth + 1), 1):

        for yNode in range(0, (navHeight + 1), 1):

            position = [xNode, yNode]

            print((position, (xNode, yNode), (navWidth, navHeight),(xNode == navWidth),(yNode == navHeight)))

            Node = node(position, nodeWidth)

            if position[0] == 0 or position[1] == 0: 

                Node.setEState(True)

                edges.append(Node)

            if xNode+1 == navWidth or yNode+1 == navHeight:

                Node.setEState(True)

                edges.append(Node)

            yList.append(Node)

        xList.append(list(yList))

        yList.clear()

    nodeMatrix = xList

    getNeighbour(nodeMatrix)

    return nodeMatrix
    

