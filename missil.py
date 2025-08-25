import pygame.transform

from configs import *
from direction import *

class Missil:
    def __init__(self, center_x, center_y, dir):
        self.__speed = 10
        self.__direction = dir

        if dir == direction.TOP:
            self.__skin = pygame.transform.rotate(skin.MISSIL, 90)
        elif dir == direction.RIGHT:
            self.__skin = skin.MISSIL
        elif dir == direction.BOTTOM:
            self.__skin = pygame.transform.flip(
                pygame.transform.rotate(skin.MISSIL, -90),
                True,
                False
            )
        else: # LEFT
            self.__skin = pygame.transform.flip(skin.MISSIL, True, False)

        self.__x = center_x - self.__skin.get_width() / 2
        self.__y = center_y - self.__skin.get_height() / 2

    def move(self):
        if self.__direction == direction.TOP:
            self.__y -= self.__speed
        elif self.__direction == direction.RIGHT:
            self.__x += self.__speed
        elif self.__direction == direction.BOTTOM:
            self.__y += self.__speed
        else: # LEFT
            self.__x -= self.__speed

    def draw(self, screen):
        screen.blit(self.__skin, [self.__x, self.__y])

    def is_out(self):
        # Não simplificado
        """if self.__y < - self.__skin.get_height():
            return True
        elif self.__x > window.WIDTH:
            return True
        elif self.__y > window.HEIGHT:
            return True
        elif self.__x < - self.__skin.get_width():
            return True
        else:
            return False"""

        # Simplificado
        return (
            self.__y < - self.__skin.get_height() or # TOP
            self.__x > window.WIDTH or # RIGHT
            self.__y > window.HEIGHT or # Bottom
            self.__x < - self.__skin.get_width() # LEFT
        )

    # Area de sobreposição
    def get_overlaping_area(self, skin, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__skin)
        who_mask = pygame.mask.from_surface(skin)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    # Verificar colisão
    def colides(self, who):
        return who.get_overlaping_area(self.__skin, self.__x, self.__y) > 0

