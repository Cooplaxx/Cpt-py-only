import pygame as pg #writing pygame as pg
import sys
from settings import *
from tilemap import *
from os import path
from button import *
from splashscreen import *
from game import *
from tilemap import *

pg.init() #initializes pygame
pg.mixer.init() #initializes sound

#load and play background music once
pg.mixer.music.load(path.join('sounds', 'song.mp3'))
pg.mixer.music.play(-1)

#background animation of main menu
frames = [] #frames variable as a list
for i in range(1, 23):  # Adjust the range based on your frame count
    # Load each frame image
    frame = pg.image.load(f"schoolbusgif/schoolbus{i}.jpg")
    #scale the frame to fill the screen
    scaled_frame = pg.transform.scale(frame, (WIDTH, HEIGHT))
    #append the scaled frame to the frames list
    frames.append(scaled_frame)

#frame settings
current_frame = 0  # Start with the first frame
frame_count = len(frames)  # Total number of frames

fullscreen = False  #global fullscreen variable

def get_font(size):  #function for whenever font is used we can make it the desired size
    return pg.font.Font("assets/font.ttf", size)

def set_screen_mode(): #for if our game is the default size on computer or if you change it to fullscreen
    global SCREEN, fullscreen
    if fullscreen:
        SCREEN = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
    else:
        SCREEN = pg.display.set_mode((WIDTH, HEIGHT))

def play(level, g): #function used for play button
    g.show_crawl_and_load_level(level) #calls the crawl screen in the game class
    g.run() #runs the game

def level_select(g):
    global current_frame, fullscreen #global variables from outside function
    clock = pg.time.Clock()
    set_screen_mode() #calling function of screen size

    while True:
        LEVEL_SELECT_MOUSE_POS = pg.mouse.get_pos() #mouse position
        SCREEN.blit(frames[current_frame], (0, 0))

        # Create a semi-transparent box
        box_surface = pg.Surface((400, 500), pg.SRCALPHA)  #width, height
        box_surface.fill((0, 0, 0, 128))  #color of the box

        #puts the semi-transparent box to the screen
        SCREEN.blit(box_surface, (WIDTH / 2 - 200, HEIGHT / 2 - 200))  # Position it at the center

        LEVEL_SELECT_TEXT = get_font(70).render("Select Level", True, "White") #level select text
        LEVEL_SELECT_RECT = LEVEL_SELECT_TEXT.get_rect(center=(WIDTH / 2, HEIGHT / 6 - 50)) #size of the level select rectangle
        SCREEN.blit(LEVEL_SELECT_TEXT, LEVEL_SELECT_RECT) #puts the words "level select" on the screen

        #level variables for calling the button class for each level
        LEVEL_1_BUTTON = Button(image=None, pos=(WIDTH / 2, HEIGHT / 2 - 100),
                                text_input="LEVEL 1", font=get_font(55), base_color="White", hovering_color="Green")
        LEVEL_2_BUTTON = Button(image=None, pos=(WIDTH / 2, HEIGHT / 2),
                                text_input="LEVEL 2", font=get_font(55), base_color="White", hovering_color="Green")
        LEVEL_3_BUTTON = Button(image=None, pos=(WIDTH / 2, HEIGHT / 2 + 100),
                                text_input="LEVEL 3", font=get_font(55), base_color="White", hovering_color="Green")
        BACK_BUTTON = Button(image=None, pos=(WIDTH / 2, HEIGHT / 2 + 200),
                             text_input="BACK", font=get_font(55), base_color="White", hovering_color="Red")

        for button in [LEVEL_1_BUTTON, LEVEL_2_BUTTON, LEVEL_3_BUTTON, BACK_BUTTON]:
            button.changeColor(LEVEL_SELECT_MOUSE_POS) #when mouse hovers over button it will change color
            button.update(SCREEN) #updates the screen

        for event in pg.event.get(): #level select loop
            if event.type == pg.QUIT: #checks if you hit quit
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN: #what happens if you hit each level button
                g.button_click_sound.play()  # Play button click sound
                if LEVEL_1_BUTTON.checkForInput(LEVEL_SELECT_MOUSE_POS):
                    play('level1.tmx', g)
                if LEVEL_2_BUTTON.checkForInput(LEVEL_SELECT_MOUSE_POS):
                    play('level2.tmx', g)
                if LEVEL_3_BUTTON.checkForInput(LEVEL_SELECT_MOUSE_POS):
                    play('level3.tmx', g)
                if BACK_BUTTON.checkForInput(LEVEL_SELECT_MOUSE_POS):
                    main_menu(g)

        #display the high score
        font = pg.font.Font(None, 36)  #adjust the font size as needed
        text = font.render(f'High Score: {g.high_score}', True, pg.Color('gold'))
        SCREEN.blit(text, (WIDTH - 10 - text.get_width(), HEIGHT - 40))  #bottom right corner where the text goes

        current_frame = (current_frame + 1) % frame_count
        clock.tick(10) #frame rate of menu
        pg.display.update()

