import pygame

pygame.font.init()


def createFont(fontName, fontSize):
    return pygame.font.SysFont(fontName, fontSize)


assetFolder = "assets"

WIDTH, HEIGHT = 750, 650
GAME_CAPTION = "PYTHON INVADERS"
FPS = 60
MAIN_FONT = createFont("comicsans", 50)
LOST_FONT = createFont("comicsans", 60)
