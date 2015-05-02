__author__ = 'Dummyc0m'
import os

def openForRead(directory):
    return open(directory, "r")

def openForWrite(directory):
    return open(directory, "w")

def openForReadWrite(directory):
    return open(directory, "r+")

def openForFreshRW(directory):
    return open(directory, "w+")

def getProgramDirectory():
    return os.path.dirname(os.path.realpath(__file__))
