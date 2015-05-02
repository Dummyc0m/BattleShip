__author__ = 'Dummyc0m'
from Ship import Ship
from Vector2i import Vector2i
from Direction import *


# returns string from matrix
def formatMatrix(matrix):
    returnVal = ""
    for a in matrix:
        for e in a:
            returnVal += str(e) + " "
        returnVal += "\n"
    return returnVal


# returns matrix from file/string
def convertMatrix(file):
    returnVal = []
    for line in file:
        tempList = []
        for element in line.split():
            tempList.append(element)
        returnVal.append(tempList)
    return returnVal


# returns matrix from board matrix
def exportMatrix(board):
    returnVal = ""
    for line in board.getComponents():
        for element in line:
            returnVal += element.toString() + " "
        returnVal += "\n"
    return returnVal


# returns a list of ships from matrix
def stripShips(matrix):
    returnVal = []
    y = 0
    for line in matrix:
        x = 0
        for element in line:
            if element == "X":
                escape = False
                for ship in returnVal:
                    if ship.contains(x, y):
                        escape = True
                        break
                if(escape):
                    x += 1
                    continue
                try:
                    if x < 9 and matrix[y][x + 1] == "X":
                        length = 0
                        for i in range(10 - x):
                            try:
                                if matrix[y][x + i] == "X":
                                    length += 1
                                else:
                                    break
                            except IndexError:
                                print "IndexError"
                                break
                        print x, y, "left", length
                        returnVal.append(Ship(EndSide.left, Vector2i(x, y), length))
                except IndexError:
                    print "IndexError"

                try:
                    if y < 9 and matrix[y + 1][x] == "X":
                        length = 0
                        for i in range(10 - y):
                            try:
                                if matrix[y + i][x] == "X":
                                    length += 1
                                else:
                                    break
                            except IndexError:
                                print "IndexError"
                                break
                        print x, y, "top", length
                        returnVal.append(Ship(EndSide.top, Vector2i(x, y), length))
                except IndexError:
                    print "IndexError"
            x += 1
        y += 1
    return returnVal

