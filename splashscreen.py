import pygame as pg
from settings import * #adds settings functionality into splascreen.py



class splashscreen: #class splashscreen
    def __init__(self): #initializes class
        pg.init()#initializes pygame within the class
        self.screen = pg.display.set_mode((WIDTH, HEIGHT)) #screen size of splash screen
        pg.display.set_caption(TITLE)


    def draw_text(self, text, size, color, x, y): #function for drawing the text of splashscreen
        font = pg.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def wait_for_key(self): #function for waiting for the input to move on loop
        waiting = True #variable waiting is set to condition true
        while waiting: #wile waiting is true loop so it doesn't run on forever
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYUP:
                    waiting = False
    def show_start_screen(self): #game splash/start screen function
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("We hope you enjoy.", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press any key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()