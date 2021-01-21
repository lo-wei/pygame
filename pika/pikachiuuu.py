import random
import time
import pygame
import sys
import math
from pygame.locals import *

pygame.init()

WIDTH = 600
HEIGHT = 420
SIZE = 30
ground_line = HEIGHT-SIZE*2-SIZE/2
base = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pikaaaaa")
surf = pygame.Surface(base.get_size()).convert()


bg_org = pygame.image.load('bg.jpg').convert()
bg_img = pygame.transform.scale(bg_org, base.get_size())
cloud_img = pygame.image.load('cloud.gif').convert()
cloud_rect = cloud_img.get_rect()
ground_org = pygame.image.load('ground.png').convert()
ground_img = pygame.transform.scale(ground_org, (SIZE,SIZE))
ground_red_org = pygame.image.load('ground_red.png').convert()
ground_red_img = pygame.transform.scale(ground_red_org, (SIZE,SIZE))
line1_org = pygame.image.load('line1.png').convert()
line1_img = pygame.transform.scale(line1_org, (SIZE,SIZE))
line2_org = pygame.image.load('line2.png').convert()
line2_img = pygame.transform.scale(line2_org, (SIZE,SIZE))
line3_org = pygame.image.load('line3.png').convert()
line3_img = pygame.transform.scale(line3_org, (SIZE,SIZE))
sea_org = pygame.image.load('sea.gif').convert()
sea_img = pygame.transform.scale(sea_org, (SIZE,SIZE))
sea1_org = pygame.image.load('sea1.gif').convert()
sea1_img = pygame.transform.scale(sea1_org, (SIZE,SIZE))
pillar_org = pygame.image.load('pillar.gif').convert()
pillar_img = pygame.transform.scale(pillar_org, (10,150))
pillar_rect = pillar_img.get_rect()
pillar_head_org = pygame.image.load('pillar_head.gif').convert()
pillar_head_img = pygame.transform.scale(pillar_head_org, (11,11))
pillar_head_rect = pillar_head_img.get_rect()
pikal_org = pygame.image.load('pika_left1.gif').convert()   # ---pikal gif---
pikal_img = pygame.transform.scale(pikal_org, (87,89))
pikal_rect = pikal_img.get_rect()
pikal2_org = pygame.image.load('pika_left2.gif').convert()
pikal2_img = pygame.transform.scale(pikal2_org, (87,89))
pikal3_org = pygame.image.load('pika_left3.gif').convert()
pikal3_img = pygame.transform.scale(pikal3_org, (87,89))
pikal4_org = pygame.image.load('pika_left4.gif').convert()
pikal4_img = pygame.transform.scale(pikal4_org, (87,89))
pikal5_org = pygame.image.load('pika_left5.gif').convert()
pikal5_img = pygame.transform.scale(pikal5_org, (87,89))     # -^-pikal gif-^-
pikar_org = pygame.image.load('pika_right.gif').convert()
pikar_img = pygame.transform.scale(pikar_org, (87,89))
pikar_rect = pikar_img.get_rect()

pikapuL1_org = pygame.image.load('pu1_L.gif').convert()
pikapuL1_img = pygame.transform.scale(pikapuL1_org, (94,86))
pikapuL1_rect = pikapuL1_img.get_rect()
pikapuL2_org = pygame.image.load('pu2_L.gif').convert()
pikapuL2_img = pygame.transform.scale(pikapuL2_org, (93,93))
pikapuL2_rect = pikapuL1_img.get_rect()
pikapuL3_org = pygame.image.load('pu3_L.gif').convert()
pikapuL3_img = pygame.transform.scale(pikapuL1_org, (91,80))
pikapuL3_rect = pikapuL3_img.get_rect()
pikapuR1_org = pygame.image.load('pu1_R.gif').convert()
pikapuR1_img = pygame.transform.scale(pikapuR1_org, (94,86))
pikapuR1_rect = pikapuR1_img.get_rect()
pikapuR2_org = pygame.image.load('pu2_R.gif').convert()
pikapuR2_img = pygame.transform.scale(pikapuR2_org, (93,93))
pikapuR2_rect = pikapuR2_img.get_rect()
pikapuR3_org = pygame.image.load('pu3_R.gif').convert()
pikapuR3_img = pygame.transform.scale(pikapuR3_org, (91,80))
pikapuR3_rect = pikapuR3_img.get_rect()

