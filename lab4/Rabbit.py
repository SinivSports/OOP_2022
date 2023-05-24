def draw_body(surface, x, y, width, height, color):
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_head(surface, x, y, size, color):
    circle(surface, color, (x, y), size // 2)


def draw_ear(surface, x, y, width, height, color):
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))



def draw_leg(surface, x, y, width, height, color):
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))
    # polygon(surface, )


def draw_eyes(surface, x, y, width, height, color):
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_mouth(surface, x, y, width, height, color):
    rect(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_arm(surface, x, y, width, height, color):
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_hare(surface, x, y, width, height, color, size):
    body_width = width // 2
    body_height = height // 2
    body_y = y + body_height // 2
    draw_body(surface, x, body_y, body_width, body_height, color)
    draw_body(surface, x, body_y, body_width // 1.4, body_height // 1.25, (96, 96, 96))
    draw_body(surface, x, body_y, body_width // 1.5, body_height // 1.3, (255, 255, 255))

    head_size = height // 4


    ear_height = height // 3
    ear_y = y - height // 2 + ear_height // 2
    for ear_x in (x - head_size // 4, x + head_size // 4):
        draw_ear(surface, ear_x, ear_y, width // 6, ear_height, color)
        draw_ear(surface, ear_x, ear_y // 0.92, width // 10, ear_height, (96, 96, 96))
        draw_ear(surface, ear_x, ear_y // 0.9, width // 12, ear_height, (255, 153, 204))

    draw_head(surface, x, y - head_size // 2, head_size, color)

    leg_height = height // 16
    leg_y = y + height // 2 - leg_height // 2
    for leg_x in (x - width // 4, x + width // 4):
        draw_leg(surface, leg_x, leg_y, width // 4, leg_height, color)

    eye_height = height // 10
    eye_y = y - height // 6 + eye_height // 4
    for eye_x in (x - head_size // 4, x + head_size // 4):
        draw_eyes(surface, eye_x, eye_y, width // 8, eye_height, (0, 0, 0))
        draw_eyes(surface, eye_x, eye_y, width // 10, eye_height // 1.1, (255, 255, 255))
        draw_eyes(surface, eye_x, eye_y, width // 24, eye_height // 1.1, (50, 150, 225))
        draw_eyes(surface, eye_x, eye_y, width // 24, eye_height // 4, (0, 0, 0))

    mouth_height = height * 1.2
    mouth_height = y + height // 2 - mouth_height // 2
    for mouth_x in (x - width // 32, x + width // 32):
        draw_mouth(surface, mouth_x, mouth_height * 1.038, width // 16, leg_height, (0, 0, 0))
        draw_mouth(surface, mouth_x, mouth_height * 1.030, width // 20, leg_height, (255, 255, 255))

    arm_height = height // 4
    arm_y = y + height // 2 - arm_height // 2
    for arm_x in (x - width // 4, x + width // 4):
        draw_arm(surface, arm_x, arm_y // 1.2, width // 6, arm_height // 4, color)



import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

draw_hare(screen, 300, 300, 300, 350, (200, 200, 200), 20)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

