# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 17:50:11 2021

@author: Yassine
"""
import math
from Node import Node
import time
class PrioQueue:
    def __init__(self, dis):
        self.l = []
        self.dis = dis
        self.spacing = {1 : (400, 50, 0), 2 : (200, 100, 400), 3 : (100, 150,200), 4 : (50, 200, 100)} # {level : (x, y, x_spacing)}
    
    
    def upHeap(self, noeud):
        self.l[noeud].select()
        parent = (noeud - 1) // 2
        if noeud != 0 and noeud != parent:
            time.sleep(0.5)
            self.l[parent].select()
            if self.l[parent].prio > self.l[noeud].prio:
                self.l[parent].prio, self.l[noeud].prio,self.l[parent].name, self.l[noeud].name = self.l[noeud].prio, self.l[parent].prio, self.l[noeud].name, self.l[parent].name
                time.sleep(0.5)
                self.l[noeud].unselect()
                self.l[parent].unselect()
                self.upHeap(parent)
            else:
                self.l[noeud].unselect()
                self.l[parent].unselect()
        else:
            self.l[noeud].unselect()
        
    def downHeap(self, noeud):
        if self.l != []:
            self.l[noeud].select()
            indice_depart = noeud
            enfant_droite = 2 * noeud + 1
            enfant_gauche = 2 * noeud + 2
            if enfant_droite < len(self.l) and self.l[indice_depart].prio > self.l[enfant_droite].prio:
                indice_depart = enfant_droite
            if enfant_gauche < len(self.l) and self.l[indice_depart].prio > self.l[enfant_gauche].prio:
                indice_depart = enfant_gauche
            if noeud != indice_depart:
                time.sleep(0.5)
                self.l[indice_depart].select()
                time.sleep(0.5)
                self.l[noeud].prio, self.l[indice_depart].prio,self.l[noeud].name, self.l[indice_depart].name = self.l[indice_depart].prio, self.l[noeud].prio, self.l[indice_depart].name, self.l[noeud].name
                self.l[noeud].unselect()
                self.l[indice_depart].unselect()
                self.downHeap(indice_depart)
            else:
                self.l[noeud].unselect()
    
    def add(self, element):
        if len(self.l) < 15:
            level = math.floor(math.log(len(self.l) + 1, 2)) + 1
            x_node = self.spacing[level][0] + (len(self.l) + 1 - 2**(level-1)) * self.spacing[level][2]
            if len(self.l) > 0:
                parent = self.l[(len(self.l) - 1)//2]
            else:
                parent = None
            node = Node(x_node, self.spacing[level][1], element[0], element[1],parent, self.dis)
            self.l.append(node)
            node.display()
            self.upHeap(len(self.l) - 1)
            
    def pop(self):
        if self.l != []:
            self.l[0].destroy()
            time.sleep(0.5)
            self.l[0].prio, self.l[len(self.l) -1].prio, self.l[0].name, self.l[len(self.l) -1].name= self.l[len(self.l) - 1].prio, self.l[0].prio,self.l[len(self.l) - 1].name, self.l[0].name
            self.l[0].display()
            self.l.pop().destroy()
            self.downHeap(0)
    
            