import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
  rows = 20
  w = 500
  def _init_(self,start,dirnx=1,dirny=0,color=(0, 255, 50 )):
    pass
  def move(self, dirnx, dirny):
    pass
  def draw(self, surface, eyes=False):
    pass

class snake(object):
  def _init_(self, color, position):
    pass
  def move (self):
    pass
  def reset(self, pos):
    pass
  def addCube(self):
    pass
  def draw(self, surface):
    pass

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
  print("HI")
  global width, rows
  width = 500
  rows = 20
  win = pygame.display.set_mode((width, width))
 # s = snake((44, 69, 88 ), (10,10))
  s = snake((255,0,0),(10,10))
  flag = True

  clock = pygame.time.Clock()
  while flag:
    pygame.time.delay(50)
    clock.tick(10)
    redrawWindow(win)
  pass 


main()
print("END")
