import pygame
import settings as settings

def keydown (event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                settings.direction = 0
            if event.key == pygame.K_LEFT:
                settings.direction = 1
            if event.key == pygame.K_UP:
                settings.direction = 2
            if event.key == pygame.K_DOWN:
                settings.direction = 3

def timer (timer):
    timer.tick(settings.fps)
    if settings.counter < 19:
        settings.counter += 1
    else:
        settings.counter = 0

def draw_board(level, screen):
    y = ((settings.HEIGHT - 50) // 32)
    x = (settings.WIDTH // 30)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * x + (0.5 * x), i * y + (0.5 * y)), 4)
            if level[i][j] == 2:
                pygame.draw.circle(screen, 'white', (j * x + (0.5 * x), i * y + (0.5 * y)), 10)
            if level[i][j] == 3:
                pygame.draw.line(screen, settings.color, (j * x + (0.5 * x), i * y), (j * x + (0.5 * x), i * y + y), 3)
            if level[i][j] == 4:
                pygame.draw.line(screen, settings.color, (j * x, i * y + (0.5 * y)), (j * x + x, i * y + (0.5 * y)), 3)
            if level[i][j] == 5:
                pygame.draw.arc(screen, settings.color, [(j * x - (0.5 * x)), (i * y + (0.5 * y)), x, y], 0, settings.PI/2, 3)
            if level[i][j] == 6:
                pygame.draw.arc(screen, settings.color, [(j * x + (0.5 * x)), (i * y + (0.5 * y)), x, y], settings.PI/2, settings.PI, 3)
            if level[i][j] == 7:
                pygame.draw.arc(screen, settings.color, [(j * x + (0.5 * x)), (i * y - (0.5 * y)), x, y], settings.PI, (3 * settings.PI)/2, 3)
            if level[i][j] == 8:
                pygame.draw.arc(screen, settings.color, [(j * x - (0.5 * x)), (i * y - (0.5 * y)), x, y], (3*settings.PI)/2, 2*settings.PI, 3)
            if level[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * x, i * y + (0.5 * y)), (j * x + x, i * y + (0.5 * y)), 3)

def draw_player(screen):
    if settings.direction == 0:
        screen.blit(settings.player_images[settings.counter // 5], (settings.player_x, settings.player_y))
    elif settings. direction == 1:
        screen.blit(pygame.transform.flip(settings.player_images[settings.counter // 5], True, False), (settings.player_x, settings.player_y))
    elif settings.direction == 2:
        screen.blit(pygame.transform.rotate(settings.player_images[settings.counter // 5], 90), (settings.player_x, settings.player_y))
    elif settings.direction == 3:
        screen.blit(pygame.transform.rotate(settings.player_images[settings.counter // 5], 270), (settings.player_x, settings.player_y))