def options(g):
    while True:
        OPTIONS_MOUSE_POS = pg.mouse.get_pos()
        SCREEN.blit(frames[current_frame], (0, 0))  #blits the background animation

        #creates a semi transparent box
        box_surface = pg.Surface((400, 300), pg.SRCALPHA)
        box_surface.fill((0, 0, 0, 128))
        SCREEN.blit(box_surface, (WIDTH / 2 - 200, HEIGHT / 2 - 150))

        #options text
        OPTIONS_TEXT = get_font(75).render("OPTIONS", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(WIDTH / 2, HEIGHT / 7))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        #buttons for tutorial, settings and back
        TUTORIAL_BUTTON = Button(image=None, pos=(WIDTH / 2, HEIGHT / 2.2 - 50),
                                 text_input="TUTORIAL", font=get_font(40), base_color="White", hovering_color="Green")
        SETTINGS_BUTTON = Button(image=None, pos=(WIDTH / 2, HEIGHT / 2.2 + 50),
                                 text_input="SETTINGS", font=get_font(40), base_color="White", hovering_color="Green")
        BACK_BUTTON = Button(image=None, pos=(WIDTH / 2, HEIGHT / 2.2 + 150),
                             text_input="BACK", font=get_font(40), base_color="White", hovering_color="Red")

        for button in [TUTORIAL_BUTTON, SETTINGS_BUTTON, BACK_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        for event in pg.event.get(): #options loop
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                g.button_click_sound.play()  #play button click sound
                if TUTORIAL_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    tutorial(g)  #display the tutorial image
                if SETTINGS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    settings(g) #settings is called
                if BACK_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu(g)

        pg.display.update()

def settings(g):
    global current_frame, SCREEN, fullscreen  #declare SCREEN and fullscreen as global
    clock = pg.time.Clock()
    volume = pg.mixer.music.get_volume()  #get current volume
    set_screen_mode()

    while True:
        SETTINGS_MOUSE_POS = pg.mouse.get_pos()
        SCREEN.blit(frames[current_frame], (0, 0))  # Blit the background animation

        #creates a semi transparent box
        box_surface = pg.Surface((400, 300), pg.SRCALPHA)
        box_surface.fill((0, 0, 0, 128))
        SCREEN.blit(box_surface, (WIDTH / 2 - 200, HEIGHT / 2 - 150))

        SETTINGS_TEXT = get_font(45).render("SETTINGS", True, "White")
        SETTINGS_RECT = SETTINGS_TEXT.get_rect(center=(WIDTH / 2, HEIGHT / 4))
        SCREEN.blit(SETTINGS_TEXT, SETTINGS_RECT)

        VOLUME_TEXT = get_font(30).render("Volume", True, "White") #size of volume text
        VOLUME_RECT = VOLUME_TEXT.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 50))
        SCREEN.blit(VOLUME_TEXT, VOLUME_RECT) #puts the volume text on screen

        #drawing volume slider
        pg.draw.rect(SCREEN, "White", (WIDTH / 2 - 100, HEIGHT / 2, 200, 10))
        pg.draw.circle(SCREEN, "Green", (int(WIDTH / 2 - 100 + volume * 200), HEIGHT / 2), 10)

        #button for fullscreen
        FULLSCREEN_BUTTON = Button(image=None, pos=(WIDTH / 2, HEIGHT / 2 + 50),
                                   text_input="FULLSCREEN", font=get_font(30), base_color="White", hovering_color="Green")
        BACK_BUTTON = Button(image=None, pos=(WIDTH / 2, HEIGHT / 2 + 150),
                             text_input="BACK", font=get_font(55), base_color="White", hovering_color="Red")

        for button in [FULLSCREEN_BUTTON, BACK_BUTTON]:
            button.changeColor(SETTINGS_MOUSE_POS)
            button.update(SCREEN)

        for event in pg.event.get(): #settings loop
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                g.button_click_sound.play()  #play button click sound
                if event.button == 1:
                    if BACK_BUTTON.checkForInput(SETTINGS_MOUSE_POS):
                        options(g)#back button takes you to options
                    if FULLSCREEN_BUTTON.checkForInput(SETTINGS_MOUSE_POS):
                        fullscreen = not fullscreen
                        set_screen_mode()
                    #check if the volume slider is being adjusted
                    if WIDTH / 2 - 100 <= SETTINGS_MOUSE_POS[0] <= WIDTH / 2 + 100 and HEIGHT / 2 - 10 <= SETTINGS_MOUSE_POS[1] <= HEIGHT / 2 + 10:
                        volume = (SETTINGS_MOUSE_POS[0] - (WIDTH / 2 - 100)) / 200
                        pg.mixer.music.set_volume(volume)  #set the volume for the music
                        g.shoot_sound.set_volume(volume)  #set the volume for the shoot sound
                        g.death_sound.set_volume(volume)  #set the volume for the death sound
                        g.collect_sound.set_volume(volume)  #set the volume for the collect sound
                        g.button_click_sound.set_volume(volume)  #set the volume for the button click sound

        current_frame = (current_frame + 1) % frame_count
        clock.tick(10)
        pg.display.update()

