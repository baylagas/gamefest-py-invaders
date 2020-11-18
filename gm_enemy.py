from config import HEIGHT
from gm_laser import Laser
from asset_loader import (
    RED_SPACE_SHIP,
    RED_LASER,
    GREEN_SPACE_SHIP,
    GREEN_LASER,
    BLUE_SPACE_SHIP,
    BLUE_LASER,
)
from gm_abs_ship import Ship


class Enemy(Ship):
    COLOR_MAP = {
        "red": (RED_SPACE_SHIP, RED_LASER),
        "green": (GREEN_SPACE_SHIP, GREEN_LASER),
        "blue": (BLUE_SPACE_SHIP, BLUE_LASER),
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = self.createMask()
        self.velocity = 1

    def checkBelowScreen(self):
        return self.y + self.height > HEIGHT

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(int(self.x - 20), self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
