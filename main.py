from random import randint
import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Window
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption('PONG GAME')

# Paddle A
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 350
# Paddle B
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 970
paddleB.rect.y = 350
# Ball
ball = Ball(WHITE, 15, 15)
ball.rect.x = 495
ball.rect.y = 380

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

carryOn = True
# Stop = False
score_time = 0
clock = pygame.time.Clock()

# Score
scoreA = 0
scoreB = 0
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # Pressing the q Key will quit the game
                carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddleB.moveUp(8)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(8)

    # adding AI to paddleA
    if ball.rect.x <= 499:
        if (paddleA.rect.y - ball.rect.y) <= 0:
            paddleA.moveDown(8)
        if (paddleA.rect.y - ball.rect.y) >= 0:
            paddleA.moveUp(8)
    else:
        if (paddleA.rect.y - 370) <= 0:
            paddleA.moveDown(5)
        else:
            paddleA.moveUp(5)

    # --- Game logic should go here
    all_sprites_list.update()

    # --- ball bouncing against 4 walls
    if ball.rect.x >= 970:
        score_time = pygame.time.get_ticks()
        print(score_time)
        # Stop = True
        scoreA += 1
        ball.rect.x = 495
        ball.rect.y = 380
        ball.velocity = [randint(4,8),randint(-2,2)]

        paddleA.rect.x = 20
        paddleA.rect.y = 350
        paddleB.rect.x = 970
        paddleB.rect.y = 350
    if ball.rect.x <= 20:
        score_time = pygame.time.get_ticks()
        print(score_time)
        # Stop = True
        scoreB += 1
        ball.rect.x = 345
        ball.rect.y = 195
        ball.velocity = [randint(4,8), randint(-2,2)]

        paddleA.rect.x = 20
        paddleA.rect.y = 350
        paddleB.rect.x = 970
        paddleB.rect.y = 350
    if ball.rect.y >= 790:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y <= 0:
        ball.velocity[1] = -ball.velocity[1]



    # --- Collision
    if pygame.sprite.collide_mask(ball,paddleA) or pygame.sprite.collide_mask(ball,paddleB):
        ball.bounce()

    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [499, 0], [499, 800], 5)


    all_sprites_list.draw(screen)

    # Display Score:
    font = pygame.font.Font(None, 70)
    text1 = font.render(str(scoreA), True, WHITE)
    screen.blit(text1, (350, 50))
    text2 = font.render(str(scoreB), True, WHITE)
    screen.blit(text2, (650, 50))


    if scoreA == 5 or scoreB == 5 :
        carryOn = False

    pygame.display.flip()

    clock.tick(60)


pygame.quit()

