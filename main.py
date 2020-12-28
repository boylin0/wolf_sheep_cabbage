from pygame.locals import QUIT
import sys
import os
import pygame as pg

from GObject.Sheep import Sheep
from GObject.Wolf import Wolf
from GObject.Cabbage import Cabbage
from GObject.Boat import Boat
from GObject.Person import Person

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
        self.fps = 60
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 20)

        self.done = False

        self.background = pg.image.load('media/background.png')
        self.background = pg.transform.scale(
            self.background, (width, height)).convert()

        self.ground = pg.image.load('media/ground.png')
        self.ground = pg.transform.scale(self.ground, (width, (int)(
            self.ground.get_height() * (width / self.ground.get_width())))).convert_alpha()

        self.Crossed = set()
        self.NotCrossed = set()

        self.boat = Boat(0, 0)
        self.boat.setPos(
            (300, height - self.ground.get_height() - (self.boat.height * 0.5)))

        self.sheep = Sheep(0, 0)
        self.NotCrossed.add(self.sheep)
        self.sheep.setPos((self.boat.x - (70 * len(self.NotCrossed)) - 25,
                           height - self.sheep.height - 100))

        self.cabbage = Cabbage(0, 0)
        self.NotCrossed.add(self.cabbage)
        self.cabbage.setPos((self.boat.x - (70 * len(self.NotCrossed)) - 25,
                             height - self.cabbage.height - 100))

        self.wolf = Wolf(0, 0)
        self.NotCrossed.add(self.wolf)
        self.wolf.setPos((self.boat.x - (70 * len(self.NotCrossed)) - 25,
                          height - self.wolf.height - 100))

        self.person = Person(300, 300)

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
                    Click_Object = None
                    # Click Object (Order by priority)
                    if self.cabbage.wasClicked(event):
                        Click_Object = self.cabbage
                    if self.wolf.wasClicked(event):
                        Click_Object = self.wolf
                    if self.sheep.wasClicked(event):
                        Click_Object = self.sheep
                    if self.boat.wasClicked(event):
                        Click_Object = self.boat

                    if Click_Object == self.boat and self.boat.isMoving == False:
                        print('Click On Boat')
                        if self.boat.Crossed == False:
                            self.boat.move((300, 0))
                            self.boat.Crossed = True
                        else:
                            self.boat.move((-300, 0))
                            self.boat.Crossed = False

                    if self.boat.isMoving == False:
                        if (Click_Object == self.sheep
                        or Click_Object == self.cabbage
                        or Click_Object == self.wolf):

                            print('Click On {0}'.format(
                                Click_Object.__class__.__name__))

                            if self.boat.Carrying == Click_Object:
                                # Unload An Object to Crossed Side
                                if self.boat.Crossed == True:
                                    self.Crossed.add(Click_Object)
                                    Click_Object.absMove((self.boat.rect.right + 10,
                                                        height - Click_Object.height - 100))

                                # Unload An Object to Not Crossed Side
                                if self.boat.Crossed == False:
                                    Click_Object.absMove((self.boat.x - (70 * len(self.NotCrossed)) - 25,
                                                        height - Click_Object.height - 100))
                                    self.NotCrossed.add(Click_Object)

                                # Unload Object On The Boat
                                self.boat.Carrying = None

                            elif self.boat.Carrying == None:

                                # Carry A Not Crossed Object
                                if Click_Object in self.NotCrossed and self.boat.Crossed == False:
                                    Click_Object.absMove(
                                        (self.boat.x + self.boat.width - Click_Object.width - 10,
                                        self.boat.rect.bottom - Click_Object.height - 30))
                                    self.boat.Carrying = Click_Object
                                    self.NotCrossed.remove(Click_Object)

                                # Carry A Crossed Object
                                if Click_Object in self.Crossed and self.boat.Crossed == True:
                                    Click_Object.absMove(
                                        (self.boat.x + self.boat.width - Click_Object.width - 10,
                                        self.boat.rect.bottom - Click_Object.height - 30))
                                    self.boat.Carrying = Click_Object
                                    self.Crossed.remove(Click_Object)

    def run_logic(self):
        self.person.setPos(
            (self.boat.x + 20, self.boat.rect.bottom - self.person.height - 10))
        self.boat.update()
        self.sheep.update()
        self.wolf.update()
        self.cabbage.update()
        for index, item in enumerate(self.NotCrossed):
            item.absMove((300 - (70 * (index + 1)) - 25,
                          height - self.ground.get_height() - item.height))
        for index, item in enumerate(self.Crossed):
            item.absMove((width - 300 + (70 * (index + 1)) - 25,
                          height - self.ground.get_height() - item.height))

    def draw(self):
        # Fill Background
        screen.fill((255, 255, 255))
        screen.blit(self.background, self.background.get_rect())
        pg.draw.rect(self.ground, (30, 160, 255),
                     (300, 0, 445, self.ground.get_height()), 0)
        screen.blit(self.ground, (0, height - self.ground.get_height()))
        # Draw title
        head_font = pg.font.SysFont(None, 16)
        text_surface = head_font.render(
            'wolf & sheep & cabbage [FPS: {0:.2f}]'.format(self.clock.get_fps()), True, (0, 0, 0))
        screen.blit(text_surface, (10, 10))

        # Draw Debug Info
        Info = '''
[DEBUG]\n
boat.Carrying:{0}\n
Crossed:{1}\n
NotCrossed:{2}\n
'''.format(
            self.boat.Carrying,
            self.Crossed,
            self.NotCrossed)
        for txt_index, txt in enumerate(Info.split('\n')):
            text_surface = head_font.render(
                txt, True, (0, 0, 0))
            screen.blit(text_surface, (10, 23 + (7 * txt_index)))

        # Draw Sheep
        screen.blit(self.sheep.image, self.sheep.rect)
        # Draw Wolf
        screen.blit(self.wolf.image, self.wolf.rect)
        # Draw Cabbage
        screen.blit(self.cabbage.image, self.cabbage.rect)
        # Draw Person
        screen.blit(self.person.image, self.person.rect)
        # Draw Boat
        screen.blit(self.boat.image, self.boat.rect)
        pg.display.flip()


if __name__ == "__main__":
    Game().run()
    pg.quit()
    sys.exit()
