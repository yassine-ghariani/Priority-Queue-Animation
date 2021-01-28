# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pygame
from NAMES import NAMES
from PrioQueue import PrioQueue
import random

pygame.init()

dis_width = 900
dis_height = 900

dis = pygame.display.set_mode((dis_width, dis_height))
dis.fill((249,235,224))
pygame.display.update()
queue = PrioQueue(dis)

anim_over = False

while not anim_over:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            anim_over = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                queue.add((random.randint(0, 50), random.choice(NAMES)))
            elif event.button == 3:
                queue.pop()
pygame.quit()