import pygame
import os
from config import soundFolder
from asset_loader import YELLOW_SPACE_SHIP, YELLOW_LASER
from gm_abs_ship import Ship


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = self.createMask()
        self.max_health = health
        self.width = self.ship_img.get_width()
        self.height = self.ship_img.get_height()

    def move_lasers(self, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.moveDown(False)
            if laser.off_screen():
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        if obj.y > 0:
                            laserEffect = pygame.mixer.Sound(os.path.join(soundFolder,"__retro-bomb-explosion_modif.wav"))
                            laserEffect.play()
                        objs.remove(obj)
                        self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthBar(window)

    def healthBar(self, window):
        pygame.draw.rect(
            window,
            (255, 0, 0),
            (self.x, self.y + self.ship_img.get_height() + 10, self.width, 10),
        )
        pygame.draw.rect(
            window,
            (0, 255, 0),
            (
                self.x,
                self.y + self.ship_img.get_height() + 10,
                (self.width * (self.health / self.max_health)),
                10,
            ),
        )

    def moveLeft(self):
        self.x -= self.velocity

    def moveRight(self):
        self.x += self.velocity

    def moveUp(self):
        self.y -= self.velocity

    def moveDown(self):
        self.y += self.velocity

    def checkDownLimit(self, height, fromBottom):
        return self.y + self.velocity + self.height + fromBottom < height

    def checkUpLimit(self, height, fromTop):
        return self.y - self.velocity - fromTop > height

    def checkRightLimit(self, width):
        return self.x + self.velocity + self.width < width

    def checkLeftLimit(self, width):
        return self.x - self.velocity > width
