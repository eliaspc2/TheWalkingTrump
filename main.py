import pygame
from pygame.locals import *

from configs import *
from player import *
from direction import *
from mr_t import *

# Inicialização do pygame e da janela do jogo
pygame.init()
screen = pygame.display.set_mode([window.WIDTH, window.HEIGHT])
pygame.display.set_caption(window.TITLE)

# Inicia a música de fundo em loop
sound.BACKGROUND.play(loops=-1)

# Instancia o jogador e o inimigo principal
player = Player(50, 230)
mr_t = MrT(800, 400)

clock = pygame.time.Clock()
while True:
    # Controla o FPS do jogo
    dt = clock.tick(60)

    # Verifica eventos (fechar a janela, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)

    # Desenha o fundo
    screen.blit(skin.BACKGROUND, [0, 0])

    key_pressed = pygame.key.get_pressed()

    # Verifica se o jogador perdeu
    if player.is_dead():
        screen.blit(
            skin.GAMEWIN,
            [
                window.WIDTH / 2 - skin.GAMEWIN.get_width() / 2,
                window.HEIGHT / 2 - skin.GAMEWIN.get_height() / 2,
            ],
        )

        # Enter para recomeçar
        if key_pressed[pygame.K_RETURN]:
            player = Player(50, 230)
            mr_t = MrT(800, 400)

        pygame.display.update()
        continue
    # Verifica se o inimigo perdeu (jogador ganhou)
    elif mr_t.is_dead():
        screen.blit(
            skin.GAMEOVER,
            [
                window.WIDTH / 2 - skin.GAMEOVER.get_width() / 2,
                window.HEIGHT / 2 - skin.GAMEOVER.get_height() / 2,
            ],
        )

        # Enter para recomeçar
        if key_pressed[pygame.K_RETURN]:
            player = Player(50, 230)
            mr_t = MrT(800, 400)

        pygame.display.update()
        continue

    # Movimentação do jogador via teclado
    if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
        player.move(direction.TOP)
    elif key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
        player.move(direction.RIGHT)
    elif key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
        player.move(direction.BOTTOM)
    elif key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
        player.move(direction.LEFT)

    # Atirar
    if key_pressed[pygame.K_SPACE]:
        player.fire()

    # Atualiza posições dos objetos
    player.move_missils()
    mr_t.move()

    # Desenha os objetos na tela
    mr_t.draw_poops(screen)

    player.draw(screen)
    player.draw_lifes(screen)

    mr_t.draw(screen)
    mr_t.draw_health(screen)

    player.draw_missils(screen)

    # Trata colisões
    if player.hits(mr_t):
        mr_t.lose_life()
        mr_t.shit_himself()

    if player.colides(mr_t) or player.step_on(mr_t.get_poops()):
        player.lose_life()
        player.reset()
        mr_t.reset()

    pygame.display.update()