ball1_org = pygame.image.load('ball1.gif').convert()
ball1_img = pygame.transform.scale(ball1_org, (60,60))
ball_rect = ball1_img.get_rect()
zero_img = pygame.image.load('zero.gif').convert()
one_img = pygame.image.load('one.gif').convert()
two_img = pygame.image.load('two.gif').convert()
three_img = pygame.image.load('three.gif').convert()
four_img = pygame.image.load('four.gif').convert()
five_img = pygame.image.load('five.gif').convert()
six_img = pygame.image.load('six.gif').convert()
seven_img = pygame.image.load('seven.gif').convert()
eight_img = pygame.image.load('eight.gif').convert()
nine_img = pygame.image.load('nine.gif').convert()
ten_img = pygame.image.load('ten.gif').convert()
over_org = pygame.image.load('game_set.gif').convert()
ready_org = pygame.image.load('ready.gif').convert()
restart_org = pygame.image.load('restart_text.gif').convert()
restart_img = pygame.transform.scale(restart_org, (300,15))
restart_rect = restart_img.get_rect()
hole1_img = pygame.image.load('hole1.gif').convert()
hole2_img = pygame.image.load('hole2.gif').convert()
hole3_img = pygame.image.load('hole3.gif').convert()
hole4_img = pygame.image.load('hole4.gif').convert()

p_org = pygame.image.load('p.gif').convert()
p_img = pygame.transform.scale(p_org, (178,112))

control_img = pygame.image.load('control.gif').convert()


'''
pikawin_org = pygame.image.load('pikawin.gif').convert()
pikawin_img = pygame.transform.scale(pikawin_org, (87,89))
pikalose_org = pygame.image.load('pikalose.gif').convert()
pikalose_img = pygame.transform.scale(pikalose_org, (87,89))
'''


class Cloud():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self):
        self.x += 3
        if cloud_rect.left > WIDTH:
            self.x = -106
            
    def draw(self):
        surf.blit(cloud_img, cloud_rect)
        
    def update(self):
        cloud_rect.topleft = (self.x, self.y)

