#создай игру "Лабиринт"!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self,player_image, player_x, player_y, player_speed, contros):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.up = contros['up']
        self.down = contros['down']
        self.left = contros['left']
        self.right = contros['right']
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[self.up] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[self.down] and self.rect.y < 430:
            self.rect.y += self.speed
        if key_pressed[self.left] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key_pressed[self.right] and self.rect.x < 630:
            self.rect.x += self.speed


class Enemy(GameSprite):
    def __init__(self,player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.stop_x1 = self.rect.x - self.speed * 80
        self.stop_x2 = self.rect.x
        self.a = 1
    def update(self):
        if self.a == 1 and self.rect.x > self.stop_x1:
            self.rect.x -=2
        else:
            self.a = 0
        if self.a == 0 and self.rect.x < self.stop_x2:
            self.rect.x +=2
        else:
            self.a = 1
            

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width,self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))





contros = {
    'up' : K_w,
    'down' : K_s,
    'left' : K_a,
    'right' : K_d,
}        
    


window = display.set_mode((700,500))
display.set_caption('Лабиринт')

win_width = 700
win_height = 500
background = transform.scale(image.load('background.jpg'), (win_width,win_height))
hero = Player('hero.png', 5, win_height - 80, 4,contros)
cyborg = Enemy('cyborg.png', win_width - 70, 255, 2)
treasure = GameSprite('treasure.png', win_width - 160, win_height - 60, 0)

wall1 = Wall(0, 0, 0, 100, win_height-400, 22, 400)
wall2 = Wall(0, 0, 0, 252, 0, 22, win_height-150)
wall3 = Wall(0, 0, 0, 438, win_height-400, 22, 400)
wall4 = Wall(0, 0, 0, 252, win_height-150, 65, 22)
wall5 = Wall(0, 0, 0, 438-65, win_height-300, 65, 22)
wall6 = Wall(0, 0, 0, 438, win_height-400, 150, 22)
wall7 = Wall(0, 0, 0, win_width-150, win_height-275, 150, 22)
wall8 = Wall(0, 0, 0, 460, win_height-90, 150, 22)
wall9 = Wall(0, 0, 0, 100, win_height-0, 400, 22)



mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')

font.init()
font = font.SysFont('Arial',70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (255, 0, 0))

clock = time.Clock()
FPS = 80

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background, (0, 0))
        hero.reset()
        cyborg.reset()
        treasure.reset()

        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
        wall9.draw_wall()

        
        hero.update() 
        cyborg.update()

        if sprite.collide_rect(hero, cyborg) or sprite.collide_rect(hero, wall1) or sprite.collide_rect(hero, wall2) or sprite.collide_rect(hero, wall3) or sprite.collide_rect(hero, wall4) or sprite.collide_rect(hero, wall5) or sprite.collide_rect(hero, wall6) or sprite.collide_rect(hero, wall7) or sprite.collide_rect(hero, wall8) or sprite.collide_rect(hero, wall9):
            finish = True
            kick.play()
            window.blit(lose, (200, 200))

        if sprite.collide_rect(hero, treasure):
            finish = True
            money.play()
            window.blit(win, (200, 200))

    display.update()
    clock.tick(FPS)
    


