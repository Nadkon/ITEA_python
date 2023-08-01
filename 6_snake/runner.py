import pygame

from constants import WIDTH, HEIGHT
from snake import Snake
from apple import Apple

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # задаємо розмір екрaну
pygame.display.set_caption('Snake') # даємо назву вікну, де буде гра
clock = pygame.time.Clock()   # створюємо обєкт годинника
running = True

snake = Snake(100,100)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.move(pygame.K_UP)
            if event.key == pygame.K_DOWN:
                snake.move(pygame.K_DOWN)
            if event.key == pygame.K_RIGHT:
                snake.move(pygame.K_RIGHT)
            if event.key == pygame.K_LEFT:
                snake.move(pygame.K_LEFT)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill('purple')

    snake.draw(screen)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip() # це очищення екрану

    clock.tick(60)  #limits FPS to 60

pygame.quit()

