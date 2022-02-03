from enum import Enum
from config import *
import pygame


class Menu:
    """
    Содержит данные для отображения "меню"(картинку, шрифт, список названий кнопок)
    """

    image = pygame.image.load('sea_battle_menu.jpg')

    def __init__(self, screen):
        self.text = pygame.font.Font(SHRIFT, SHRIFT_SIZE)
        self.button_game = self.text.render('Играть', True, 'black')
        self.button_records = self.text.render('Рекорды', True, 'black')
        self.button_help = self.text.render('Справка', True, 'black')
        self.screen = screen

    def draw(self):
        image_rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        game_rect = self.button_game.get_rect(center=(WIDTH * 0.4, HEIGHT // 3))
        records_rect = self.button_game.get_rect(center=(WIDTH * 0.4, HEIGHT * 0.5))
        help_rect = self.button_game.get_rect(center=(WIDTH * 0.4, HEIGHT * 0.7))
        return image_rect, game_rect, records_rect, help_rect


class Game:
    """
    Содержит механику игры, логику исполнения правил
    """
    pass


class Manager:
    """
    Управляет состоянием игры, осушествляет переключение между "меню" и "игровым сеансом"
    """
    def __init__(self):
        self.artist = Draw()
        self.menu = Menu(self.artist.screen)

    def draw(self):
        self.artist.draw(self.menu)


class Draw:
    """
    Занимается отрисовкой игры
    """
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

    def draw(self, other):
        rect_list = other.draw()
        self.screen.blit(other.image, rect_list[0])
        self.screen.blit(other.button_game, rect_list[1])
        self.screen.blit(other.button_records, rect_list[2])
        self.screen.blit(other.button_help, rect_list[3])


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


def main():
    """
    Содержит главный цикл игры, инициализирует дисплей pygame
    :return: None
    """
    pygame.display.init()
    pygame.font.init()
    pygame.display.set_caption('Sea Battle')
    manager = Manager()
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
