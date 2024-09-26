import pygame as pg 
from stackObject import StackObject


class Game:

    def __init__(self) -> None:
        
        self.screen = pg.display.set_mode((500, 500))
        self.clock = pg.time.Clock()
        self.rotation = 0
    
    def run(self):
        
        car = StackObject(self,(50,50))

        running = True

        while running:

            for event in pg.event.get():

                if event.type == pg.QUIT:
                    
                    running = False

            self.screen.fill('black')
            car.render()

            self.rotation = (self.rotation + 1)%1000

            pg.display.update()

            self.clock.tick(60)
        
        pg.quit()


game = Game()

game.run()

            
            
                    
            
