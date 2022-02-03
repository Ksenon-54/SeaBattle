from enum import Enum
from config import *
import pygame


class Menu:
    """
    Содержит данные для отображения "меню"(картинку, шрифт, список названий кнопок)
    """
    def __init__(self, screen):
        self.image = pygame.image.load('sea_battle_menu.jpg')
        self.text = pygame.font.Font(SHRIFT, SHRIFT_SIZE)
        self.buttons = ('Играть', 'Рекорды', 'Справка',)
        self.screen = screen
        self.image_rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))


class Game:
    """
    Содержит механику игры, логику исполнения правил
    """
    pass


class Manager:
    """
    Управляет состоянием игры, осушествляет переключение между "меню" и "игровым сеансом"
    """
    def __init__(self, screen):
        self.menu = Menu(screen)

    def draw(self):
        self.menu.screen.blit(self.menu.image, self.menu.image_rect)
        text_render = self.menu.text.render(self.menu.buttons[0], True, 'black')
        text_rect = text_render.get_rect(center=(WIDTH*0.4, HEIGHT // 3))
        self.menu.screen.blit(text_render, text_rect)


class Round:
    """
    Обрабатывает события данного "игрового сеанса"
    """
    pass


class PlayingField:
    """
    Содержит данные игровых полей
    """
    pass


class Cell(Enum):
    """
    Содержит данные состояний клетки, наличие или отсутствие коробля
    """
    pass


class Ship:
    """
    Содержит данные о типах кораблей, определяет количество сегментов у коробля
    """
    pass


class Player:
    """
    Содержит общие методы взаимодействия игроков
    """
    pass


class PlayerHuman(Player):
    """
    Описывает атрибуты и методы игрока человек
    """
    pass


class PlayerAI(Player):
    """
    Эмулирует поведение игрока
    """
    pass


class Draw:
    """
    Занимается отрисовкой игры
    """
    pass


def main():
    """
    Содержит главный цикл игры, инициализирует дисплей pygame
    :return: None
    """
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
