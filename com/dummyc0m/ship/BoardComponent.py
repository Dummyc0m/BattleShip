__author__ = 'Dummyc0m'
class BoardComponent(object):
    def __init__(self):
        self.occupied = False
        self.hit = False
        self.hasHit = False

    def isOccupied(self):
        return self.occupied

    def hitComponent(self):
        if self.occupied:
            self.hit = True
            return True
        self.hasHit = True
        return False

    def hasBeenHit(self):
        return self.hasHit

    def isHit(self):
        return self.hit

    def toString(self):
        return "-"