class Ball():
    
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx    # 水平座標速度
        self.vy = vy    # 垂直座標速度
        self.gy = 2     # 重力加速度
        self.fx = 3     # friction

    def move(self, cloud, pikal, pikar, switch_pikal, over, left_score, right_score, move_right):
        self.fx -= self.fx
        self.x += self.vx
        self.vy += self.gy
        self.y += self.vy/3

        #detect ball collision
        ball_rect.topleft = (self.x, self.y)
        if ball_rect.bottom > ground_line: #球撞地
            self.y = ground_line - ball_rect.height
            self.vy = -self.vy
        
        if ball_rect.top < 0: #球撞天
            self.y = 0
            self.vy = -self.vy/2
           
        if ball_rect.left < 0:  #球撞左
            self.x = 0
            self.vx = -self.vx
        if ball_rect.right > WIDTH:    #球撞右
            self.x = WIDTH - ball_rect.height
            self.vx = -self.vx

        if collision(ball_rect, pikal.rect):    #球撞皮卡左
            if (ball_rect.bottom - ball_rect.height/3) >= pikal.rect.top \
               and (ball_rect.bottom - ball_rect.height/3) <= (pikal.rect.top + pikal.rect.height/2): #球撞皮卡左.頭[1,2,3,4]
                self.y = pikal.rect.top - ball_rect.height
                self.vy = -self.vy
                if ball_rect.centerx > (pikal.rect.left + pikal.rect.width*(3/4)) \
                   and ball_rect.centerx < pikal.rect.right:       #球撞皮卡左.頭[4]
                    self.vx = 10
                elif ball_rect.centerx > (pikal.rect.left + pikal.rect.width*(2/4)) \
                   and ball_rect.centerx < (pikal.rect.left + pikal.rect.width*(3/4)): #球撞皮卡左.頭[3]
                    self.vx = 5
                elif ball_rect.centerx > (pikal.rect.left + pikal.rect.width*(1/4)) \
                   and ball_rect.centerx < (pikal.rect.left + pikal.rect.width*(2/4)): #球撞皮卡左.頭[2]
                    self.vx = 3
                elif ball_rect.centerx > pikal.rect.left \
                   and ball_rect.centerx < (pikal.rect.left + pikal.rect.width*(1/4)): #球撞皮卡左.頭[1]
                    self.vx = 1
            elif ball_rect.right > pikal.rect.left \
                 and ball_rect.right < (pikal.rect.left + 10): #球撞皮卡左.背
                self.x = pikal.rect.left - ball_rect.width
                self.vx = -self.vx
            elif ball_rect.left < pikal.rect.right \
                 and ball_rect.left > (pikal.rect.right - 10): #球撞皮卡左.臉
                self.x = pikal.rect.right
                self.vx = -self.vx
            

        if collision(ball_rect, pikar.rect):    #球撞皮卡右
            if (ball_rect.bottom - ball_rect.height/3) >= pikar.rect.top \
               and (ball_rect.bottom - ball_rect.height/3) <= (pikar.rect.top + pikar.rect.height/2): #球撞皮卡右.頭[1,2,3,4]
                self.y = pikar.rect.top - ball_rect.height
                self.vy = -self.vy
                if ball_rect.centerx > (pikar.rect.left + pikar.rect.width*(3/4)) \
                   and ball_rect.centerx < pikar.rect.right:       #球撞皮卡右.頭[4]
                    self.vx = -1
                elif ball_rect.centerx > (pikar.rect.left + pikar.rect.width*(2/4)) \
                   and ball_rect.centerx < (pikar.rect.left + pikar.rect.width*(3/4)): #球撞皮卡右.頭[3]
                    self.vx = -3
                elif ball_rect.centerx > (pikar.rect.left + pikar.rect.width*(1/4)) \
                   and ball_rect.centerx < (pikar.rect.left + pikar.rect.width*(2/4)): #球撞皮卡右.頭[2]
                    self.vx = -5
                elif ball_rect.centerx > pikar.rect.left \
                   and ball_rect.centerx < (pikar.rect.left + pikar.rect.width*(1/4)): #球撞皮卡右.頭[1]
                    self.vx = -10
            elif ball_rect.right > pikar.rect.left \
                 and ball_rect.right < (pikar.rect.left + 10): #球撞皮卡右.臉
                self.x = pikar.rect.left - ball_rect.width
                self.vx = -self.vx
            elif ball_rect.left < pikar.rect.right \
                 and ball_rect.left > (pikar.rect.right - 10): #球撞皮卡右.背
                self.x = pikar.rect.right
                self.vx = -self.vx
                
        if collision(ball_rect, pillar_rect):   #球撞桿
            if ball_rect.bottom > pillar_rect.top \
                and ball_rect.bottom < (pillar_rect.top + 10): #球撞桿頭
                if self.vy < 0: #球往下撞
                    self.y = pillar_rect.top - ball_rect.height
                    self.vy = -self.vy
            if ball_rect.right > pillar_rect.left \
                  and ball_rect.right < pillar_rect.right + 10: #球撞桿左
                self.x = pillar_rect.left - ball_rect.width
                self.vx = -self.vx
            if ball_rect.left < pillar_rect.right \
                  and ball_rect.left > pillar_rect.left - 10: #球撞桿右
                self.x = pillar_rect.right
                self.vx = -self.vx

        if ball_rect.top <= cloud_rect.bottom and ball_rect.top >= cloud_rect.top and over == False:  #黑洞
            if ball_rect.centerx < cloud_rect.right and ball_rect.centerx > cloud_rect.left:
                if self.vy > 0: #球往上撞
                    holes = [hole1_img, hole2_img, hole3_img, hole4_img]
                    
                    for i in range(4):  #吸球
                        hole_rect = holes[i].get_rect()
                        hole_rect.bottom = cloud_rect.bottom
                        hole_rect.centerx = cloud_rect.centerx
                        surf.blit(holes[i], hole_rect)
                        base.blit(surf ,(0,0))
                        pygame.display.update()
                        time.sleep(0.1)

                    move_right = background(left_score, right_score, move_right)
                    cloud.move()
                    cloud.update()
                    cloud.draw()
                    switch_pikal %= 5
                    switch_pikal = pikal.draw(switch_pikal)
                    pikar.draw()
                    base.blit(surf ,(0,0))
                    pygame.display.update()
                    
                    self.x = random.randint(0, WIDTH - ball_rect.width)
                    self.vy = -(self.vy * 5) 
                    ball_rect.topleft = (self.x, self.y)
                    
                    for i in range(4):  #吐球
                        hole_rect = holes[i].get_rect()
                        hole_rect.bottom = cloud_rect.bottom
                        hole_rect.centerx = ball_rect.centerx
                        surf.blit(holes[i], hole_rect)
                        base.blit(surf ,(0,0))
                        pygame.display.update()
                        time.sleep(0.1)
                        
    def draw(self):
        surf.blit(ball1_img, (self.x, self.y))

