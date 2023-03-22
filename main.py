import pygame
import settings as settings
import functions as f

pygame.init()

screen = pygame.display.set_mode([settings.WIDTH, settings.HEIGHT])
timer = pygame.time.Clock()

run = True
while run:

    f.timer(timer)
    screen.fill('black')
    f.draw_board(settings.level, screen)
    f.draw_player(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        f.keydown(event)

    pygame.display.flip()
pygame.quit()