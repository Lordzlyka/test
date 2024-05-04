import pygame
import random
import pymunk
from random import *
from pygame import *
from pymunk import *
class slot():
    def __init__(self, slot_image, slot_x, slot_y, size_x, size_y):
        self.image = transform.skale(image.load(slot_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = slot_x
        self.rect.y = slot_y
    def reset(self):
        window.blit(self.image, (self.rect.x))

win_width = 500
win_heidht = 500
display.set_caption('slot machine')
window = display.set_mode((win_width, win_heidht))
fon = pygame.image.load('fon_casino.jpg').convert()


run = True
while run:
    window.blit(fon, (0, 0))
    for i in event.get():
        if i.type == QUIT:
            run = False
    display.update()




