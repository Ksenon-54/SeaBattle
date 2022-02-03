from enum import Enum
from config import *
import pygame


class Menu:
    """
    Содержит данные для отображения "меню"(картинку, шрифт, список названий кнопок)
    """
    buttons_names = ('Играть', 'Рекорды', 'Справка')
    image = pygame.image.load('sea_battle_menu.jpg')

    def __init__(self, name='welcome'):
        self.name = name
        if self.name == 'Рекорды':
            pass
        elif self.name == 'Справка':
            pass
        else:
            self.image_rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            self.buttons = [Button(button, i) for i, button in enumerate(self.buttons_names)]

    def check_buttons(self, mouse_pos):
        for button in self.buttons:
            if button.coliide_mouse(mouse_pos):
                if button.name == self.buttons_names[0]:
                    return Game()
                elif button.name == self.buttons_names[1]:
                    return Menu(name=button.name)


class Game:
    """
    Содержит механику игры, логику исполнения правил
    """

    background = pygame.image.load('background.jpg')

    def __init__(self):
        pass


class Button:
    def __init__(self, name: str, index: int, color='black'):
        self.name = name
        self.color = color
        self.text = pygame.font.Font(SHRIFT, SHRIFT_SIZE)
        self.index = index

    def coliide_mouse(self, mouse_pos):
        return pygame.Rect.collidepoint(self.rect_text(), *mouse_pos)

    def set_color(self, mouse_pos):
        if self.coliide_mouse(mouse_pos):
            self.color = 'red'
        else:
            self.color = 'black'

    def render_text(self):
        return self.text.render(self.name, True, self.color)

    def rect_text(self):
        return self.render_text().get_rect(center=(WIDTH * 0.4, HEIGHT // 3 + 40 * self.index))


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
        return done

    def handle_events(self, events):
        """
        Обрабатывает события мыши, клавиатуры
        """
        done = False
        for event in events:
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    game = self.menu.check_buttons(pygame.mouse.get_pos())
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
                self.screen.blit(button.render_text(), button.rect_text())


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
