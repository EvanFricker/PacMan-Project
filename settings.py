import pygame
from map import board
import math
pygame.init()

WIDTH = 510
HEIGHT = 550
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)
level = board
color = 'blue'
PI = math.pi

player_images =[]
for i in range(1, 5):
    player_images.append(pygame.transform.scale(pygame.image.load(f'assets\player_images\P{i}.png'), (35, 35)))
player_x = 250
player_y = 348

direction = 0
counter = 0
