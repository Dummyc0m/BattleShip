__author__ = 'Dummyc0m'


# vector
class Vector2i:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def toString(self):
        return "Vector2i[x:" + str(self.x) + ", y:" + str(self.y) + "]"