#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Vector2i import Vector2i
from Game import *
import sys
__author__ = 'Dummyc0m'


# main method
def main():
    gameMode = input("Which gamemode? (single/double/construct): ", ["single", "double", "construct"])
    if gameMode == "single":
        sp()
    elif gameMode == "double":
        dp()
    elif gameMode == "construct":
        con()

# loop until correct input
def input(notification, selectionList):
    inputDef = raw_input(notification).lower()
    if not inputDef in selectionList:
        return input(notification, selectionList)
    return inputDef

# formats coordinates from input
def formatCoords(input, verticalIndex, horizontalIndex):
    hitX = 0
    hitY = 0
    for vi in verticalIndex:
        if vi in input.upper():
            break
        hitY += 1
    for hi in horizontalIndex:
        if hi in input.upper():
            break
        hitX += 1
    return hitX, hitY

# single player
def sp():
    mapName = raw_input("Map name: ")
    singleGame = SPGame(mapName, 30)
    displayInfo = ""
    looping = True
    verticalIndex = "ABCDEFGHIJ"
    horizontalIndex = "0123456789"
    while 1:
        print "BattleShip Single Player 1.0-SNAPSHOT\n" + displayInfo
        print singleGame.encodeBoard()
        if not looping:
            break
        input = raw_input("Coords: ")
        hitX, hitY = formatCoords(input, verticalIndex, horizontalIndex)
        if hitX < 10 and hitY < 10:
            if singleGame.hitCoords(Vector2i(hitX, hitY)):
                displayInfo = "HIT!"
            else:
                displayInfo = "MISS!"
        else:
            displayInfo = "UNABLE TO LOCATE SHIP"
            singleGame.missHit()
        updateResult = singleGame.update()
        if updateResult == SinglePlayerResult.victory:
            displayInfo = "Victory!"
            looping = False
        elif updateResult == SinglePlayerResult.defeat:
            displayInfo = "Defeat!"
            looping = False
        else:
            displayInfo = str(updateResult) + " chances left"

# double player
def dp():
    mapFirst = raw_input("Map for Player 1: ")
    mapSecond = raw_input("Map for Player 2: ")
    doubleGame = DPGame(mapFirst, mapSecond, 30)
    displayInfo = ""
    looping = True
    verticalIndex = "ABCDEFGHIJ"
    horizontalIndex = "0123456789"
    while 1:
        print "BattleShip Dual Player 1.0-SNAPSHOT\n" + displayInfo
        print doubleGame.encodeBoard()
        if not looping:
            break
        sys.stdout.write("Coords: ")
        inputFirst = sys.stdin.readline()
        sys.stdout.write("Coords: ")
        inputSecond = sys.stdin.readline()
        hitX, hitY = formatCoords(inputFirst, verticalIndex, horizontalIndex)
        if hitX < 10 and hitY < 10:
            if doubleGame.hitCoordsFirst(Vector2i(hitX, hitY)):
                displayInfo = "Player 1: HIT!\n"
            else:
                displayInfo = "Player 1: MISS!\n"
        else:
            displayInfo = "Player 1: UNABLE TO LOCATE SHIP\n"
            doubleGame.missHitFirst()

        hitX, hitY = formatCoords(inputSecond, verticalIndex, horizontalIndex)
        if hitX < 10 and hitY < 10:
            if doubleGame.hitCoordsSecond(Vector2i(hitX, hitY)):
                displayInfo += "Player 2: HIT!\n"
            else:
                displayInfo += "Player 2: MISS!\n"
        else:
            displayInfo += "Player 2: UNABLE TO LOCATE SHIP\n"
            doubleGame.missHitSecond()

        updateResult = doubleGame.update()
        if updateResult == DoublePlayerResult.keep:
            displayInfo += "Chance(s): " + str(doubleGame.getChances()[0])
        elif updateResult == DoublePlayerResult.victoryDefeat:
            displayInfo += "Player 1 won!"
            looping = False
        elif updateResult == DoublePlayerResult.defeatVictory:
            displayInfo += "Player 2 won!"
            looping = False
        else:
            displayInfo += "It's a tie"
            looping = False


# construction
def con():
    mapName = raw_input("Map name: ")
    constructGame = ConstructGame(mapName)
    while 1:
        print 1

"""
def mainBackup():
    verticalIndex = 'ABCDEFGHIJ'
    horizontalIndex = '0123456789'
    construct = False
    fileName = raw_input("Enter File Name: ")
    if fileName == "construct":
        construct = True
    else:
        file = FileUtil.openForRead(os.path.join(FileUtil.getProgramDirectory(), "maps", fileName + ".battlefield"))
        ships = Formatter.stripShips(Formatter.convertMatrix(file))
        board = Board(False)
        board.addShips(ships)
    chances = 40
    #Construction Mode
    if construct:
        print "Entering construction mode"
        chances = 0
        constructBoard = Board(True)
        constructBoard.setVerticalIndex("0123456789")
        end = False
        fileName = raw_input("Enter File Name: ")
        try:
            file = FileUtil.openForReadWrite(os.path.join(FileUtil.getProgramDirectory(), "maps", fileName + ".battlefield"))
        except IOError:
            file = FileUtil.openForFreshRW(os.path.join(FileUtil.getProgramDirectory(), "maps", fileName + ".battlefield"))
        ships = Formatter.stripShips(Formatter.convertMatrix(file))
        constructBoard.addShips(ships)
        while not end:
            print constructBoard.encodeBoard()
            input = raw_input("Enter command: ").lower()
            params = input.split()
            if(params[0] == "exit"):
                end = True
            elif(params[0] == "top"):
                if(params[3] > 5):
                    print "A ship longer than 5 is not allowed"
                ship = Ship(EndSide.top, Vector2i(int(params[1]), int(params[2])), int(params[3]))
                constructBoard.addShip(ship)
            elif(params[0] == "left"):
                if(params[3] > 5):
                    print "A ship longer than 5 is not allowed"
                ship = Ship(EndSide.left, Vector2i(int(params[1]), int(params[2])), int(params[3]))
                constructBoard.addShip(ship)
            elif(params[0] == "rm"):
                constructBoard.removeShip(constructBoard.getComponent(int(params[1]), int(params[2])).getShip())
            elif(params[0] == "export"):
                shipCount = [0, 0, 0, 0, 0]
                for ship in constructBoard.getShips():
                    shipCount[ship.getLength() - 1] += 1
                if shipCount == [0, 1, 2, 1, 1]:
                    file.seek(0)
                    file.truncate()
                    file.write(Formatter.exportMatrix(constructBoard))
                else:
                    print "You need 1 1-block-ship, 2 3-block-ship, 1 4-block-ship, 1 5-block-ship"
            elif(params[0] == "displayships"):
                for ship in constructBoard.getShips():
                    print ship.toString()
    #Start of Game
    while chances > 0:
        if(board.isAllDestroyed()):
            print "Congrats! You have destroyed all enemy ships"
            break
        print "Battle Ship 1.0-SNAPSHOT By", __author__
        print board.encodeBoard()
        print "You have", chances, "bombs left"
        input = raw_input("Coordinates: ")
        hitX = 0
        hitY = 0
        for vi in verticalIndex:
            if vi in input.upper():
                break
            hitY += 1
        for hi in horizontalIndex:
            if hi in input.upper():
                break
            hitX += 1
        if not (hitX > 9 or hitY > 9):
            board.hitComponent(hitX, hitY)
        else:
            print "Failed to locate coordinates"
        chances -= 1
        if chances < 1:
            print "You have used up all your bombs"
"""


if __name__ == '__main__':
    main()