from pygame.locals import QUIT
import sys
import os
import pygame as pg

from GObject.Sheep import Sheep
from GObject.Wolf import Wolf
from GObject.Cabbage import Cabbage
from GObject.Boat import Boat

# Set Window Position
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 270)

# Start Game Window
pg.init()
width = 1024
height = 768
screen = pg.display.set_mode((width, height))
pg.display.set_caption('Wolf & Sheep & Cabbage')


class Game:

    def __init__(self):
        self.fps = 30
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 20)

        self.done = False

        self.OnBoat = None
        self.BoatCrossed = False
        self.Crossed = set()
        self.NotCrossed = set()

        self.sheep = Sheep(100, 250)
        self.sheep.setPos((300 - self.sheep.width - 10,
                           height - self.sheep.height - 100))

        self.cabbage = Cabbage(100, 250)
        self.cabbage.setPos(
            (self.sheep.x - self.cabbage.width - 10, height - self.cabbage.height - 100))

        self.wolf = Wolf(100, 250)
        self.wolf.setPos(
            (self.cabbage.x - self.wolf.width - 10, height - self.wolf.height - 100))

        self.boat = Boat(100, 250)
        self.boat.setPos((300, height - self.boat.height - 50))

        self.background = pg.image.load('media/background.png')
        self.background = pg.transform.scale(
            self.background, (width, height)).convert()

        self.ground = pg.image.load('media/ground.png')
        self.ground = pg.transform.scale(self.ground, (width, (int)(
            self.ground.get_height() * (width / self.ground.get_width())))).convert_alpha()

        self.NotCrossed = {self.sheep, self.cabbage, self.wolf}

    def run(self):
        while not self.done:
            self.handle_events()
            self.run_logic()
            self.draw()
            self.clock.tick(self.fps)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.boat.wasClicked(event):

                        # Boat Cross River
                        if self.BoatCrossed:
                            self.boat.setPos(
                                (300, self.boat.y))
                        else:
                            self.boat.setPos(
                                (width - 300 - self.boat.width, self.boat.y))
                        self.BoatCrossed = not self.BoatCrossed

                        # Move Object On Boat
                        if not self.OnBoat == None:
                            self.OnBoat.setPos(
                                (self.boat.x + 60, self.boat.y - 30))

                    else:
                        if self.sheep.wasClicked(event):
                            if self.OnBoat == None:
                                self.sheep.setPos(
                                    (self.boat.x + 60, self.boat.y - 30))
                                self.OnBoat = self.sheep
                            elif self.OnBoat == self.sheep:
                                if not self.BoatCrossed:
                                    self.sheep.setPos((300 - self.sheep.width - 10,
                                                       height - self.sheep.height - 100))
                                else:
                                    self.sheep.setPos((width - 300,
                                                       height - self.sheep.height - 100))
                                self.OnBoat = None

    def run_logic(self):
        pass

    def draw(self):
        # Fill Background
        screen.fill((255, 255, 255))
        screen.blit(self.background, self.background.get_rect())
        screen.blit(self.ground, (0, height - self.ground.get_height()))
        # Draw title
        head_font = pg.font.SysFont(None, 16)
        text_surface = head_font.render(
            'wolf & sheep & cabbage [FPS: {0:.2f}]'.format(self.clock.get_fps()), True, (0, 0, 0))
        screen.blit(text_surface, (10, 10))

        # Draw Info
        Info = '''
[DEBUG]\n
OnBoat:{0}\n
Crossed:{1}\n
NotCrossed:{2}\n
'''.format(
            self.OnBoat,
            self.Crossed,
            self.NotCrossed)
        inf_index = 0
        for txt in Info.split('\n'):
            text_surface = head_font.render(
                txt, True, (0, 0, 0))
            screen.blit(text_surface, (10, 23 + (7 * inf_index)))
            inf_index += 1

        # Draw Sheep
        screen.blit(self.sheep.image, self.sheep.rect)
        # Draw Wolf
        screen.blit(self.wolf.image, self.wolf.rect)
        # Draw Cabbage
        screen.blit(self.cabbage.image, self.cabbage.rect)
        # Draw Boat
        screen.blit(self.boat.image, self.boat.rect)
        pg.display.flip()


if __name__ == "__main__":
    Game().run()
    pg.quit()
    sys.exit()