class Pikal():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.puisleft = False
        self.ispu = False
        self.switch_pikapu = 0
        self.isJump = False
        self.jumpCount = 10
        self.img = pikal_img
        self.rect = self.img.get_rect()
        #self.v = 8 #velocity
        #self.m = 2 #mass

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_a] and self.x > (SIZE/2):
            self.x -= 5
        if pressed_keys[K_d] and (self.x+self.rect.width) < pillar_rect.left:
            self.x += 5

    def pu(self):
        if self.ispu:
            pressed_keys = pygame.key.get_pressed()
            if (pressed_keys[K_a] or self.puisleft == True) and self.x > (SIZE/2) : #往左撲
                self.puisleft = True
                self.x -= 40
            elif self.rect.right < pillar_rect.left and self.puisleft == False: #往右撲
                self.x += 40

            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.2 * neg
                self.jumpCount -= 1
            else:
                self.puisleft = False
                self.ispu = False
                self.jumpCount = 10
            
    def draw(self, switch_pikal):
        #print(self.pos)
        if self.ispu:
            if self.jumpCount <= 10 and self.jumpCount >= 0:
                self.switch_pikapu = 0
            if self.jumpCount <= 0 and self.jumpCount >= -7:
                self.switch_pikapu = 1
            if self.jumpCount <= -7 and self.jumpCount >= -10:
                self.switch_pikapu = 2
                
            if self.puisleft:
                pikapuL = [pikapuL1_img, pikapuL2_img, pikapuL3_img]
                surf.blit(pikapuL[self.switch_pikapu], (self.x, self.y))
                self.img = pikapuL[self.switch_pikapu]
            else:
                pikapuR = [pikapuR1_img, pikapuR2_img, pikapuR3_img]
                surf.blit(pikapuR[self.switch_pikapu], (self.x, self.y))
                self.img = pikapuR[self.switch_pikapu]
        else:
            pikals = [pikal_img, pikal2_img, pikal3_img, pikal4_img, pikal5_img]
            surf.blit(pikals[switch_pikal], (self.x, self.y))
            self.img = pikals[switch_pikal]
            switch_pikal += 1
        return switch_pikal

    def jump(self, left_score, right_score):
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                if left_score >= SCORE//1.3: # 7/10分時跳超高
                    self.y -= (self.jumpCount ** 2) * 0.8 * neg
                else:
                    self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10
            '''
            if self.v == 0:
                F = ( 0.5 * self.m * (self.v*self.v) )
            else:
                F = -( 0.5 * self.m * (self.v*self.v) )
    
            # Change position
            self.y = self.y - F

            # Change velocity
            self.v = self.v - 1

            # If ground is reached, reset variables.
            if self.y == pikal_rect[1]:
                self.y = pikal_rect[1]
                self.isJump = 0
                self.v = 8
            '''
    def update(self): #rect_update
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)

