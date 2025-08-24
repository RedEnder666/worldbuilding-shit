import pygame
import sys
from pygame.locals import *


class MapViewer:
    def __init__(self, screen_width=1280, screen_height=720):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.background = pygame.image.load('back.png').convert()
        self.background_x = 0
        self.background_y = 0
        self.scale = 1.0
        self.scale_factor = 0.1
        self.is_dragging = False
        self.previous_mouse_position = pygame.mouse.get_pos()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:  # Колесо мыши вверх - увеличение масштаба
                        mouse_pos = pygame.mouse.get_pos()
                        new_scale = min(self.scale + self.scale_factor, 3.0)  # Ограничение масштаба до 5.0
                        scale_difference = new_scale - self.scale
                        scaled_mouse_pos = ((mouse_pos[0] - self.background_x) / self.scale, (mouse_pos[1] - self.background_y) / self.scale)
                        self.background_x -= scaled_mouse_pos[0] * scale_difference
                        self.background_y -= scaled_mouse_pos[1] * scale_difference
                        self.scale = new_scale
                    elif event.button == 5:  # Колесо мыши вниз - уменьшение масштаба
                        mouse_pos = pygame.mouse.get_pos()
                        new_scale = max(self.scale - self.scale_factor, 0.5)  # Ограничение масштаба до 0.5
                        scale_difference = new_scale - self.scale
                        scaled_mouse_pos = ((mouse_pos[0] - self.background_x) / self.scale, (mouse_pos[1] - self.background_y) / self.scale)
                        self.background_x -= scaled_mouse_pos[0] * scale_difference
                        self.background_y -= scaled_mouse_pos[1] * scale_difference
                        self.scale = new_scale
                    elif event.button == 1:
                        self.is_dragging = True
                        self.previous_mouse_position = pygame.mouse.get_pos()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.is_dragging = False

            # Перемещение изображения
            if self.is_dragging:
                mouse_position = pygame.mouse.get_pos()
                mouse_difference = [(mouse_position[i] - self.previous_mouse_position[i]) for i in range(2)]
                self.background_x += mouse_difference[0]
                self.background_y += mouse_difference[1]
                self.previous_mouse_position = mouse_position

            # Отрисовка изображения
            self.screen.fill((33, 33, 33))
            scaled_image = pygame.transform.scale(self.background,
                                                  (int(self.background.get_width() * self.scale),
                                                   int(self.background.get_height() * self.scale)))
            self.screen.blit(scaled_image, (self.background_x, self.background_y))

            # Обновление экрана
            pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    map_viewer = MapViewer()
    map_viewer.run()
