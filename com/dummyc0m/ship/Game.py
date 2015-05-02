__author__ = 'Dummyc0m'
from Board import Board
import FileUtil
import os
import Formatter
from GameResult import *


# common code
class AbstractGame(object):
    def __init__(self, cheat, verticalIndex, horizontalIndex, mapName):
        self.cheat = cheat
        self.verticalIndex = verticalIndex
        self.horizontalIndex = horizontalIndex
        self.mapName = mapName

    def constructNewBoard(self):
        self.board = Board(self.cheat, self.verticalIndex, self.horizontalIndex)


# single player
class SPGame(AbstractGame):
    def __init__(self, mapName, chances):
        super(SPGame, self).__init__(False, 'ABCDEFGHIJ', '0123456789', mapName)
        self.chances = chances
        self.constructFromFile()

    def constructFromFile(self):
        self.constructNewBoard()
        try:
            self.file = FileUtil.openForRead(os.path.join(FileUtil.getProgramDirectory(), "maps", self.mapName + ".battlefield"))
        except IOError:
            print "Error loading map"
        ships = Formatter.stripShips(Formatter.convertMatrix(self.file))
        self.board.addShips(ships)

    def hitCoords(self, vector):
        self.chances -= 1
        return self.board.hitComponent(vector)

    def missHit(self):
        self.chances -= 1

    def update(self):
        if self.board.isAllDestroyed():
            return SinglePlayerResult.victory
        if self.chances < 1:
            return SinglePlayerResult.defeat
        return self.chances

    def encodeBoard(self):
        return self.board.encodeBoard()


# double player
class DPGame(object):
    def __init__(self, mapForFirst, mapForSecond, chances):
        self.gameFirst = SPGame(mapForFirst, chances)
        self.gameSecond = SPGame(mapForSecond, chances)
        self.chanceFirst = chances
        self.chanceSecond = chances

    def hitCoordsFirst(self, vector):
        self.chanceFirst -= 1
        return self.gameFirst.hitCoords(vector)

    def hitCoordsSecond(self, vector):
        self.chanceSecond -= 1
        return self.gameSecond.hitCoords(vector)

    def missHitFirst(self):
        self.chanceFirst -= 1

    def missHitSecond(self):
        self.chanceSecond -= 1

    def update(self):
        resultFirst = self.gameFirst.update()
        resultSecond = self.gameSecond.update()
        if resultFirst == SinglePlayerResult.victory and resultSecond == SinglePlayerResult.victory:
            return DoublePlayerResult.tie
        if resultFirst == SinglePlayerResult.victory:
            return DoublePlayerResult.victoryDefeat
        if resultSecond == SinglePlayerResult.victory:
            return DoublePlayerResult.defeatVictory
        if resultFirst < 1 and resultSecond < 1:
            return DoublePlayerResult.tie
        return DoublePlayerResult.keep

    def getChances(self):
        return self.chanceFirst, self.chanceSecond

    def encodeBoard(self):
        firstEncoded = self.gameFirst.encodeBoard().splitlines(False)
        secondEncoded = self.gameSecond.encodeBoard().splitlines(True)
        returnVal = ""
        i = 0
        for l in firstEncoded:
            returnVal += l + secondEncoded[i]
            i += 1
        return returnVal


# to-do construction mode
class ConstructGame(AbstractGame):
    def __init__(self, mapName):
        super(ConstructGame, self).__init__(True, '0123456789', '0123456789', mapName)
        self.constructFromFile()

    def constructFromFile(self):
        self.constructNewBoard()
        try:
            self.file = FileUtil.openForReadWrite(os.path.join(FileUtil.getProgramDirectory(), "maps", self.mapName + ".battlefield"))
            ships = Formatter.stripShips(Formatter.convertMatrix(self.file))
            self.board.addShips(ships)
        except IOError:
            self.file = FileUtil.openForFreshRW(os.path.join(FileUtil.getProgramDirectory(), "maps", self.mapName + ".battlefield"))

