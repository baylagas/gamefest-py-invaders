import pygame
import os
import time
import random
from asset_loader import BG
from config import WIDTH, HEIGHT, GAME_CAPTION, FPS, MAIN_FONT, LOST_FONT, soundFolder
from gm_player import Player
from gm_enemy import Enemy
from gm_utils import collide

RUN = True
PLAYER = Player(300, 530)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_CAPTION)
pygame.mixer.init()


def checkEvents():
    global RUN
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False


def checkKeyPress():
    global PLAYER
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and PLAYER.checkLeftLimit(0):  # left
        PLAYER.moveLeft()
    if keys[pygame.K_d] and PLAYER.checkRightLimit(WIDTH):  # right
        PLAYER.moveRight()
    if keys[pygame.K_w] and PLAYER.checkUpLimit(0, 40):  # up
        PLAYER.moveUp()
    if keys[pygame.K_s] and PLAYER.checkDownLimit(HEIGHT, 20):  # down
        PLAYER.moveDown()
    if keys[pygame.K_SPACE]:  # shoot
        PLAYER.shoot()


def drawUIBar():
    pygame.draw.rect(WIN, (0, 0, 0), (0, 0, WIDTH, 50))


def createEnemies(enemies, wave_length):
    for i in range(wave_length):
        enemy = Enemy(
            random.randrange(50, WIDTH - 100),
            random.randrange(-1500, -100),
            random.choice(["red", "blue", "green"]),
        )
        enemies.append(enemy)


def centerLabel(label, height):
    newWidth = WIDTH / 2 - label.get_width() / 2
    return (newWidth, height)


def playGameMusic():
    pygame.mixer.music.load(os.path.join(soundFolder,"night-soft-techno_modif.mp3"))
    pygame.mixer.music.play(-1)

def stopGameMusic():
    pygame.mixer.music.stop()

def main():
    global RUN
    level = 0
    lives = 5
    enemies = []
    wave_length = 5
    lost = False
    lost_count = 0
    clock = pygame.time.Clock()
    playGameMusic()

    def redraw_window():
        WIN.blit(BG, (0, 0))

        for enemy in enemies:
            enemy.draw(WIN)

        drawUIBar()
        level_label = MAIN_FONT.render(f"level: {level}", 1, (255, 255, 255))
        lives_label = MAIN_FONT.render(f"lives: {lives}", 1, (255, 255, 255))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        WIN.blit(lives_label, (10, 10))

        PLAYER.draw(WIN)
        if lost:
            lost_label = LOST_FONT.render("You Lost", 1, (255, 255, 255))
            WIN.blit(lost_label, centerLabel(lost_label, 350))
        pygame.display.update()

    while RUN:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or PLAYER.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                stopGameMusic()
                RUN = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 2
            createEnemies(enemies, wave_length)

        checkEvents()
        checkKeyPress()

        for enemy in enemies[:]:
            enemy.moveDown()
            enemy.move_lasers(PLAYER)

            if random.randrange(0, 4 * FPS) == 1:
                enemy.shoot()

            if collide(enemy, PLAYER):
                PLAYER.health -= 10
                laserEffect = pygame.mixer.Sound(os.path.join(soundFolder,"__retro-bomb-explosion_modif.wav"))
                laserEffect.play()
                enemies.remove(enemy)
            elif enemy.checkBelowScreen():
                lives -= 1
                enemies.remove(enemy)

        PLAYER.move_lasers(enemies)


main()
