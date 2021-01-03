from pygame import time
from pygame.locals import QUIT
import sys
import os
import pygame as pg

from GObject.Sheep import Sheep
from GObject.Wolf import Wolf
from GObject.Cabbage import Cabbage
from GObject.Boat import Boat
from GObject.Person import Person
from GObject.Cloud import Cloud
from GObject.UIObject import UIObject


class Game:

    def __init__(self):
        self.fps = 60
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 20)

        self.done = False
        self.reset = False
        self.gameover = False
        self.complete = False

        self.background = pg.image.load('media/background.png')
        self.background = pg.transform.scale(
            self.background, (width, height)).convert()

        self.ground = pg.image.load('media/ground.png')
        self.ground = pg.transform.scale(self.ground, (width, (int)(
            self.ground.get_height() * (width / self.ground.get_width())))).convert_alpha()

        self.clouds = []
        for i in range(5):
            self.clouds.append(Cloud(width, 30, 300, 0.2, 0.9))

        self.Crossed = set()
        self.NotCrossed = set()

        self.boat = Boat(0, 0)
        self.boat.SetPos(
            (300, height - self.ground.get_height() - (self.boat.height * 0.5)))

        self.sheep = Sheep(0, 0)
        self.NotCrossed.add(self.sheep)
        self.sheep.SetPos((self.boat.x - (70 * len(self.NotCrossed)) - 25 - 300,
                           height - self.sheep.height - 100))

        self.cabbage = Cabbage(0, 0)
        self.NotCrossed.add(self.cabbage)
        self.cabbage.SetPos((self.boat.x - (70 * len(self.NotCrossed)) - 25 - 300,
                             height - self.cabbage.height - 100))

        self.wolf = Wolf(0, 0)
        self.NotCrossed.add(self.wolf)
        self.wolf.SetPos((self.boat.x - (70 * len(self.NotCrossed)) - 25 - 300,
                          height - self.wolf.height - 100))

        self.person = Person(300, 300)

        self.btn_reset = UIObject('media/ui/button_reset.png', 0.5, 0, 0)
        self.btn_reset.SetPos(
            (width - self.btn_reset.width - 10, 10))

        self.btn_test = UIObject('media/ui/button_empty.png', 0.5, 0, 0)
        self.btn_test.SetPos(
            (self.btn_reset.x - self.btn_test.width - 10, 10))

        self.ui_gameover = UIObject('media/ui/ui_gameover.png', 0.4, 0, 0)
        self.ui_gameover.SetPos(
            (width / 2 - self.ui_gameover.width / 2, height / 3 - self.ui_gameover.height / 2))

        self.ui_complete = UIObject('media/ui/ui_complete.png', 0.9, 0, 0)
        self.ui_complete.SetPos(
            (width / 2 - self.ui_complete.width / 2, height / 3 - self.ui_complete.height / 2))

        self.btn_replay = UIObject('media/ui/ui_replay.png', 0.22, 0, 0)
        self.btn_replay.SetPos(
            (width / 2 - self.btn_replay.width / 2, self.ui_gameover.rect.bottom + 40))

    def run(self):
        while True:
            self.handle_events()
            self.run_update()
            self.run_logic()
            self.draw()
            self.clock.tick(self.fps)
            if self.reset:
                return False
            if self.done:
                return True

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:

                    # UI Events
                    if self.btn_reset.Clicked(event):
                        self.reset = True

                    if self.btn_test.Clicked(event):
                        print('this is a test button')
                        self.boat.Move((width - 300 - self.boat.width, self.boat.y))
                        self.boat.Crossed = True
                        self.Crossed = [self.sheep, self.wolf, self.cabbage]
                        self.NotCrossed = set() 
                        
                    if self.gameover == True or self.complete == True:
                        if self.btn_replay.Clicked(event):
                            self.reset = True

                    # Object Events
                    if self.gameover == False and self.complete == False:
                        Click_Object = None
                        # Determine Clicked Object (Order by priority)
                        if self.cabbage.Clicked(event):
                            Click_Object = self.cabbage
                        if self.wolf.Clicked(event):
                            Click_Object = self.wolf
                        if self.sheep.Clicked(event):
                            Click_Object = self.sheep
                        if self.boat.Clicked(event):
                            Click_Object = self.boat
                        if self.person.Clicked(event):
                            self.person.PlayAnimation('boat_shaking')

                        # Handle Boat Event
                        if Click_Object == self.boat and self.boat.isMoving == False:
                            print('Click On Boat')
                            if self.boat.Crossed == False:
                                self.boat.Move(
                                    (width - 300 - self.boat.width, self.boat.y))
                                self.boat.Crossed = True

                            else:
                                self.boat.Move((300, self.boat.y))
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
                                        Click_Object.Move((self.boat.rect.right + 10,
                                                              height - Click_Object.height - 100))

                                    # Unload An Object to Not Crossed Side
                                    if self.boat.Crossed == False:
                                        Click_Object.Move((self.boat.x - (70 * len(self.NotCrossed)) - 25,
                                                              height - Click_Object.height - 100))
                                        self.NotCrossed.add(Click_Object)

                                    # Unload Object On The Boat
                                    self.boat.Carrying = None

                                elif self.boat.Carrying == None:

                                    # Carry A Not Crossed Object
                                    if Click_Object in self.NotCrossed and self.boat.Crossed == False:
                                        Click_Object.Move(
                                            (self.boat.x + self.boat.width - Click_Object.width - 10,
                                             self.boat.rect.bottom - Click_Object.height - 30))
                                        self.boat.Carrying = Click_Object
                                        self.NotCrossed.remove(Click_Object)

                                    # Carry A Crossed Object
                                    if Click_Object in self.Crossed and self.boat.Crossed == True:
                                        Click_Object.Move(
                                            (self.boat.x + self.boat.width - Click_Object.width - 10,
                                             self.boat.rect.bottom - Click_Object.height - 30))
                                        self.boat.Carrying = Click_Object
                                        self.Crossed.remove(Click_Object)

                                elif self.boat.Carrying != Click_Object:
                                    # Switch An Object from Crossed Side
                                    if self.boat.Crossed == True and Click_Object in self.Crossed:
                                        self.Crossed.add(self.boat.Carrying)
                                        self.boat.Carrying = Click_Object
                                        self.Crossed.remove(Click_Object)
                                        Click_Object.Move((self.boat.x + self.boat.width - Click_Object.width - 10,
                                                             self.boat.rect.bottom - Click_Object.height - 30))

                                    # Switch An Object from Not Crossed Side
                                    if self.boat.Crossed == False and Click_Object in self.NotCrossed:
                                        self.NotCrossed.add(self.boat.Carrying)
                                        self.boat.Carrying = Click_Object
                                        self.NotCrossed.remove(Click_Object)
                                        Click_Object.Move((self.boat.x + self.boat.width - Click_Object.width - 10,
                                                             self.boat.rect.bottom - Click_Object.height - 30))

    def run_update(self):
        self.person.SetPos(
            (self.boat.x + 15, self.boat.rect.bottom - self.person.height - 10))
        self.boat.Update()
        self.sheep.Update()
        self.wolf.Update()
        self.cabbage.Update()
        self.person.Update()
        for cloud in self.clouds:
            cloud.Update()
        self.btn_test.Update()


        if self.gameover == False and self.complete == False:
            Delta = 0
            for index, item in enumerate(self.NotCrossed):
                Delta = Delta + item.width + 25
                item.Move((300 - Delta,
                            height - self.ground.get_height() - item.height))

            Delta = 0
            for index, item in enumerate(self.Crossed):
                item.Move((width - 300 + Delta + 25,
                            height - self.ground.get_height() - item.height))
                Delta = Delta + item.width + 25

    def run_logic(self):
        # Determine Complete
        if self.sheep in self.Crossed and self.wolf in self.Crossed and self.cabbage in self.Crossed:
            self.complete = True

        # Determine GameOver
        if self.boat.isMoving and self.gameover == False:
            if not self.NotCrossed == set():
                for Side in [self.NotCrossed, self.Crossed]:
                    if self.sheep in Side and self.cabbage in Side:
                        self.gameover = True
                        self.sheep.Move((self.cabbage.rect.x - self.sheep.width + 45,self.cabbage.rect.bottom - self.sheep.height))
                        self.cabbage.PlayAnimation('eat_cabbage')
                        self.cabbage.SetDefaultAnimation('eaten')
                        self.sheep.PlayAnimation('eat_cabbage')
                    if self.wolf in Side and self.sheep in Side:
                        self.gameover = True
                        self.wolf.Move((self.sheep.rect.x - self.sheep.width +15 ,self.sheep.rect.bottom - self.wolf.height))
                        self.sheep.PlayAnimation('wolf_eat_sheep')
                        self.sheep.SetDefaultAnimation('sheep_dead')
                        self.wolf.PlayAnimation('wolf_eat_sheep')

    def draw(self):
        # Fill Background
        screen.fill((255, 255, 255))
        screen.blit(self.background, self.background.get_rect())
        pg.draw.rect(self.ground, (30, 160, 255),
                     (300, 0, width - 600, self.ground.get_height()), 0)
        screen.blit(self.ground, (0, height - self.ground.get_height()))
        # Draw Cloud
        for cloud in self.clouds:
            screen.blit(cloud.image, cloud.rect)
        
        # Draw title
        text_surface = self.font.render(
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
            text_surface = self.font.render(
                txt, True, (0, 0, 0))
            screen.blit(text_surface, (10, 23 + (7 * txt_index)))
        
        # Draw GameOver
        if self.gameover:
            self.ui_gameover.Draw(screen)
            self.btn_replay.Draw(screen)
        elif self.complete:
            self.ui_complete.Draw(screen)
            self.btn_replay.Draw(screen)
        
        # Draw Buttons
        self.btn_reset.Draw(screen)
        self.btn_test.Draw(screen)

        # Draw Objects
        self.wolf.Draw(screen)
        self.sheep.Draw(screen)
        self.cabbage.Draw(screen)
        self.person.Draw(screen)
        self.boat.Draw(screen)
        pg.display.flip()


if __name__ == "__main__":

    # Set Window Position
    #os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 270)

    # Start Game Window
    pg.init()
    width = 1024
    height = 768
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption('Wolf & Sheep & Cabbage')
    reRun = True
    img_loading = pg.image.load('media/ui/ui_loading.png')
    scale = (width / img_loading.get_width())
    img_loading = pg.transform.scale(img_loading, (int(img_loading.get_width() * scale), int(img_loading.get_height() * scale))).convert_alpha()
    while reRun:

        # display loading title
        screen.fill((255, 255, 255))
        screen.blit(img_loading, pg.Rect(0,0,width,height))
        pg.display.flip()

        # handle window event
        for i in range(10):
            pg.time.delay(100)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

        if not Game().run():
            reRun = True
        else:
            reRun = False

    pg.quit()
    sys.exit()
