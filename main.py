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

dis_width = 1700
dis_height = 350

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
                nums = [i.prio for i in queue.l]
                new_num = random.randint(0,50)
                while new_num in nums:
                    new_num = random.randint(0,50)
                queue.add((new_num, random.choice(NAMES)))
            elif event.button == 3:
                queue.pop()
pygame.quit()