from pygame import *
from random import randint
# подгружаем отдельно функции для работы со шрифтом
font.init()
font1 = font.Font(None, 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))

font2 = font.Font(None, 36)


# нам нужны такие картинки:
img_back = "sky.png" # фон игры
 
img_hero = "rocket.png" # герой
img_enemy = "ball.png" # враг
 
score = 0 # сбито кораблей
goal = 10 # столько кораблей нужно сбить для победы
lost = 0 # пропущено кораблей
max_lost = 3 # проиграли, если пропустили столько
 
# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# класс главного игрока
class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 40:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 40:
            self.rect.y += self.speed

class Enemy(GameSprite):
  
    def update(self):
            global s_y, s_x
            self.rect.x += s_x

s_y = 5
s_x = 5 

win_width = 700
win_height = 500
display.set_caption("Pin-Pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

ball = Enemy(img_enemy, 350, 250, 35, 35, 5)
rocket1 = Player(img_hero, 10, 250, 25, 50, 5)
rocket2 = Player(img_hero, 625, 250, 25, 50, 5)


finish = False
run = True 
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()
    if rocket1.rect.colliderect(ball.rect) or rocket2.rect.colliderect(ball.rect):
        s_x *= -1
 

    if not finish:
        window.blit(background, (0,0))
        ball.update()
        ball.reset()
        rocket1.update()
        rocket2.update2()
        rocket1.reset()
        rocket2.reset()
        display.update()

    time.delay(50)