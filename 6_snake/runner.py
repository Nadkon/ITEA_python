import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1288, 720)) # задаємо розмір екрaну
pygame.display.set_caption('Snake') # даємо назву вікну, де буде гра
clock = pygame.time.Clock()   # створюємо обєкт годинника
running = True

rect = pygame.Rect(100, 100, 100, 100)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill('purple')

    pygame.draw.rect(screen, 'red', rect)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip() # це очищення екрану

    clock.tick(60)  #limits FPS to 60

pygame.quit()

