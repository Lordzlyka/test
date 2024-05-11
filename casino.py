import pygame
import random
import pymunk
from random import *
from pygame import *
from pymunk import *
class slot():
    def __init__(self, slot_image, slot_x, slot_y, size_x, size_y):
        self.player_image=slot_image
        self.image = transform.scale(image.load(self.player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = slot_x
        self.rect.y = slot_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

win_width = 500
win_heidht = 500
display.set_caption('slot machine')
window = display.set_mode((win_width, win_heidht))
fon = pygame.image.load('poker_fon.jpg').convert()
slot1 = 0
slot2 = 0
slot3 = 0
slot_machine = slot('slot_machine.png',50,100,400,300)
def print_slots():
    random()
    slot1 = slot(slot1, 150, 150, 50, 50)
    slot2 = slot(slot2, 200, 150, 50, 50)
    slot3 = slot(slot3, 250, 150, 50, 50)
    if slot1 == slot2 and slot2 == slot3:
        print(win)
        #вызвать функцию монеток
    
def random():
    random_slot1 = randint(1, 4)
    if random_slot1 == 1:
        slot1 = 'apple.png'
    elif random_slot1 == 2:
        slot1 = 'limon.png'
    elif random_slot1 == 3:
        slot1 = 'persik.png'
    else:
        slot1 = 'zemlyanika.png'

    random_slot2also = randint(1, 8)
    random_slot2 = randint(1, 4)
    if random_slot2 == 1:
        slot2 = 'apple.png'
    elif random_slot2 == 2:
        slot2 = 'limon.png'
    elif random_slot2 == 3:
        slot2 = 'persik.png'
    else:
        slot2 = 'zemlyanika.png'
    if slot1 == slot2 and random_slot2also < 3:
        slot2 == slot1

    random_slot3also = randint(1, 16)
    random_slot3 = randint(1, 4)
    if random_slot3 == 1:
        slot3 = 'apple.png'
    elif random_slot3 == 2:
        slot3 = 'limon.png'
    elif random_slot3 == 3:
        slot3 = 'persik.png'
    else:
        slot3 = 'zemlyanika.png'
    if slot2 == slot3 and random_slot3also < 5:
        slot3 = slot2
    print(slot1)
    print(slot2)
    print(slot3)
    
    
run = True
while run:
    print_slots()
    window.blit(fon, (0, 0))
    slot_machine.reset()
    for i in event.get():
        if i.type == QUIT:
            run = False
    display.update()





