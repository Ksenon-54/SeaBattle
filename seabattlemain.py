from enum import Enum
from config import *
import pygame


class Menu:
    """
    Содержит данные для отображения "меню"(картинку, шрифт, список названий кнопок)
    """
    buttons_names = ['Играть']  # ('Играть', 'Рекорды', 'Справка')
    image = pygame.image.load('sea_battle_menu.jpg')

    def __init__(self):
        self.image_rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.buttons = [Button(button) for button in self.buttons_names]


class Game:
    """
    Содержит механику игры, логику исполнения правил
    """
    pass


class Button:
    def __init__(self, name, color='black'):
        self.name = name
        self.color = color
        self.text = pygame.font.Font(SHRIFT, SHRIFT_SIZE)
        self.button_text = self.text.render(self.name, True, self.color)
        self.button_rect = self.button_text.get_rect(center=(WIDTH * 0.4, HEIGHT // 3))

    def set_color(self, mouse_pos):
        if pygame.Rect.collidepoint(self.button_rect, *mouse_pos):
            self.color = 'red'
            print('set color: ', self.color)
        else:
            self.color = 'black'


class Manager:
    """
    Управляет состоянием игры, осушествляет переключение между "меню" и "игровым сеансом"
    """
    def __init__(self):
        self.artist = Draw()
        self.menu = Menu()

    def draw(self, other):
        self.artist.draw(other)

    def process(self, py_events):
        """
        Запускает методы и обработчик событий
        :param py_events: очередь событий pygame
        :return: True если выход
        """
        done = self.handle_events(py_events)
        self.draw(self.menu)
        if pygame.mouse.get_focused():
            mouse_pos = pygame.mouse.get_pos()
            for button in self.menu.buttons:
                button.set_color(mouse_pos)
                # print('manager: ', button.color)
        return done

    def handle_events(self, events):
        """
        Обрабатывает события мыши, клавиатуры
        """
        done = False
        for event in events:
            if event.type == pygame.QUIT:
                done = True
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         self.gun.activate()
            # elif event.type == pygame.MOUSEBUTTONUP:
            #     if event.button == 1:
            #         self.balls.append(self.gun.strike())
            #         self.score_t.b_used += 1
        return done


class Draw:
    """
    Занимается отрисовкой игры
    """
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

    def draw(self, other):
        if isinstance(other, Menu):
            self.screen.blit(other.image, other.image_rect)
            for button in other.buttons:
                print('draw')
                self.screen.blit(button.button_text, button.button_rect)


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
    clock = pygame.time.Clock()
    finished = False
    while not finished:
        clock.tick(FPS)
        finished = manager.process(pygame.event.get())
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
