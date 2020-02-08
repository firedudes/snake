import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
  rows = 20
  w = 500
  def _init_(self,start,dirnx=1,dirny=0,color=(0, 255, 50 )):
    self.pos = start
    self.dirnx = 1
    self.dirny = 0 
    self.color = color 
  def move(self, dirnx, dirny):
    self.dirnx = dirnx
    self.dirny = dirny
    self.pos(self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
  def draw(self, surface, eyes=False):
    dis = self.w // self.rows
    i = self.pos[0]
    j =  self.pos[1]
    pygame.draw.rect(surface, self.color (i*dis+1,j*dis+1, dis-2, dis-2))
class snake(object):
  body = []
  turns = {}

  def _init_(self, color, pos):
    self.color = color
    self.head = cube(pos)
    self.apped.append(self.head)
    self = dirnx = 0
    self = dirny = 1
  def move (self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

    keys = pygame.key.get.pressed()

    for keys in keys:
        if keys[pygame.K_LEFT]:
            self.dirnx = -1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        elif keys[pygame.K_RIGHT]:
            self.dirnx = 1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        elif keys[pygame.K_UP]:
            self.dirnx = 0
            self.dirny = -1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        elif keys[pygame.K_DOWN]:
            self.dirnx = 0
            self.dirny = 1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

    for i, c in enumerate(self.body):
        p = c.pos[:]
        if p in self.turns:
            turn = self.turns[p]
            c.move(turn[0], turn[1])
            if i == len(self.body)-1 :
                self.turns.pop(p)
        else:
          if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
          elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
          elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
          elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
          else: c.move(c.dirnx,c.dirny)
       

  def reset(self, pos):
    pass
  def addCube(self):
    pass
  def draw(self, surface):
      for i, c in enumerate(self.body):
        if i ==0:
            c.draw(surface, True)
        else:
            c.draw(surface)

def drawGrid(w, rows, surface):
  sizeBtwn = w // rows

  x = 0
  y = 0
  for l in range(rows):
    x = x + sizeBtwn
    y = y + sizeBtwn
    pygame.draw.line(surface, (255,255,255), (x,0), (x,w))
    pygame.draw.line(surface, (255,255,255), (0,y), (w,y))

def redrawWindow(surface):
  global rows, width
  surface.fill((44, 88, 78 ))
  drawGrid(width, rows, surface)
  pygame.display.update()

def randomSnack(rows, items):
  pass

def messagebox(subject, content):
  pass

def main():
  global width, rows
  width = 500
  rows = 20
  win = pygame.display.set_mode((width, width))
 # s = snake((44, 69, 88 ), (10,10))
  #s = snake((255,0,0),(10,10))
  flag = True

  clock = pygame.time.Clock()
  while flag:
    pygame.time.delay(50)
    clock.tick(10)
    redrawWindow(win)
  pass 


main()
print("END")
