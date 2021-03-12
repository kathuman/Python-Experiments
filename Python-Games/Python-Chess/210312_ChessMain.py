"""
This file will 
1.- contain the main drive file.
2.- Handle player input
3.- display the current gameplay object
"""
import pygame as p
from Python-Chess import 210312_ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

'''
Initialize a global dictionary of images. This will be called exactly once in main
'''

def loadImages():
    pieces = ['wp','wR','wN','wB','wQ','wK','bp','bR','bN','bB','bQ','bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(piece+"png"), (SQ_SIZE, SQ_SIZE))
    # note that we can access a piece by saying IMAGES['wp'] for example

'''
This will be our main driver
1.- handle user imput
2.- Update the graphics
'''

def main():
    p.init()
    screen = p.display.sel_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.color("white"))