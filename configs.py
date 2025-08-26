import pygame

# Inicializa os módulos principais do pygame
pygame.init()
pygame.mixer.init()


# Configurações básicas da janela do jogo
class window:
    WIDTH = 946
    HEIGHT = 549
    TITLE = "The Walking Mr. T"
    MARGIN = 30


# Espaço reservado para definição de fontes (não utilizado)
class font:
    ...


# Carrega e configura os sons utilizados no jogo
class sound:
    BACKGROUND = pygame.mixer.Sound("sounds/background.mp3")
    BACKGROUND.set_volume(0.50)

    MASSIVE_FART = pygame.mixer.Sound("sounds/massive_fart.mp3")
    MASSIVE_FART.set_volume(0.50)

    MISSIL = pygame.mixer.Sound("sounds/missile.mp3")
    MISSIL.set_volume(0.50)

    CRASH = pygame.mixer.Sound("sounds/crash.mp3")
    CRASH.set_volume(0.50)

    GAMEOVER = pygame.mixer.Sound("sounds/gameover.mp3")
    GAMEOVER.set_volume(0.50)


# Carrega as imagens utilizadas no jogo
class skin:
    BACKGROUND = pygame.image.load("imgs/background.png")
    CAR = pygame.image.load("imgs/car.png")
    LIFE = pygame.image.load("imgs/life.png")
    MISSIL = pygame.image.load("imgs/missil.png")
    POOP = pygame.image.load("imgs/poop.png")
    MR_T = pygame.image.load("imgs/mr_t.png")
    GAMEOVER = pygame.image.load("imgs/gameover.png")
    GAMEWIN = pygame.image.load("imgs/gamewin.png")
