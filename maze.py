#создай игру "Лабиринт"!
from pygame import *
import pygame
pygame.init()
pygame.font.init()
mixer.init()

#создай окно игры
WIDTH = 700
HEIGHT = 500
FPS = 60 

wi = display.set_mode((WIDTH, HEIGHT))

font = pygame.font.Font(None, 70)
win = font.render("YOU WIN", True, (255, 215, 0))
lose = font.render("YOU LOSE", True, (180, 0, 0))

p1x = 600
p1y = 420

clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, p1x, p1y, player_speen):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = p1x
        self.rect.y = p1y
        self.speen = player_speen

    def reset(self):
        wi.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speen
        if keys[K_RIGHT] and self.rect.x < WIDTH - 80:
            self.rect.x += self.speen
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speen
        if keys[K_DOWN] and self.rect.y < HEIGHT - 80:
            self.rect.y += self.speen

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 450:
            self.direction = "right"
        elif self.rect.x >= WIDTH - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speen
        else:
            self.rect.x += self.speen

cyborg = Enemy('cyborg.png', 450, 300, 3)
hero = Player('hero.png', 100, 300, 3)
final = GameSprite("treasure.png", 600, 420, 0)
money = transform.scale(image.load("treasure.png"), (70, 70))

class Wall(pygame.sprite.Sprite):
    def __init__(
        self,
        color: (176, 106, 255),
        wall_x: int,
        wall_y: int,
        wall_width: int,
        wall_height: int,
        wi: pygame.Surface,
    ):
        super().__init__()
        self.color = color
        self.width = wall_width
        self.height = wall_height

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        self.wi = wi
    def draw_wall(self):
        self.wi.blit(self.image, (self.rect.x, self.rect.y))

w1 = Wall((176, 106, 255), 100, 20, 450, 10, wi)
w2 = Wall((176, 106, 255), 100, 30, 10, 260, wi)
w3 = Wall((176, 106, 255), 100, 380, 10, 90, wi)
w4 = Wall((176, 106, 255), 100, 460, 450, 10, wi)
w5 = Wall((176, 106, 255), 100, 380, 80, 10, wi)
w6 = Wall((176, 106, 255), 100, 280, 160, 10, wi)
w7 = Wall((176, 106, 255), 250, 30, 10, 130, wi)
w8 = Wall((176, 106, 255), 260, 280, 10, 90, wi)
w9 = Wall((176, 106, 255), 180, 150, 70, 10, wi)
w10 = Wall((176, 106, 255), 180, 90, 10, 110, wi)
w11 = Wall((176, 106, 255), 370, 120, 10, 250, wi)
w12 = Wall((176, 106, 255), 370, 360, 180, 10, wi)
w13 = Wall((176, 106, 255), 370, 280, 180, 10, wi)
w14 = Wall((176, 106, 255), 540, 30, 10, 90, wi)
w15 = Wall((176, 106, 255), 470, 120, 80, 10, wi)
w16 = Wall((176, 106, 255), 470, 120, 10, 80, wi)
w17 = Wall((176, 106, 255), 550, 210, 10, 80, wi)
w18 = Wall((176, 106, 255), 550, 360, 10, 110, wi)

display.set_caption("Лабиринт")
mixer.music.load("jungles.ogg")
background = transform.scale(image.load("background.jpg"), (700, 500))
mixer.music.play()

game = True
fihish = False
while game:
    clock.tick(FPS)
    

    for e in pygame.event.get():
        if e.type == QUIT:
            game = False
    if fihish != True:
        hero.update()
        cyborg.update()

        wi.blit(background,(0, 0))
        wi.blit(money,(p1x, p1y))
        hero.reset()
        cyborg.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()
        w14.draw_wall()
        w15.draw_wall()
        w16.draw_wall()
        w17.draw_wall()
        w18.draw_wall()
        
        pygame.display.update()

    if (
        pygame.sprite.collide_rect(hero, cyborg)
        or pygame.sprite.collide_rect(hero, w1)
        or pygame.sprite.collide_rect(hero, w2)
        or pygame.sprite.collide_rect(hero, w3)
        or pygame.sprite.collide_rect(hero, w4)
        or pygame.sprite.collide_rect(hero, w5)
        or pygame.sprite.collide_rect(hero, w6)
        or pygame.sprite.collide_rect(hero, w7)
        or pygame.sprite.collide_rect(hero, w8)
        or pygame.sprite.collide_rect(hero, w9)
        or pygame.sprite.collide_rect(hero, w10)
        or pygame.sprite.collide_rect(hero, w11)
        or pygame.sprite.collide_rect(hero, w12)
        or pygame.sprite.collide_rect(hero, w13)
        or pygame.sprite.collide_rect(hero, w14)
        or pygame.sprite.collide_rect(hero, w15)
        or pygame.sprite.collide_rect(hero, w16)
        or pygame.sprite.collide_rect(hero, w17)
        or pygame.sprite.collide_rect(hero, w18)
    ):
        fihish = True
        wi.blit(lose, (250, 250))
        kick = mixer.Sound("kick.ogg")
        kick.play()
        pygame.display.update()

    if (pygame.sprite.collide_rect(hero, final)):
        fihish = True
        wi.blit(win, (250, 250))
        money = mixer.Sound("money.ogg")
        money.play()
        pygame.display.update()