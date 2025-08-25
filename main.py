import pygame
from pygame.locals import *
from configs import *
from player import *
from direction import *
from trump import *

pygame.init()
screen = pygame.display.set_mode([window.WIDTH, window.HEIGHT])
pygame.display.set_caption(window.TITLE)

sound.BACKGROUND.play(loops=-1)

player = Player(50, 230)
trump = Trump(800, 400)

clock = pygame.time.Clock()
while True:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)

    screen.blit(skin.BACKGROUND, [0, 0])

    key_pressed = pygame.key.get_pressed()

    # Jogador perdeu
    if player.is_dead():
        screen.blit(
            skin.GAMEWIN,
            [
                window.WIDTH / 2 - skin.GAMEWIN.get_width() / 2,
                window.HEIGHT / 2 - skin.GAMEWIN.get_height() / 2
            ]
        )

        # Enter para recomeçar
        if key_pressed[pygame.K_RETURN]:
            player = Player(50, 230)
            trump = Trump(800, 400)

        pygame.display.update()
        continue
    # Trump perdeu (Jogador ganhou)
    elif trump.is_dead():
        screen.blit(
            skin.GAMEOVER,
            [
                window.WIDTH / 2 - skin.GAMEOVER.get_width() / 2,
                window.HEIGHT / 2 - skin.GAMEOVER.get_height() / 2
            ]
        )

        # Enter para recomeçar
        if key_pressed[pygame.K_RETURN]:
            player = Player(50, 230)
            trump = Trump(800, 400)

        pygame.display.update()
        continue

    if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
        player.move(direction.TOP)
    elif key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
        player.move(direction.RIGHT)
    elif key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
        player.move(direction.BOTTOM)
    elif key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
        player.move(direction.LEFT)

    if key_pressed[pygame.K_SPACE]:
        player.fire()

    # Movimentos
    player.move_missils()
    trump.move()

    # Desenhar
    trump.draw_poops(screen)

    player.draw(screen)
    player.draw_lifes(screen)

    trump.draw(screen)
    trump.draw_health(screen)

    player.draw_missils(screen)

    if player.hits(trump):
        trump.lose_life()
        trump.shit_himself()

    if player.colides(trump) or player.step_on(trump.get_poops()):
        player.lose_life()
        player.reset()
        trump.reset()

    pygame.display.update()