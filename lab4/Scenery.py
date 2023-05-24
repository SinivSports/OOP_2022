# Это изменённый код Лабораторной работы №3 студента Александра Стерлина (Вариант 8 (Карпухин) - Вариант 19 (Стерлин))
# Вся цветовая гамма оставлена в оригинальном виде
import pygame
from pygame.draw import *
from math import * # Подключение библиотек
import random

pygame.init()
frames = 30
screen = pygame.display.set_mode((400, 400)) # Создание области для рисования

def elipse(surface, color, rect, angle, width=0): # Функция поворота эллипса
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))

def room(surface, color_1, color_2): # Функция рисования комнаты разными цветами
    screen.fill(color_1)
    polygon(surface, color_2, [(0, 190), (400, 190), (400, 400), (0, 400)])

def window(surface, color_1, color_2, x, y, width, height): #Функция рисования окна
    rect(surface, color_1, (x - width // 2, y - height // 2, width, height))
    rect(surface, color_2, (x - width // 2 + 10, y - height // 2 + 10, width // 2.5, height // 3))
    rect(surface, color_2, (x - width // 2 + 100, y - height // 2 + 10, width // 2.5, height // 3))
    rect(surface, color_2, (x - width // 2 + 10, y - height // 2 + 65, width // 2.5, height // 2))
    rect(surface, color_2, (x - width // 2 + 100, y - height // 2 + 65, width // 2.5, height // 2))

def cat_body(surface, color_body, x, y, width, height): # Функция рисования тела кота
    elipse(surface, (0, 0, 0), (x - width // 2, y - height // 2, width, height + 1), -70, 1)
    elipse(surface, color_body, (x - width // 2, y - height // 2, width, height), -70, 0)
    elipse(surface, (0, 0, 0), (x * 3.7, y - height // 2, width * 2, height - 4), -200, 1)
    elipse(surface, color_body, (x * 3.7, y - height // 2, width * 2, height - 5), -200, 0)
    ellipse(surface, (0, 0, 0), (x - 5, y - height - 11, width * 4 + 1, height * 2 + 2), 1)
    ellipse(surface, color_body, (x - 5, y - height - 10, width * 4, height * 2))
    ellipse(surface, (0, 0, 0), (x - width // 2 - 6, y - height // 2 - 23, width * 1.7 + 2, height * 1.5 + 2), 1)
    ellipse(surface, color_body, (x - width // 2 - 5, y - height // 2 - 22, width * 1.7, height * 1.5))
    ellipse(surface, (0, 0, 0), (x * 3.1 - 1, y - 13, width * 1.4 + 2, height * 1.3 + 2), 1)
    ellipse(surface, color_body, (x * 3.1, y - 12, width * 1.4, height * 1.3))
    ellipse(surface, (0, 0, 0), (x * 4.08 - 1, y + 23, width // 2 - 3, height + 8), 1)
    ellipse(surface, color_body, (x * 4.08, y + 24, width // 2 - 5, height + 6))
    ellipse(surface, (0, 0, 0), (x + width // 2 - 5, y + height // 2.5 - 2, width + 7, height // 1.5 + 2), 1)
    ellipse(surface, color_body, (x + width // 2 - 4, y + height // 2.5 - 1, width + 5, height // 1.5))

def cat_ears(surface, color_ears, x, y, width, height): #Функция рисования ушей кота
    polygon(surface, (0, 0, 0), [(x - width * 1.3, y - height * 1.32 - 2), (x - width - 5, y - 8), (x - width // 2 + 5,
                                                                                                    y - height // 1.5 + 2)], 1)
    polygon(surface, color_ears, [(x - width * 1.3, y - height * 1.32), (x - width - 5, y - 10), (x - width // 2 + 5,
                                                                                                  y - height // 1.5)])
    polygon(surface, (250, 180, 240), [(x - width * 1.3 + 2, y - height * 1.2), (x - width - 3, y - 13), (x - width // 2,
                                                                                                  y - height // 1.5)])
    polygon(surface, (0, 0, 0), [(x + width * 2.3, y - height * 1.34 - 2), (x + width * 2.5, y - 9), (x + width * 2 - 10,
                                                                                                    y - height // 1.5 + 2)], 1)
    polygon(surface, color_ears, [(x + width * 2.3, y - height * 1.34), (x + width * 2.5, y - 11), (x + width * 2 - 10,
                                                                                                    y - height // 1.5)])
    polygon(surface, (250, 180, 240), [(x + width * 2.2 + 2, y - height * 1.2), (x + width * 2.3, y - 14), (x + width * 2 - 6,
                                                                                                    y - height // 1.5)])

def cat_eyes(surface, color_eyes, x, y): # Функция рисования глаз кота
    ellipse(surface, color_eyes, (x, y, 25, 17))
    ellipse(surface, color_eyes, (x + 45, y, 25, 17))
    elipse(surface, (255, 255, 255), (x + 3, y + 3, 13, 4), -220)
    elipse(surface, (255, 255, 255), (x + 48, y + 3, 13, 4), -220)
    ellipse(surface, (0, 0, 0), (x + 60, y, 5, 15))
    ellipse(surface, (0, 0, 0), (x + 15, y, 5, 15))

def cat_nose(surface, x, y): # Функция рисования носа кота
    polygon(surface, (255, 255, 255), [(x - 5, y), (x + 5, y), (x, y + 5)])
    polygon(surface, (0, 0, 0), [(x - 6, y), (x + 6, y), (x, y + 6)], 1)
    line(surface, (0, 0, 0), (x, y + 5), (x, y + 10), 1)
    arc(surface, (0, 0, 0), (x, y, 10, 15), pi, 15 * pi / 8)
    arc(surface, (0, 0, 0), (x - 10, y, 10, 15), pi, 15 * pi / 8)
    arc(surface, (0, 0, 0), (x + 10, y, 70, 30), 0.4, 2.3)
    arc(surface, (0, 0, 0), (x + 10, y + 5, 70, 30), 0.4, 2.3)
    arc(surface, (0, 0, 0), (x + 10, y + 10, 70, 30), 0.4, 2.3)
    arc(surface, (0, 0, 0), (x - 90, y, 70, 30), 0.6, 2.5)
    arc(surface, (0, 0, 0), (x - 90, y + 5, 70, 30), 0.6, 2.5)
    arc(surface, (0, 0, 0), (x - 90, y + 10, 70, 30), 0.6, 2.5)

def ball(surface, color_1, color_2, x, y, width, height, quantity): # Функция рисования клубка
    while quantity > 0:
        quantity -= 1
        ellipse(surface, color_2, (x - width // 2 - 2.5, y - height // 2 - 2.5, width + 5, height + 5), 1)
        ellipse(surface, color_1, (x - width // 2, y - height // 2, width, height))
        arc(surface, color_2, (x - width // 4 + 10, y - height // 2 + 10, width // 2, height // 2), 0, 2 * pi / 3)
        arc(surface, color_2, (x - width // 4, y - height // 2 + 15, width, height // 2), 2 * pi / 3, pi)
        arc(surface, color_2, (x - width // 4 + 10, y - height // 4 + 10, width // 2, height // 2), 0, 2 * pi / 3)
        arc(surface, color_2, (x - width // 6 + 5, y - height // 2 + 44, width // 4, height // 1.2), pi / 2, pi)
        arc(surface, color_2, (x - width // 4 + 25, y - height // 6 + 30, width // 2, height // 2), pi / 2, pi)
        arc(surface, color_1, (x - width * 1.5, y - height // 1.8, width * 3, height), pi, 3 * pi / 2)
        x = random.randrange(50, 350)
        y = random.randrange(175, 350)

    return 0

quantity = int(input("Сколько клубков должно появиться?\n"))

room(screen, (100, 60, 30), (140, 120, 50))
window(screen, (175, 238, 238), (135, 206, 235), 100, 95, 180, 140)
ball(screen, (128, 128, 128,), (0, 0, 0), 140, 350, 120, 80, quantity)
cat_body(screen, (200, 115, 5), 81, 253, 70, 45)
cat_ears(screen, (200, 115, 5), 80, 240, 30, 30)
cat_eyes(screen, (114, 158, 47), 64, 230)
polygon(screen, (255, 255, 255),  [(95, 250), (105, 250), (100, 255)])
cat_nose(screen, 100, 250)

pygame.display.update()
clock = pygame.time.Clock()
exit = False
while not exit:
    clock.tick(frames)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
            