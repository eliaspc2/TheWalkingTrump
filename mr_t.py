import random

from configs import *
from direction import *
from poop import *


class MrT:
    """Inimigo principal controlado pela IA."""

    def __init__(self, x, y):
        """Inicializa a posição e estado do inimigo."""
        self.__x = x
        self.__y = y
        self.__x_initial = x
        self.__y_initial = y
        self.__speed = 5
        self.__skin = skin.MR_T
        self.__poops = []
        self.__direction = direction.LEFT
        self.__health = 100

    def shit_himself(self):
        """Adiciona um cocô na lista e toca o som correspondente."""
        self.__poops.append(
            Poop(
                self.__x + self.__skin.get_width() / 2 - skin.POOP.get_width() / 2,
                self.__y + self.__skin.get_height() - skin.POOP.get_height(),
            )
        )
        sound.MASSIVE_FART.play()

    def draw(self, screen):
        """Desenha o inimigo na tela."""
        screen.blit(self.__skin, [self.__x, self.__y])

    def draw_poops(self, screen):
        """Desenha os cocôs produzidos."""
        for poop in self.__poops:
            poop.draw(screen)

    def reset(self):
        """Retorna o inimigo para a posição inicial."""
        self.__x = self.__x_initial
        self.__y = self.__y_initial

    def lose_life(self):
        """Reduz a vida do inimigo."""
        self.__health -= 10

        if self.__health < 0:
            self.__health = 0

    def is_dead(self):
        """Retorna True se o inimigo não tiver mais vida."""
        return self.__health <= 0

    def draw_health(self, screen):
        """Desenha a barra de vida do inimigo."""
        pygame.draw.rect(
            screen,
            "white",
            [630, 5, 310, 20],
            5,
        )

        color = "green"
        if self.__health < 15:
            color = "red"
        elif self.__health < 55:
            color = "yellow"

        pygame.draw.rect(
            screen,
            color,
            [635, 10, self.__health * 3, 10],
            5,
        )

    def move(self):
        """Move o inimigo de acordo com a direção atual."""
        if self.__direction == direction.TOP:
            self.__y -= self.__speed

            # LIMITE
            if self.__y < window.MARGIN:
                self.__y = window.MARGIN
                self.__direction = direction.random()
        elif self.__direction == direction.RIGHT:
            self.__x += self.__speed

            # LIMITE
            if self.__x > window.WIDTH - window.MARGIN - self.__skin.get_width():
                self.__x = window.WIDTH - window.MARGIN - self.__skin.get_width()
                self.__direction = direction.random()
        elif self.__direction == direction.BOTTOM:
            self.__y += self.__speed

            # LIMITE
            if self.__y > window.HEIGHT - window.MARGIN - self.__skin.get_height():
                self.__y = window.HEIGHT - window.MARGIN - self.__skin.get_height()
                self.__direction = direction.random()
        else:  # LEFT
            self.__x -= self.__speed

            # LIMITE
            if self.__x < window.MARGIN:
                self.__x = window.MARGIN
                self.__direction = direction.random()

        if random.randint(0, 100) < 5:
            self.__direction = direction.random()

    def get_poops(self):
        """Retorna a lista de cocôs criados."""
        return self.__poops

    # Area de sobreposição
    def get_overlaping_area(self, skin, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__skin)
        who_mask = pygame.mask.from_surface(skin)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    # Verificar colisão
    def colides(self, who):
        return who.get_overlaping_area(self.__skin, self.__x, self.__y) > 0
