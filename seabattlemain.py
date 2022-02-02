from enum import Enum
from config import *
import pygame


class Menu:
    def __init__(self, screen):
        self.image = pygame.image.load('sea_battle_menu.jpg')
        self.text = pygame.font.Font('C:\\Windows\\Fonts\\segoepr.ttf', SHRIFT_SIZE)
        self.buttons = ['Играть одному!', 'Играть с другом!', 'Рекорды', 'Справка']
        self.screen = screen


class Game:
    pass


class Manager:
    def __init__(self, screen):
        self.menu = Menu(screen)

    def draw(self):
        image_rect = self.menu.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.menu.screen.blit(self.menu.image, image_rect)
        text_render = self.menu.text.render('Играть одному!', True, 'black')
        text_rect = text_render.get_rect(center=(WIDTH*0.4, HEIGHT // 3))
        self.menu.screen.blit(text_render, text_rect)


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
    pygame.display.init()
    pygame.font.init()
    pygame.display.set_caption('Sea Battle')
    screen = pygame.display.set_mode(SCREEN_SIZE)
    manager = Manager(screen)
    finished = False
    clock = pygame.time.Clock()
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        manager.draw()
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
