# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 18:22:03 2021

@author: Yassine
"""
import pygame
class Node:
    def __init__(self, x, y, prio, name, parent, dis):
        self.x = x
        self.y = y
        self.prio = prio
        self.name = name
        self.color = (32,138,174)
        self.width = 95
        self.height = 25
        self.s = pygame.Surface((self.width, self.height))
        self.font_style = pygame.font.SysFont('arial', 19)
        self.parent = parent
        if self.parent != None:
            pygame.draw.line(dis, (96, 73, 44), (self.x + 47, self.y), (self.parent.x + 47, self.parent.y + 25))
        self.dis = dis
        
        
    def display(self):
        self.s.fill(self.color)
        
        msg = self.font_style.render(str(self.prio) + '| ' + self.name, False, (96, 73, 44))
        text_rect = msg.get_rect(center=(self.width/2, self.height/2))
        self.s.blit(msg, text_rect)
        
        self.dis.blit(self.s,(self.x, self.y))
        pygame.display.update()
        
    def destroy(self):
        self.s.fill((249,235,224))
        self.dis.blit(self.s,(self.x, self.y))
        if self.parent != None:
            pygame.draw.line(self.dis, (249,235,224), (self.x + 47, self.y), (self.parent.x + 47, self.parent.y + 25))
        pygame.display.update()
        
    def select(self):
        self.color = (13, 33, 73)
        self.display()
    
    def unselect(self):
        self.color = (32,138,174)
        self.display()
        