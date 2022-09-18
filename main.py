import pygame
import shapes

class Tetris():
    def __init__(self):
        # initial
        self.isStarted = False
    def tetrisUI(self):
        # initial UI
        self.fps = 200
    
    def start(self):
        if self.isStarted:
            return
        self.isStarted = True

    def pause(self):
        if not self.isStarted:
            return
    
    def keyPressed(self, event):
        key = event.key()
        # pause
        if key == pygame.K_p:
            self.pause()
            return
        # up
        # down
        # left
        # right

        else:
            return