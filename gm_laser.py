import pygame
from config import HEIGHT
from gm_utils import collide


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.velocity = 5
        self.mask = self.createMask()

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def createMask(self):
        return pygame.mask.from_surface(self.img)

    def moveDown(self, goingDown=True):
        if goingDown:
            self.y += self.velocity
        else:
            self.y -= self.velocity

    def off_screen(self):
        return not (self.y <= HEIGHT and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)
