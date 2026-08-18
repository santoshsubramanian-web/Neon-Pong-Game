from sys import exit
import pygame

GAME_WIDTH, GAME_HEIGHT = 800, 600
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
SPEED = 5
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 90
BALL_WIDTH, BALL_HEIGHT = 20, 20


#Rectangles
player_paddle = pygame.Rect(10, GAME_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
enemy_paddle = pygame.Rect(GAME_WIDTH - 30, GAME_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
center_line = pygame.Rect(GAME_WIDTH//2, 0, 5, 8000)
ball = pygame.Rect(GAME_WIDTH//2, GAME_HEIGHT//2, BALL_WIDTH, BALL_HEIGHT)

clock = pygame.time.Clock()

def draw():
    #Background Color (Varient of purple)
    screen.fill((15, 17, 26))

    # Drawing player paddle
    pygame.draw.rect(screen, (0, 240, 255), player_paddle)

    #Drawing Opponent Paddle
    pygame.draw.rect(screen, (255, 0, 85), enemy_paddle)

    #Drawing The center line
    pygame.draw.rect(screen, (40, 45, 62), center_line)

    #Drawing Ball(Arbitrary position for now)
    pygame.draw.rect(screen, (255, 230, 0), ball)
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # For Bouncing the ball around the screen(for now it ignores the paddles and phases through them)
    

    #Getting user inputs for changing the state of the ball(From normal bounce mode to fast bounce mode) for now i will just change the color when a key is pressed
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]):
        player_paddle.y -= SPEED
    elif (keys[pygame.K_DOWN] or keys[pygame.K_s]):
        player_paddle.y += SPEED

    #Checking for boundaries(UP)
    if player_paddle.y < 0:
        player_paddle.y = 0
    #Checking for boundaries(DOWN)
    if player_paddle.y > GAME_HEIGHT - PADDLE_HEIGHT:
        player_paddle.y = GAME_HEIGHT - PADDLE_HEIGHT

    #

    draw()
    pygame.display.update()
    clock.tick(60)