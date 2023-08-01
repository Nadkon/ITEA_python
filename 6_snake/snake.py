import pygame as pg
from constants import SQUARE_HEIGHT, SQUARE_WIDTH

class Snake:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.head = pg.Rect(x, y, SQUARE_WIDTH, SQUARE_HEIGHT)

    def draw(self, screen):
        pg.draw.rect(screen, 'green', self.head)