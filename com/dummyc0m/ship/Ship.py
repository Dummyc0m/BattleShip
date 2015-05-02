__author__ = 'Dummyc0m'
from Direction import *
from ShipComponent import ShipComponent


class Ship(object):
    def __init__(self, endSide, startVec, length):
        self.length = length
        self.startVec = startVec
        if endSide == EndSide.top:
            self.direction = Direction.vertical
            self.components = []
            for i in range(length):
                self.components.append(ShipComponent(self, Direction.vertical, startVec.getX(), startVec.getY() + i))
        elif endSide == EndSide.left:
            self.direction = Direction.horizontal
            self.components = []
            for i in range(length):
                self.components.append(ShipComponent(self, Direction.horizontal, startVec.getX() + i, startVec.getY()))

    def isAllDown(self):
        for c in self.components:
            if not c.isHit() :
                return False
        return True

    def getComponents(self):
        return self.components

    def getLength(self):
        return self.length

    def contains(self, x, y):
        for component in self.components:
            if component.getX() == x and component.getY() == y:
                return True
        return False

    def toString(self):
        return "Ship[direction: " + str(self.direction) + ", length: " + str(self.length) + ", startVec: " + self.startVec.toString() + "]"