class Pikar():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.puisleft = True
        self.ispu = False
        self.switch_pikapu = 0
        self.isJump = False
        self.jumpCount = 10
        self.img = pikal_img
        self.rect = self.img.get_rect()

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.x > pillar_rect.right:
            self.x -= 5
        if pressed_keys[K_RIGHT] and (self.x+self.rect.width) < WIDTH-SIZE/2:
            self.x += 5

    def pu(self):
        if self.ispu:
            pressed_keys = pygame.key.get_pressed()
            if self.rect.right < WIDTH-SIZE/2 and (pressed_keys[K_RIGHT] or self.puisleft == False): #往右撲
                self.puisleft = False
                self.x += 2
            elif self.puisleft == True and self.x > pillar_rect.right : #往左撲
                self.x -= 2

            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.1 * neg
                self.jumpCount -= 1
            else:
                self.puisleft = True
                self.ispu = False
                self.jumpCount = 10

    def draw(self):
        if self.ispu:
            if self.jumpCount <= 10 and self.jumpCount >= 0:
                self.switch_pikapu = 0
            if self.jumpCount <= 0 and self.jumpCount >= -7:
                self.switch_pikapu = 1
            if self.jumpCount <= -7 and self.jumpCount >= -10:
                self.switch_pikapu = 2
                
            if self.puisleft:
                pikapuL = [pikapuL1_img, pikapuL2_img, pikapuL3_img]
                surf.blit(pikapuL[self.switch_pikapu], (self.x, self.y))
                self.img = pikapuL[self.switch_pikapu]
            else:
                pikapuR = [pikapuR1_img, pikapuR2_img, pikapuR3_img]
                surf.blit(pikapuR[self.switch_pikapu], (self.x, self.y))
                self.img = pikapuR[self.switch_pikapu]
        else:
            surf.blit(pikar_img, (self.x, self.y))
            self.img = pikar_img

    def jump(self, left_score, right_score):
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                if right_score >= SCORE//1.2:  # 7/10分時跳超高
                    self.y -= (self.jumpCount ** 2) * 0.8 * neg
                else:
                    self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

    def update(self):   #rect_update
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)

def collision(rect1, rect2):
    if pygame.Rect.colliderect(rect1, rect2):
        return True
    return False

def who_goes_first():
    # Randomly choose which player goes first.
    if random.randint(0, 1) == 0:
        return 'left_first'
    else:
        return 'right_first'

def infinity(cloud_img):
    pxa = pygame.PixelArray(cloud_img)
    temp = pxa[-1,:]
    pxa[1:106,:] = pxa[0:105,:]
    pxa[0,:] = temp
    del pxa

def background(left_score, right_score, move_right):
    
    surf.blit(bg_img, (0,0))
    
    for i in range(0,WIDTH,SIZE):   #line
        if i == 0:
            surf.blit(line1_img, (i, HEIGHT-SIZE*3))
        elif i == WIDTH-SIZE:
            surf.blit(line3_img, (i, HEIGHT-SIZE*3))
        else:
            surf.blit(line2_img, (i, HEIGHT-SIZE*3))
            
    for i in range(0,WIDTH,SIZE):   #ground
        surf.blit(ground_red_img, (i,HEIGHT-SIZE*4))
        surf.blit(ground_img, (i,HEIGHT-SIZE*2))
        surf.blit(ground_img, (i,HEIGHT-SIZE))

    surf.blit(p_org, (WIDTH/2-75, 350)) #control key

    if left_score >= SCORE//2 or right_score >= SCORE//2: #移動球桿
        if pillar_rect.centerx < WIDTH/3 or move_right == True:
            move_right = True
            pillar_rect.x += 1
            pillar_head_rect.x += 1
            if pillar_rect.centerx > WIDTH*(2/3):
                move_right = False
        if pillar_rect.centerx > WIDTH*(2/3) or move_right == False:
            move_right = False
            pillar_rect.x -= 1
            pillar_head_rect.x -= 1
            if pillar_rect.centerx < WIDTH/3:
                move_right = True
    else:
        pillar_rect.bottom = HEIGHT-SIZE*2
        pillar_rect.centerx = WIDTH/2
        pillar_head_rect.bottom = pillar_rect.top
        pillar_head_rect.centerx = pillar_rect.centerx
    
    surf.blit(pillar_img, pillar_rect)
    surf.blit(pillar_head_img, pillar_head_rect)

    return move_right