def tutorial(g): #tutorial function what to do when tutorial is hit
    global current_frame
    clock = pg.time.Clock()
    set_screen_mode()

    while True:
        TUTORIAL_MOUSE_POS = pg.mouse.get_pos()
        SCREEN.fill((0, 0, 0))  #fill the screen with black

        #load and display the tutorial image
        tutorial_img = pg.image.load('img/tutorial.jpg').convert_alpha() #shows the image used in the tutorial
        tutorial_img = pg.transform.scale(tutorial_img, (WIDTH, HEIGHT))  #scale the image to fit the screen
        SCREEN.blit(tutorial_img, (0, 0))

        BACK_BUTTON = Button(image=None, pos=(WIDTH - 100, HEIGHT - 50),
                             text_input="BACK", font=get_font(55), base_color="BLACK", hovering_color="Red")

        BACK_BUTTON.changeColor(TUTORIAL_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        for event in pg.event.get(): #tutorial loop
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                g.button_click_sound.play()  # Play button click sound
                if BACK_BUTTON.checkForInput(TUTORIAL_MOUSE_POS):
                    options(g)

        current_frame = (current_frame + 1) % frame_count
        clock.tick(10)
        pg.display.update()

def main_menu(g): #main menu function
    global current_frame

    clock = pg.time.Clock() #frame rate
    set_screen_mode()
    pg.mixer.music.load(path.join('sounds', 'song.mp3')) #plays this song
    pg.mixer.music.play(-1)

    while True:
        SCREEN.blit(frames[current_frame], (0, 0))
        MENU_MOUSE_POS = pg.mouse.get_pos() #mouse position


        MENU_TEXT = get_font(50).render("The Bell Doesn't Dismiss You!", True, "Yellow")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        #buttons for play, options and quit
        PLAY_BUTTON = Button(image=pg.image.load("menubuttons/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(55), base_color="White", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=pg.image.load("menubuttons/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(55), base_color="White", hovering_color="Green")
        QUIT_BUTTON = Button(image=pg.image.load("menubuttons/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(55), base_color="White", hovering_color="Red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS) #position of mouse changes button color
            button.update(SCREEN)

        for event in pg.event.get(): #menu screen loop
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                g.button_click_sound.play()  # Play button click sound
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    level_select(g)  # Go to level select screen

                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options(g)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pg.quit()
                    sys.exit()

        # Update the frame index for the next loop iteration
        current_frame = (current_frame + 1) % frame_count

        # Control the frame rate
        clock.tick(10)

        pg.display.update()

splash = splashscreen() #variable for splashscreen class
splash.show_start_screen() #calls the show start screen of the splascreen class
g = Game(play, main_menu) #variable for game class
main_menu(g)#calls main menu function
