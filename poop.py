from configs import *
class Poop:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__skin = skin.POOP

    def draw(self, screen):
        screen.blit(self.__skin, [self.__x, self.__y])

    # Area de sobreposição
    def get_overlaping_area(self, skin, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__skin)
        who_mask = pygame.mask.from_surface(skin)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    # Verificar colisão
    def colides(self, who):
        return who.get_overlaping_area(self.__skin, self.__x, self.__y) > 0