def score(left_score, right_score):
    if ball_rect.bottom >= ground_line:
        if ball_rect.right <= pillar_rect.left:
            right_score += 1
        if ball_rect.left >= pillar_rect.right:
            left_score += 1

    score_img = [zero_img, one_img, two_img,
                 three_img, four_img, five_img,
                 six_img, seven_img, eight_img,
                 nine_img, ten_img]
    
    score_rect = score_img[left_score].get_rect()
    score_rect.top = 20
    score_rect.right = 96
    surf.blit(score_img[left_score], score_rect)
    score_rect = score_img[right_score].get_rect()
    score_rect.top = 20
    score_rect.right = WIDTH-32
    surf.blit(score_img[right_score], score_rect)

    return left_score, right_score

def ready(cloud, switch_pikal, pikal, pikar, ball, left_score, right_score, move_right):
    for height in range(60, 24, -1):    #ready
        move_right = background(left_score, right_score, move_right)
        cloud.move()
        cloud.update()
        cloud.draw()
        switch_pikal %= 5
        switch_pikal = pikal.draw(switch_pikal)
        pikar.draw()
        ball.draw()
        base.blit(surf, (0,0))
        ready_img = pygame.transform.scale(ready_org, (height*4, height))
        ready_rect = ready_img.get_rect()
        ready_rect.center = (WIDTH/2, HEIGHT/4)
        surf.blit(ready_img, ready_rect)
        base.blit(surf, (0,0))
        pygame.display.update()
        time.sleep(0.03)

def game_over(left_score, right_score, ball, pikal, pikar, cloud, switch_pikal, over, move_right):
    over = True
    for height in range(100):
        time.sleep(0.03)
        over_img = pygame.transform.scale(over_org, (height*4, height))
        over_rect = over_img.get_rect()
        over_rect.center = (WIDTH/2, HEIGHT/3)
        ball.move(cloud, pikal, pikar, switch_pikal, over, left_score, right_score, move_right)
        ball.draw()
        switch_pikal %= 5
        switch_pikal = pikal.draw(switch_pikal)
        pikar.draw()
        surf.blit(over_img, over_rect)
        base.blit(surf, (0,0))
        pygame.display.update()
    #cloud_move = -106
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        
        #cloud_move = background(cloud_move)
        ball.move(cloud, pikal, pikar, switch_pikal, over, left_score, right_score, move_right)
        ball.draw()
        switch_pikal %= 5
        switch_pikal = pikal.draw(switch_pikal)
        pikar.draw()
        surf.blit(pillar_head_img, pillar_head_rect)
        surf.blit(pillar_img, pillar_rect)
        surf.blit(over_img, over_rect)
        restart_rect.center = (over_rect.centerx, over_rect.bottom+20)
        surf.blit(restart_img, restart_rect)
        
        '''
        if left_score == 5:
            surf.blit(pikawin_img, pikal_rect)
            surf.blit(pikalose_img, pikar_rect)
        if right_score == 5:
            surf.blit(pikawin_img, pikar_rect)
            surf.blit(pikalose_img, pikal_rect)
        '''
        clock = pygame.time.Clock()
        clock.tick(100)
        base.blit(surf, (0,0))
        pygame.display.update()

def init():
    pikal_rect.bottom = ground_line
    pikal_rect.left = SIZE/2
    pikal = Pikal(pikal_rect[0], pikal_rect[1])

    pikar_rect.bottom = ground_line
    pikar_rect.right = WIDTH - SIZE/2
    pikar = Pikar(pikar_rect[0], pikar_rect[1])
    
    ball = Ball(pikal.rect.left, 10, 1, 0)

    left_score = 0
    right_score = 0

    over = False
    
    return pikal, pikar, ball, left_score, right_score, over

