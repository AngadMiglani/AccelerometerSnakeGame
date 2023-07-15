import pygame
pygame.init()

width = 600
height = 350
screen = pygame.display.set_mode((width, height))
background = (0, 200, 0)
food_colour = (200, 0, 0)
snake_colour = (0, 0, 200)
snake_length = 30
snake_width = 30
snakeX = 500
snakeY = 300
FPS = 25
shift = 10
direction = 0
fpsClock = pygame.time.Clock()
game_over = False
while not game_over:
    screen.fill(background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 1
            if event.key == pygame.K_RIGHT:
                direction = 2
            if event.key == pygame.K_UP:
                direction = 3
            if event.key == pygame.K_DOWN:
                direction = 4
    if direction == 1:
        snakeX = snakeX - shift
    if direction == 2:
        snakeX = snakeX + shift
    if direction == 3:
        snakeY = snakeY - shift
    if direction == 4:
        snakeY = snakeY + shift
    pygame.draw.circle(screen, food_colour, (400, 300), 10)
    pygame.draw.rect(screen, snake_colour, [snakeX, snakeY, snake_length, snake_width])
    pygame.display.update()
    fpsClock.tick(FPS)
pygame.quit()
