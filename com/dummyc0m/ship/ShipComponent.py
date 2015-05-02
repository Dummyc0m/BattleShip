__author__ = 'Dummyc0m'
from BoardComponent import BoardComponent


class ShipComponent(BoardComponent):
    def __init__(self, ship, direction, x, y):
        super(ShipComponent, self).__init__()
        self.occupied = True
        self.ship = ship
        self.direction = direction
        self.x = x
        self.y = y

    def getShip(self):
        return self.ship

    def getDirection(self):
        return self.direction

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setHit(self):
        self.hit = True

    def toString(self):
        return "X"