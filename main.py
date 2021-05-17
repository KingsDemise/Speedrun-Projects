import pygame
from pygame import mixer
import random
import math
pygame.init()

screen=pygame.display.set_mode((800,600))
bg=pygame.image.load('3d-hyperspace-background-with-warp-tunnel-effect.jpg')
pygame.display.set_caption("Space Invaders x Among Us")
icon=pygame.image.load('iconfinder_among-us-player-white_7033730.png')
pygame.display.set_icon(icon)

mixer.music.load("Spiral (320 kbps).mp3")
mixer.music.play(-1)

playerImg=pygame.image.load('1-1.png')
playerX=370
playerY=480
playerX_change=0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.1)
    enemyY_change.append(40)

bulletImg=pygame.image.load('bullet.png')
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=2
bullet_state="ready"

score_value=0
font=pygame.font.SysFont('Simple', 32)

X=10
Y=10

over_font = pygame.font.SysFont('Nexa Bold', 64)

def show_score(x, y):
    score=font.render("Score : " + str(score_value),True,(0,0,255))
    screen.blit(score, (x, y))
def instructions():
    ins=font.render("D/RIGHT ARROW to go right. A/LEFT ARROW to go left. SPACE to fire",True,(255,255,255))
    screen.blit(ins, (10,28))
def game_over_text():
    over_text = over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text, (250, 300))

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

running=True
while running:
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-0.25
            if event.key==pygame.K_a:
                playerX_change=-0.25
            if event.key==pygame.K_RIGHT:
                playerX_change = 0.25
            if event.key==pygame.K_d:
                playerX_change = 0.25
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_a:
                playerX_change = 0

    playerX+=playerX_change
    if playerX<=0:
        playerX=0
    if playerX>736:
        playerX=736

    for i in range(num_of_enemies):
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i]=0.1
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i]=-0.1
            enemyY[i]+=enemyY_change[i]
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound=mixer.Sound("stationary-kill_gDwMUvN.mp3")
            explosionSound.play()
            bulletY=480
            bullet_state="ready"
            score_value+=1
            enemyX[i]=random.randint(0,736)
            enemyY[i]=random.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)

    if bulletY<=0:
        bulletY=480
        bullet_state="ready"
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change

    player(playerX,playerY)
    show_score(X,Y)
    instructions()
    pygame.display.update()