def fade_in(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        #ball = set_round()
        base.blit(fade, (0,0))
        pygame.display.update()
        #pygame.time.delay(3)

def fade_out(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0,300):
        fade.set_alpha(255-alpha)
        #ball = set_round()
        base.blit(fade, (0,0))
        pygame.display.update()
        #pygame.time.delay(3)


def pause():
    for i in range(HEIGHT-SIZE, 0-SIZE*2, -SIZE):
        for j in range(0,WIDTH, SIZE):
            surf.blit(sea1_img, (j,i))
            surf.blit(sea_img, (j,i+SIZE))
        time.sleep(0.04)
        base.blit(surf, (0,0))
        pygame.display.update()

    surf.blit(control_img, (0,0))
    surf.blit(pillar_img, pillar_rect)
    surf.blit(pillar_head_img, pillar_head_rect)
    base.blit(surf, (0,0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    return
        

def run():
    pikal, pikar, ball, left_score, right_score, over = init()
    cloud = Cloud(-106, 20)
    switch_pikal = 0
    in_point = False
    move_right = True
    while True: #each round
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: #左皮卡[左]
                    pass
                if event.key == pygame.K_d: #左皮卡[右]
                    pass
                if event.key == pygame.K_w: #左皮卡[上]
                    if not pikal.ispu:
                        pikal.isJump = True
                if event.key == pygame.K_s: #左皮卡[下]
                    pass
                if event.key == pygame.K_z: #左皮卡[撲街&還沒寫的殺球]
                    if not pikal.isJump:
                        pikal.ispu = True
                if event.key == pygame.K_LEFT:  #右皮卡[左]
                    pass
                if event.key == pygame.K_RIGHT: #右皮卡[左]
                    pass
                if event.key == pygame.K_UP:    #右皮卡[左]
                    if not pikar.ispu:
                        pikar.isJump = True
                if event.key == pygame.K_DOWN:  #右皮卡[左]
                    pass
                if event.key == pygame.K_RETURN:#(enter key) #右皮卡[撲街&還沒寫的殺球]
                    if not pikar.isJump:
                        pikar.ispu = True
                if event.key == pygame.K_SPACE:
                    pikal, pikar, ball, left_score, right_score, over = init()
                if event.key == pygame.K_p:
                    pause()
                    
        if in_point == False:
            ready(cloud, switch_pikal, pikal, pikar, ball, left_score, right_score, move_right)
            in_point = True

        move_right = background(left_score, right_score, move_right)

        cloud.update()
        cloud.move()
        cloud.draw()
        
        pikal.move()
        switch_pikal %= 5
        switch_pikal = pikal.draw(switch_pikal)
        pikal.jump(left_score, right_score)
        pikal.pu()
        pikal.update()
        
        pikar.move()
        pikar.draw()
        pikar.jump(left_score, right_score)
        pikar.pu()
        pikar.update()

        ball.move(cloud, pikal, pikar, switch_pikal, over, left_score, right_score, move_right)
        ball.draw()

        #GAME OVER
        left_score, right_score = score(left_score, right_score)
        if left_score == SCORE or right_score == SCORE:
            over = game_over(left_score, right_score, ball, pikal, pikar, cloud, switch_pikal, over, move_right)
            pikal, pikar, ball, left_score, right_score, over = init()
        
        base.blit(surf, (0,0))
        clock = pygame.time.Clock()
        clock.tick(60)
        pygame.display.update()

        #一分結束
        if ball_rect.bottom >= ground_line:
            in_point = False

            #判定一這球左右輸贏
            if ball_rect.centerx <= pillar_rect.centerx:
                win_point = "left"
            if ball_rect.centerx >= pillar_rect.centerx:
                win_point = "right"

            for i in range(30): #如果要修下一局球在中間的bug要在這之前先判定左贏還右贏
                clock.tick(30)
                ball.move(cloud, pikal, pikar, switch_pikal, over, left_score, right_score, move_right)
                ball.draw()
                base.blit(surf, (0,0))
                pygame.display.update()
            
            #fade_in(WIDTH,HEIGHT)

            #下一球開始 重設畫面
            pikal_rect.bottom = ground_line
            pikal_rect.left = SIZE/2
            pikal = Pikal(pikal_rect[0], pikal_rect[1])
            pikar_rect.bottom = ground_line
            pikar_rect.right = WIDTH - SIZE/2
            pikar = Pikar(pikar_rect[0], pikar_rect[1])
            if win_point == "left":
                ball = Ball(pikal_rect.left, 10, 0, 0)
            else:
                ball = Ball(pikar_rect.left, 10, 0, 0)

            move_right = background(left_score, right_score, move_right)
            cloud.move()
            cloud.update()
            cloud.draw()
            switch_pikal %= 5
            switch_pikal = pikal.draw(switch_pikal)
            pikar.draw()
            ball.draw()
            base.blit(surf, (0,0))
            pygame.display.update()
            
            #fade_out(WIDTH,HEIGHT)

SCORE = 10
run()
