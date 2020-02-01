import math
import random
import tinker as tk
from tinker import messagebox

class cube(object):
  rows = 0
  w = 0
  def _init_(self,start,dnrx=1,dnry=0,color=(0, 255, 50 )):
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
  pass

def redrawWindow(surface):
  pass

def randomSnack(rows, items):
  pass
def main():
  width = 500
  height =  500
  rows = 20
  win = pygame.display.set_mode((width, height))
  pass