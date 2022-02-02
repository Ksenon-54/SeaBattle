from enum import Enum
from config import *
import pygame


class Menu:
    def __init__(self):
        image = pygame.image.load('seabattlemenu.jpg')
        image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(image, image_rect)


class Game:
    pass


class Manager:
    pass


class Round:
    pass


class PlayingField:
    pass


class Cell(Enum):
    pass


class Ship:
    pass


class Player:
    pass


class PlayerHuman(Player):
    pass


class PlayerAI(Player):
    pass


class Draw:
    pass


def main():
    pass


if __name__ == '__main__':
    pygame.display.init()
    pygame.display.set_caption('Sea Battle')
    screen = pygame.display.set_mode(SCREEN_SIZE)
    finished = False
    clock = pygame.time.Clock()
    menu = Menu()
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        pygame.display.update()

    pygame.quit()
