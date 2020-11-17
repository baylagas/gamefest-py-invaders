import pygame
import os
from config import assetFolder, WIDTH, HEIGHT


def pyLoad(assetName):
    return pygame.image.load(os.path.join(assetFolder, assetName))


def pyTScale(assetName):
    return pygame.transform.scale(pyLoad(assetName), (WIDTH, HEIGHT))


RED_SPACE_SHIP = pyLoad("pixel_ship_red_small.png")
GREEN_SPACE_SHIP = pyLoad("pixel_ship_green_small.png")
BLUE_SPACE_SHIP = pyLoad("pixel_ship_blue_small.png")
YELLOW_SPACE_SHIP = pyLoad("pixel_ship_yellow.png")  # player
RED_LASER = pyLoad("pixel_laser_red.png")
GREEN_LASER = pyLoad("pixel_laser_green.png")
BLUE_LASER = pyLoad("pixel_laser_blue.png")
YELLOW_LASER = pyLoad("pixel_laser_yellow.png")
BG = pyTScale("background-black.png")
