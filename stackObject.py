import pygame as pg 
import os

class StackObject:

    def __init__(self, game, position) -> None:
        self.game = game
        self.objectImages = [pg.image.load('car/' + img) for img in os.listdir('car')]
        self.position = position
        self.objectSurface = pg.Surface((100,100))
        self.spread = 1

    def render(self):
        self.objectSurface.fill("black")

        for index, img in enumerate(self.objectImages):

            rotated_image = pg.transform.rotate(img, self.game.rotation)
            
            self.objectSurface.blit(rotated_image, (self.position[0] - rotated_image.get_width() // 2, self.position[1] - rotated_image.get_height() // 2 - index* self.spread))

        self.game.screen.blit(pg.transform.scale(self.objectSurface, self.game.screen.get_size()),(0,0))

        