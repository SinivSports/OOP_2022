import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1400, 600))
COLOR = 255,255,255
screen.fill(COLOR)
circle(screen, (255, 255, 0), (150, 175), 120)
circle(screen, (0, 0, 0), (150, 175), 123, 3)
circle(screen, (255, 0, 0), (200, 175),50)
circle(screen, (0, 0, 0), (200, 175), 20)
circle(screen, (255, 0, 0), (100, 175),40)
circle(screen, (0, 0, 0), (100, 175), 16)
polygon(screen, (0, 0, 0), [(100,250), (200,250),
                            (200,275), (100,275)])
polygon(screen, (0, 0, 0), [(70,110), (150,140),
                            (145,145), (75,115)])
polygon(screen, (0, 0, 0), [(240,90), (150,140),
                            (155,145), (245,85)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()


