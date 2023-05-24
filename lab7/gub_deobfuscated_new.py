import pygame
from pygame import *
import random
import sys, random, math, fractions, time
pygame.font.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("hueta")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 30))
        self.orig_image = pygame.Surface((60, 30))
        self.image.fill(GREEN)
        self.orig_image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = 10
        self.rect.bottom = HEIGHT / 2
        self.speedy = 0
        self.angle = 0
        self.score1 = 0

    def update(self):
        self.stat = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy = -4
        if keystate[pygame.K_s]:
            self.speedy = 4
        self.rect.y += self.speedy
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        y = self.rect.centery
        x = self.rect.centerx
        xx, yy = pygame.mouse.get_pos()
        self.angle = math.degrees(math.asin((y - yy) / (((x - xx) ** 2 + (y - yy) ** 2) ** 0.5)))
        self.image = pygame.transform.rotozoom(self.orig_image, self.angle, 1)
        self.rect = self.orig_image.get_rect(center=self.rect.center)
        if keystate[pygame.K_q]:
            self.image = pygame.transform.scale2x(self.image)
            self.stat = 1

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)
    def bigshoot(self):
        bulletbig = BulletBIG(self.rect.centerx, self.rect.centery)
        all_sprites.add(bulletbig)
        bulletsbig.add(bulletbig)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(WIDTH - self.rect.width)
        self.rect.bottom = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.speedx = -self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = -self.speedx
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.speedy = -self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
            self.speedy = -self.speedy


class Mob1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(WIDTH - self.rect.width)
        self.rect.bottom = random.randrange(-100, -40)
        self.speedy = 0
        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.speedx = -self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = -self.speedx
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.speedy = -self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
            self.speedy = -self.speedy
        xx = self.rect.centerx
        yy = self.rect.centery
        self.speedx = (player.rect.centerx - xx) / (
                    (abs(xx - player.rect.centerx) + abs(yy - player.rect.centery)) / 5)
        self.speedy = (player.rect.centery - yy) / (
                    (abs(xx - player.rect.centerx) + abs(yy - player.rect.centery)) / 5)


class Mob2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(300, WIDTH)
        self.rect.bottom = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 3)
        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.speedx = -self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = -self.speedx
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.speedy = -self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
            self.speedy = -self.speedy


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        xx, yy = pygame.mouse.get_pos()
        self.speedx = -(player.rect.centerx - xx) / ((abs(xx - player.rect.centerx) + abs(yy - player.rect.centery)) / 20)
        self.speedy = -(player.rect.centery - yy) / ((abs(xx - player.rect.centerx) + abs(yy - player.rect.centery)) / 20)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0:
            self.kill()


class Bullet_BAD(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(0, 0))
        self.rect.bottom = y
        self.rect.centerx = x
        xx = gun.rect.centerx
        yy = gun.rect.centery
        self.speedx = (player.rect.centerx - xx) / ((abs(xx - player.rect.centerx) + abs(yy - player.rect.bottom)) / 10)
        self.speedy = (player.rect.bottom - yy) / ((abs(xx - player.rect.centerx) + abs(yy - player.rect.bottom)) / 10)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.kill()
        if self.rect.left < 0:
            self.rect.left = 0
            self.kill()
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.kill()
        if self.rect.top < 0:
            self.rect.top = 0
            self.kill()


class BulletBIG(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        xx, yy = pygame.mouse.get_pos()
        self.speedx = -(player.rect.centerx - xx) / ((abs(xx - player.rect.centerx) + abs(yy - player.rect.centery)) / 5)
        self.speedy = -(player.rect.centery - yy) / ((abs(xx - player.rect.centerx) + abs(yy - player.rect.centery)) / 5)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0:
            self.kill()


class GunBAD(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 30))
        self.orig_image = pygame.Surface((60, 30))
        self.image.fill(BLUE)
        self.orig_image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH
        self.rect.centery = 0
        self.speedy = random.randrange(1, 3)
        self.speedx = 0
        self.shoot_time = time.time()

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.speedy = -self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
            self.speedy = -self.speedy
        xx = player.rect.centerx
        yy = player.rect.centery
        y = self.rect.centery
        x = self.rect.centerx
        self.angle = -math.degrees(math.asin((y - yy) / (((x - xx) ** 2 + (y - yy) ** 2) ** 0.5)))
        self.image = pygame.transform.rotozoom(self.orig_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def shoot(self):
        bullet_bad = Bullet_BAD(self.rect.x, self.rect.y)
        all_sprites.add(bullet_bad)
        bullets_bad.add(bullet_bad)
        self.shoot_time = time.time()


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
mobsblock = pygame.sprite.Group()
bullets = pygame.sprite.Group()
bulletsbig = pygame.sprite.Group()
bullets_bad = pygame.sprite.Group()
player = Player()
mob = Mob()
gun = GunBAD()
all_sprites.add(player)
all_sprites.add(gun)
for i in range(1):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окнаd
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            player.shoot()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and player.stat == 1:
            player.bigshoot()
        if time.time() - gun.shoot_time > 1:
            gun.shoot()

    # Обновление
    all_sprites.update()

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
        player.score1 += 1
        t = random.randint(1, 10)
        if t == 9:
            m = Mob2()
            all_sprites.add(m)
            mobsblock.add(m)
    bighits = pygame.sprite.groupcollide(mobs, bulletsbig, True, False)
    for hit in bighits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
        player.score1 += 3
        t = random.randint(1, 10)
        if t == 9:
            m = Mob2()
            all_sprites.add(m)
            mobsblock.add(m)
            player.score1 += 5
    blockhits = pygame.sprite.groupcollide(mobsblock, bullets, False, True)
    for hit in blockhits:
        m = Mob1()
        all_sprites.add(m)
        mobs.add(m)

    # Проверка, не ударил ли моб игрока
    hits = pygame.sprite.spritecollide(player, mobs, False) or pygame.sprite.spritecollide(player, bullets_bad, False)
    if hits:
        running = False

    # Рендеринг
    screen.fill(BLACK)
    font = pygame.font.Font(None, 36)
    score = font.render('score: ' + str(player.score1), True, (180, 0, 0))
    screen.blit(score, (10, 50))
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()