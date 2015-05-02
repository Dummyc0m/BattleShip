#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Dummyc0m'
from BoardComponent import BoardComponent


class Board(object):
    def __init__(self, displayComponents, verticalIndex, horizontalIndex):
        self.displayComponents = displayComponents
        self.verticalIndex = verticalIndex
        self.horizontalIndex = horizontalIndex
        self.height = 10
        self.width = 10
        self.initializeBoard()
        self.tableTop = '    '
        for i in horizontalIndex:
            self.tableTop += str(i) + '   '
        self.tableTop += '\n  ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐ \n'
        self.tableSeparator = '\n  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ \n'
        self.tableBottom = '\n  └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘ '
        self.columnSeparator = ' │ '
        self.emptyComponent = ' '
        self.hitEmptyComponent = '~'
        self.destroyedShipComponent = '◘'
        self.damagedShipComponent = '○'
        self.ships = []

    def initializeBoard(self):
        self.boardMatrix = []
        for i in range(self.width):
            temp = []
            for o in range(self.height):
                temp.append(BoardComponent())
            self.boardMatrix.append(temp)

    def hitComponent(self, vector):
        return self.boardMatrix[vector.getY()][vector.getX()].hitComponent()

    def isAllDestroyed(self):
        for ship in self.ships:
            if(not ship.isAllDown()):
                return False
        return True

    def addShip(self, ship):
        self.ships.append(ship)
        for c in ship.getComponents():
            self.boardMatrix[c.getY()][c.getX()] = c

    def addShips(self, ships):
        for ship in ships:
            self.addShip(ship)

    def setVerticalIndex(self, index):
        self.verticalIndex = index

    def getShips(self):
        return self.ships

    def removeShip(self, ship):
        self.ships.remove(ship)
        for component in ship.getComponents():
            self.boardMatrix[component.getY()][component.getX()] = BoardComponent()

    def getComponents(self):
        return self.boardMatrix

    def getComponent(self, vector):
        return self.boardMatrix[vector.getY()][vector.getX()]

    def encodeBoard(self):
        returnVal = self.tableTop
        i = 0
        for list in self.boardMatrix:
            returnVal += self.verticalIndex[i]
            returnVal += self.columnSeparator
            for element in list:
                if element.isHit() or (self.displayComponents and element.isOccupied()):
                    if element.getShip().isAllDown():
                        returnVal += self.destroyedShipComponent
                    else:
                        returnVal += self.damagedShipComponent
                else:
                    if element.hasBeenHit():
                        returnVal += self.hitEmptyComponent
                    else:
                        returnVal += self.emptyComponent
                returnVal += self.columnSeparator
            if(i < 9):
               returnVal += self.tableSeparator
            i += 1
        returnVal += self.tableBottom
        return returnVal