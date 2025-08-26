import pygame.transform

from configs import *
from missil import *
from direction import *


class Player:
    """Representa o carro controlado pelo jogador."""

    def __init__(self, x, y):
        """Inicializa o jogador com posição e estado padrão."""
        self.__x = x
        self.__y = y
        self.__x_initial = x
        self.__y_initial = y
        self.__speed = 10
        self.__skin = skin.CAR
        self.__missils = []
        # Contador simples para limitar a frequência dos tiros
        self.__cooldown_frames = 10
        self.__direction = direction.RIGHT
        self.__lives = 5

    def draw(self, screen):
        """Desenha o carro do jogador na tela."""
        screen.blit(self.__skin, [self.__x, self.__y])

    def draw_lifes(self, screen):
        """Desenha os ícones de vida do jogador."""
        for x in range(self.__lives):
            screen.blit(
                skin.LIFE, [10 + x * (skin.LIFE.get_width() + 5), 10]
            )

    def lose_life(self):
        """Reduz uma vida e toca o som de colisão."""
        self.__lives -= 1
        sound.CRASH.play()

    def is_dead(self):
        """Retorna True se o jogador ficou sem vidas."""
        return self.__lives <= 0

    def reset(self):
        """Retorna o jogador para a posição inicial."""
        self.__x = self.__x_initial
        self.__y = self.__y_initial

    def move(self, dir):
        """Move o carro na direção especificada."""
        self.__direction = dir

        # Mover o carro numa direção
        if dir == direction.TOP:
            self.__y -= self.__speed
            self.__skin = pygame.transform.rotate(skin.CAR, 90)

            # LIMITE!!
            if self.__y < window.MARGIN:
                self.__y = window.MARGIN
        elif dir == direction.RIGHT:
            self.__x += self.__speed
            self.__skin = skin.CAR

            # LIMITE!!
            if self.__x > window.WIDTH - self.__skin.get_width() - window.MARGIN:
                self.__x = window.WIDTH - self.__skin.get_width() - window.MARGIN
        elif dir == direction.BOTTOM:
            self.__y += self.__speed
            self.__skin = pygame.transform.rotate(skin.CAR, -90)
            self.__skin = pygame.transform.flip(self.__skin, True, False)

            # LIMITE!!
            if self.__y > window.HEIGHT - self.__skin.get_height() - window.MARGIN:
                self.__y = window.HEIGHT - self.__skin.get_height() - window.MARGIN
        else:  # LEFT
            self.__x -= self.__speed
            # self.__skin = pygame.transform.rotate(skin.CAR, 180)
            # self.__skin = pygame.transform.flip(self.__skin, False, True)
            self.__skin = pygame.transform.flip(skin.CAR, True, False)

            # LIMITE!!
            if self.__x < window.MARGIN:
                self.__x = window.MARGIN

    def fire(self):
        """Dispara um míssil se o cooldown permitir."""
        if self.__cooldown_frames < 30:
            return

        center_x = self.__skin.get_width() / 2 + self.__x
        center_y = self.__skin.get_height() / 2 + self.__y

        self.__missils.append(Missil(center_x, center_y, self.__direction))

        sound.MISSIL.play()

        self.__cooldown_frames = 0

    def hits(self, who):
        """Verifica se algum míssil atingiu o alvo."""
        for missil in self.__missils:
            if missil.colides(who):
                self.__missils.remove(missil)
                return True

        return False

    def draw_missils(self, screen):
        """Desenha os míssseis disparados."""
        for missil in self.__missils:
            missil.draw(screen)

    def move_missils(self):
        """Atualiza a posição dos mísseis e cooldown."""
        if self.__cooldown_frames < 30:
            self.__cooldown_frames += 1

        for missil in self.__missils:
            missil.move()

            if missil.is_out():
                self.__missils.remove(missil)

    def step_on(self, poops):
        """Retorna True se o jogador pisar em algum cocô."""
        for poop in poops:
            if self.colides(poop):
                return True

        return False

    # Area de sobreposição
    def get_overlaping_area(self, skin, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__skin)
        who_mask = pygame.mask.from_surface(skin)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    # Verificar colisão
    def colides(self, who):
        return who.get_overlaping_area(self.__skin, self.__x, self.__y) > 0
