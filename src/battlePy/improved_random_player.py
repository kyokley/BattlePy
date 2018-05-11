from battlePy.player import Player
from battlePy.default_config import (BOARD_WIDTH,
                                     BOARD_HEIGHT)
from battlePy.ship import UP, RIGHT
import random

class ImprovedRandomPlayer(Player):
    def initPlayer(self):
        self.name = 'ImprovedRandomPlayer'

    def newGame(self):
        self.shots = set()

    def placeShips(self):
        for ship in self.ships:
            isValid = False
            while not isValid:
                orientation = random.choice([UP, RIGHT])
                if orientation == UP:
                    location = (random.randint(0, BOARD_WIDTH - 1),
                                random.randint(0, BOARD_HEIGHT - 1 - ship.size))
                else:
                    location = (random.randint(0, BOARD_WIDTH - 1 - ship.size),
                                random.randint(0, BOARD_HEIGHT - 1))
                ship.placeShip(location, orientation)

                if self.isShipPlacedLegally(ship):
                    isValid = True

    def fireShot(self):
        shot = (random.randint(0, BOARD_WIDTH - 1),
                random.randint(0, BOARD_HEIGHT - 1))

        while shot in self.shots:
            shot = (random.randint(0, BOARD_WIDTH - 1),
                    random.randint(0, BOARD_HEIGHT - 1))
        self.shots.add(shot)
        return shot
