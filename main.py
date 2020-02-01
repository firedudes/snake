import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
  rows = 0
  w = 0
  def _init_(self,start,dirnx=1,dirny=0,color=(0, 255, 50 )):
    pass

  def move(self, dirnx, dnry) :
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
  pa

def redrawWindow(surface):
  global rows, width
  win.fill((44, 88, 78 ))
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
  s = snake ((44, 69, 88 ), (10,10))
  flag = true

  clock = pygame.time.Clock()
  while flag:
    pygame.time.delay(50)
    clock.tick(10)

    redrawWindow(win)
  pass 


  main()