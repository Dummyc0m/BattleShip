__author__ = 'Dummyc0m'
from enum import Enum


# results of sp game
class SinglePlayerResult(Enum):
    defeat = "defeat"
    victory = "victory"


# results of dp game
class DoublePlayerResult(Enum):
    defeatVictory = "defeatVictory"
    victoryDefeat = "victoryDefeat"
    tie = "tie"
    keep = "keep"