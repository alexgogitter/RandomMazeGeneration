## Vector2 operators that will/may be required to calculate and handle 3-dimensional images
import math

def add(Vector2D: tuple, scalar: int):

    return((float(Vector2D[0] + scalar)), (float(Vector2D[1] + scalar)))

###Adds a vector to a Vector


def addVec(Vector2D1: tuple, Vector2D2: tuple):

    return (((float(Vector2D1[0])) + (float(Vector2D2[0]))), ((float(Vector2D1[1])) + (float(Vector2D2[1]))))

###Subtracts a vector from a vector


def sub(Vector2D1: tuple, Vector2D2: tuple):

    return (((float(Vector2D1[0])) - (float(Vector2D2[0]))), ((float(Vector2D1[1])) - (float(Vector2D2[1]))))

###Multiplies a vector by a scalar


def scale(Vector2D: tuple, ScaleFactor: tuple):

    return (Vector2D[0]*ScaleFactor, Vector2D[1]*ScaleFactor)

###Calculates Euclidean distance between two Vectors


def length(Vector2D: tuple):

    return(math.sqrt((Vector2D[0] * Vector2D[0]) + (Vector2D[1] * Vector2D[1])))

###Converts a vector into a Unit Vector


def normalize(Vector2D: tuple):

    VectNorm1 = Vector2D[0] / length(Vector2D)

    VectNorm2 = Vector2D[1] / length(Vector2D)

    return(float (VectNorm1), float(VectNorm2))

###Calculaates dot product of two 2D column vectors


def dotprod(Vector2D1: tuple, Vector2D2: tuple):## Works on only normalized vectors
    
    return((Vector2D1[0] * Vector2D2[0]) + (Vector2D1[1] * Vector2D2[1]))
