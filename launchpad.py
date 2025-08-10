###################################################################################################################################
## Image and Code credit are all visible in Quotes within Comments. Check Below for Example                                      ##
##                                                                                                               ##
## "https://wallpaperping.com/4k-background.html"                                                                                ##
##                                                                                                               ##
## Some images have been modified / edited for the purpose of this program                                                       ##
## Links for the websites are in Quotes and Brackets. Check below for an example                                                 ##
##                                                                                                               ##
## ["https://github.com/russs123/pygame_tutorials/blob/main/Button/button.py"] - Code by russs123                                ##
##                                                                                                               ##
## Keyboard and mouse are used as program input. Mouse movement, clicks, and key presses will all register within the program    ##
##                                                                                                               ##
## Program is created using the PyGame Library which can be downloaded from ["https://www.pygame.org/wiki/GettingStarted"]       ##
###################################################################################################################################
 
# Imports Required Functions
import pygame
import random
import pygame.midi
import sys
import numpy as np
 
# Starts App
pygame.init()
pygame.midi.init()
 
# Display Size
width = 1000
height = 700
display = pygame.display.set_mode((width, height))

# Game state management
MAIN_MENU = 0
GAME_SCREEN = 1
INFO_SCREEN = 2
current_state = MAIN_MENU
 
# Dictionary created to call upon different colors
# Color RGB values taken from "https://www.rapidtables.com/web/color/RGB_Color.html"
colorDict = {
    "black": (0, 0, 0),
    "cyan": (48, 157, 176),
    "lightPurple": (53, 4, 110),
    "darkPurple": (33, 2, 69),
    "orange": (168, 114, 13),
    "lightGreen": (33, 163, 61),
    "darkGreen": (13, 71, 25),
    "lightPink": (166, 27, 117),
    "lightBlue": (30, 187, 212),
    "LightBLUE": (50, 115, 168),
    "white": (255, 255, 255),
    "yellow": (224, 227, 20),
    "darkBlue": (0, 0, 153),
    "transparent": (0, 0, 0, 0)
}
 
# Generates Random Colors
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
 
# Variable for Random Color generator
color = random_color()
 
# Class for Button
# Credit - ["https://github.com/russs123/pygame_tutorials/blob/main/Button/button.py"] - Code by russs123
class Button():
   def __init__(self, x, y, image, scale, name):
       width = image.get_width()
       height = image.get_height()
       self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
       self.rect = self.image.get_rect()
       self.rect.topleft = (x, y)
       self.clicked = False
       self.name = name
 
   def draw(self, surface):
       action = False
       # Gets the mouse position
       pos = pygame.mouse.get_pos()
 
       # Checks mouseover and clicked conditions
       if self.rect.collidepoint(pos):
           if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
               self.clicked = True
               action = True
 
       if pygame.mouse.get_pressed()[0] == 0:
           self.clicked = False
 
       # Blits a button on screen
       display.blit(self.image, (self.rect.x, self.rect.y))
 
       return action
 
# Creates the base Screen for the program
def initialScreen():
    global display
    global startButton
    global exitButton
    global infoButton
    global mainLogo
    global current_state
    current_state = MAIN_MENU
# Creates the Display (Surface) of the program + Background
    display = pygame.display.set_mode((width, height))
    backgroundImage = pygame.image.load('assets/homeScreenBackground.gif')
    backgroundImage = pygame.transform.scale(backgroundImage, (width, height))
    display.blit(backgroundImage, (0, 0))
# Creates a caption for game and draws buttons
    pygame.display.set_caption("Welcome to SoundMixer")
    soundMixerLogo = pygame.image.load('assets/fin.png').convert_alpha()
 
    display.blit(soundMixerLogo, (40, 20))
 
    startButton = Button(100, 500, imageDictionary["startButtonImg"], 0.425, "start_button")
    exitButton = Button(550, 490, imageDictionary["exitButtonImg"], 0.425, "exit_button")
    infoButton = Button(850, 30, imageDictionary["infoButtonImg"], 1.10, "info_button")
 
    pygame.display.set_icon(imageDictionary["logo"])
 
startButtonImg = pygame.image.load('assets/start_btn.png').convert_alpha()
soundMixerLogo = pygame.image.load('assets/fin.png').convert_alpha()
exitButtonImg = pygame.image.load('assets/exit_btn.png').convert_alpha()
infoButtonImg = pygame.image.load("assets/fin_question.png").convert_alpha()
 
imageDictionary = {
    "startButtonImg": pygame.image.load('assets/start_btn.png'),
    "soundMixerLogo": pygame.image.load('assets/fin.png'),
    "exitButtonImg": pygame.image.load('assets/exit_btn.png'),
    "infoButtonImg": pygame.image.load("assets/fin_question.png"),
    "logo": pygame.image.load("assets/music-wave.png"),
    "helpLogo": pygame.image.load("assets/question-mark.png")
}
 
buttonDictionary = {
    "startButton": Button(100, 500, startButtonImg, 0.425, "Start Button"),
    "exitButton": Button(550, 490, exitButtonImg, 0.425, "Exit Button"),
    "infoButton": Button(850, 30, infoButtonImg, 1.10, "Info Button")
 
}
 
# Creates the game Screen for the program
def nextScreen():
    global display
    global BG
    global current_state
    current_state = GAME_SCREEN
    Boxes()

    # Get display size dynamically
    display_width, display_height = display.get_size()

    # Load and scale newLogo.png to ~65% of original size
    gameLogo = pygame.image.load('assets/newLogo.png').convert_alpha()
    logo_width, logo_height = gameLogo.get_width(), gameLogo.get_height()
    scaled_width = int(logo_width * 0.75)
    scaled_height = int(logo_height * 0.75)
    gameLogo = pygame.transform.scale(gameLogo, (scaled_width, scaled_height))

    pygame.display.set_caption("LaunchPAD - Welcome to Unfound Sounds!")

    # Center horizontally, move a bit higher than before
    logo_x = (display_width - scaled_width) // 2
    logo_y = -210
    display.blit(gameLogo, (logo_x, logo_y))
 
# Draws All boxes for the LaunchPad
def Boxes():
    width = 80
    height = 80
    newWidth = 280
    # Q W E R T Y U I O P
    for i in range(10, 911, 100):
        pygame.draw.rect(display, colorDict["lightPink"], (i, 270, width, height), 5)
    #  A S D F G H J K L
    for i in range(60, 900, 100):
        pygame.draw.rect(display, colorDict["lightPink"], (i, 370, width, height), 5)
    # Z X C V B N M
    for i in range(170, 800, 100):
        pygame.draw.rect(display, colorDict["lightPink"], (i, 470, width, height), 5)
    # 1 2 3
    for i in range(60, 661, 300):
        pygame.draw.rect(display, colorDict["lightPink"], (i, 590, newWidth, height + 5), 5)
 
 
KEYDOWN = pygame.key.get_pressed()
 
# Colors the board accordingly if a key is pressed
def drawBoard():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            pygame.draw.rect(display, color, (60, 370, 80, 80))
        if event.key == pygame.K_b:
            pygame.draw.rect(display, color, (570, 470, 80, 80))
        if event.key == pygame.K_c:
            pygame.draw.rect(display, color, (370, 470, 80, 80))
        if event.key == pygame.K_d:
            pygame.draw.rect(display, color, (260, 370, 80, 80))
        if event.key == pygame.K_e:
            pygame.draw.rect(display, color, (210, 270, 80, 80))
        if event.key == pygame.K_f:
            pygame.draw.rect(display, color, (360, 370, 80, 80))
        if event.key == pygame.K_g:
            pygame.draw.rect(display, color, (460, 370, 80, 80))
        if event.key == pygame.K_h:
            pygame.draw.rect(display, color, (560, 370, 80, 80))
        if event.key == pygame.K_i:
            pygame.draw.rect(display, color, (710, 270, 80, 80))
        if event.key == pygame.K_j:
            pygame.draw.rect(display, color, (660, 370, 80, 80))
        if event.key == pygame.K_k:
            pygame.draw.rect(display, color, (760, 370, 80, 80))
        if event.key == pygame.K_l:
            pygame.draw.rect(display, color, (860, 370, 80, 80))
        if event.key == pygame.K_m:
            pygame.draw.rect(display, color, (770, 470, 80, 80))
        if event.key == pygame.K_n:
            pygame.draw.rect(display, color, (670, 470, 80, 80))
        if event.key == pygame.K_o:
            pygame.draw.rect(display, color, (810, 270, 80, 80))
        if event.key == pygame.K_p:
            pygame.draw.rect(display, color, (910, 270, 80, 80))
        if event.key == pygame.K_q:
            pygame.draw.rect(display, color, (10, 270, 80, 80))
        if event.key == pygame.K_r:
            pygame.draw.rect(display, color, (310, 270, 80, 80))
        if event.key == pygame.K_s:
            pygame.draw.rect(display, color, (160, 370, 80, 80))
        if event.key == pygame.K_t:
            pygame.draw.rect(display, color, (410, 270, 80, 80))
        if event.key == pygame.K_u:
            pygame.draw.rect(display, color, (610, 270, 80, 80))
        if event.key == pygame.K_v:
            pygame.draw.rect(display, color, (470, 470, 80, 80))
        if event.key == pygame.K_w:
            pygame.draw.rect(display, color, (110, 270, 80, 80))
        if event.key == pygame.K_x:
            pygame.draw.rect(display, color, (270, 470, 80, 80))
        if event.key == pygame.K_y:
            pygame.draw.rect(display, color, (510, 270, 80, 80))
        if event.key == pygame.K_z:
            pygame.draw.rect(display, color, (170, 470, 80, 80))
        if event.key == pygame.K_1:
            pygame.draw.rect(display, color, (60, 590, 275, 80))
        if event.key == pygame.K_2:
            pygame.draw.rect(display, color, (360, 590, 275, 80))
        if event.key == pygame.K_3:
            pygame.draw.rect(display, color, (660, 590, 275, 80))
        pygame.display.flip()
 
# Dictionary storing all the key values for audio

# MIDI note mapping for keys (A-Z, 1-3)

# Key to frequency mapping (A-Z, 1-3)
key_to_freq = {
    pygame.K_a: 261.63,  # C4
    pygame.K_b: 293.66,  # D4
    pygame.K_c: 329.63,  # E4
    pygame.K_d: 349.23,  # F4
    pygame.K_e: 392.00,  # G4
    pygame.K_f: 440.00,  # A4
    pygame.K_g: 493.88,  # B4
    pygame.K_h: 523.25,  # C5
    pygame.K_i: 587.33,  # D5
    pygame.K_j: 659.25,  # E5
    pygame.K_k: 698.46,  # F5
    pygame.K_l: 783.99,  # G5
    pygame.K_m: 880.00,  # A5
    pygame.K_n: 987.77,  # B5
    pygame.K_o: 1046.50, # C6
    pygame.K_p: 1174.66, # D6
    pygame.K_q: 1318.51, # E6
    pygame.K_r: 1396.91, # F6
    pygame.K_s: 1567.98, # G6
    pygame.K_t: 1760.00, # A6
    pygame.K_u: 1975.53, # B6
    pygame.K_v: 2093.00, # C7
    pygame.K_w: 2349.32, # D7
    pygame.K_x: 2637.02, # E7
    pygame.K_y: 2793.83, # F7
    pygame.K_z: 3135.96, # G7
    pygame.K_1: 261.63,  # C4
    pygame.K_2: 329.63,  # E4
    pygame.K_3: 392.00,  # G4
}

# Generate a pygame Sound for a given frequency
def make_tone(freq, duration=0.5, volume=0.5, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(freq * t * 2 * np.pi)
    audio = wave * (2**15 - 1) * volume
    audio = audio.astype(np.int16)
    # Ensure 2D array for stereo mixer
    if len(audio.shape) == 1:
        audio = np.column_stack((audio, audio))
    return pygame.sndarray.make_sound(audio)

# Cache for generated tones
tones = {}
 
# Checks in dictionary for key and plays its audio accordingly
def soundPlay():
    pygame.key.set_repeat()
    if event.key in key_to_freq:
        freq = key_to_freq[event.key]
        if event.key not in tones:
            tones[event.key] = make_tone(freq)
        tones[event.key].play(-1)  # loop until stopped
 
# Checks in dictionary for key and stops its audio accordingly
def soundStop():
    if event.key in tones:
        tones[event.key].stop()
 
# Clears the board if the key is not being pressed
def clearBoard():
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
            pygame.draw.rect(display, colorDict["darkPurple"], (60, 370, 80, 80))
        if event.key == pygame.K_b:
            pygame.draw.rect(display, colorDict["darkPurple"], (570, 470, 80, 80))
        if event.key == pygame.K_c:
            pygame.draw.rect(display, colorDict["darkPurple"], (370, 470, 80, 80))
        if event.key == pygame.K_d:
            pygame.draw.rect(display, colorDict["darkPurple"], (260, 370, 80, 80))
 
        if event.key == pygame.K_e:
            pygame.draw.rect(display, colorDict["darkPurple"], (210, 270, 80, 80))
        if event.key == pygame.K_f:
            pygame.draw.rect(display, colorDict["darkPurple"], (360, 370, 80, 80))
        if event.key == pygame.K_g:
            pygame.draw.rect(display, colorDict["darkPurple"], (460, 370, 80, 80))
        if event.key == pygame.K_h:
            pygame.draw.rect(display, colorDict["darkPurple"], (560, 370, 80, 80))
 
        if event.key == pygame.K_i:
            pygame.draw.rect(display, colorDict["darkPurple"], (710, 270, 80, 80))
        if event.key == pygame.K_j:
            pygame.draw.rect(display, colorDict["darkPurple"], (660, 370, 80, 80))
        if event.key == pygame.K_k:
            pygame.draw.rect(display, colorDict["darkPurple"], (760, 370, 80, 80))
        if event.key == pygame.K_l:
            pygame.draw.rect(display, colorDict["darkPurple"], (860, 370, 80, 80))
        if event.key == pygame.K_m:
            pygame.draw.rect(display, colorDict["darkPurple"], (770, 470, 80, 80))
        if event.key == pygame.K_n:
            pygame.draw.rect(display, colorDict["darkPurple"], (670, 470, 80, 80))
 
        if event.key == pygame.K_o:
            pygame.draw.rect(display, colorDict["darkPurple"], (810, 270, 80, 80))
        if event.key == pygame.K_p:
            pygame.draw.rect(display, colorDict["darkPurple"], (910, 270, 80, 80))
        if event.key == pygame.K_q:
            pygame.draw.rect(display, colorDict["darkPurple"], (10, 270, 80, 80))
        if event.key == pygame.K_r:
            pygame.draw.rect(display, colorDict["darkPurple"], (310, 270, 80, 80))
        if event.key == pygame.K_s:
            pygame.draw.rect(display, colorDict["darkPurple"], (160, 370, 80, 80))
        if event.key == pygame.K_t:
            pygame.draw.rect(display, colorDict["darkPurple"], (410, 270, 80, 80))
 
        if event.key == pygame.K_u:
            pygame.draw.rect(display, colorDict["darkPurple"], (610, 270, 80, 80))
        if event.key == pygame.K_v:
            pygame.draw.rect(display, colorDict["darkPurple"], (470, 470, 80, 80))
        if event.key == pygame.K_w:
            pygame.draw.rect(display, colorDict["darkPurple"], (110, 270, 80, 80))
        if event.key == pygame.K_x:
            pygame.draw.rect(display, colorDict["darkPurple"], (270, 470, 80, 80))
        if event.key == pygame.K_y:
            pygame.draw.rect(display, colorDict["darkPurple"], (510, 270, 80, 80))
        if event.key == pygame.K_z:
            pygame.draw.rect(display, colorDict["darkPurple"], (170, 470, 80, 80))
 
        if event.key == pygame.K_1:
            pygame.draw.rect(display, colorDict["darkPurple"], (60, 590, 275, 80))
        if event.key == pygame.K_2:
            pygame.draw.rect(display, colorDict["darkPurple"], (360, 590, 275, 80))
        if event.key == pygame.K_3:
            pygame.draw.rect(display, colorDict["darkPurple"], (660, 590, 275, 80))
 
        pygame.display.update()
 
# Information screen
def info_screen():
    global display
    global current_state
    current_state = INFO_SCREEN
    pygame.display.set_icon(imageDictionary["helpLogo"])
    display.fill(colorDict["lightBlue"])
    x = 270
    y = 80
    width = 450
    height = 550
    lineWidth = 7
 
    pygame.display.set_caption("Instruction / Help Screen!!!!")
 
    displayImg = pygame.image.load('assets/cityskies.png')
    display.blit(displayImg, (0, 0))
 
    pygame.draw.rect(display, colorDict["darkBlue"], (x, y, width, height), lineWidth)
    pygame.draw.rect(display, colorDict["lightBlue"], (280, 90, 430, 530))
 
    display.blit(instructionDictionary["line1"], infoRectDict["textRect1"])
    display.blit(instructionDictionary["line2"], infoRectDict["textRect2"])
    display.blit(instructionDictionary["line3"], infoRectDict["textRect3"])
    display.blit(instructionDictionary["line4"], infoRectDict["textRect4"])
    display.blit(instructionDictionary["line5"], infoRectDict["textRect5"])
    display.blit(instructionDictionary["line6"], infoRectDict["textRect6"])
    display.blit(instructionDictionary["line7"], infoRectDict["textRect7"])
    display.blit(instructionDictionary["line8"], infoRectDict["textRect8"])
 
 
startButtonImg = pygame.image.load('assets/start_btn.png').convert_alpha()
soundMixerLogo = pygame.image.load('assets/fin.png').convert_alpha()
exitButtonImg = pygame.image.load('assets/exit_btn.png').convert_alpha()
infoButtonImg = pygame.image.load("assets/fin_question.png").convert_alpha()
startButton = Button(100, 500, imageDictionary["startButtonImg"], 0.425, "start_button")
exitButton = Button(550, 490, imageDictionary["exitButtonImg"], 0.425, "exit_button")
infoButton = Button(850, 30, imageDictionary["infoButtonImg"], 1.10, "info_button")
 
initialScreen()
 
# ALL FONTS USED
fontDictionary = {
    "font1": pygame.font.SysFont('comicsans', 24),
    "font2": pygame.font.SysFont('Segoe UI', 80),
    "font3": pygame.font.SysFont('inkfree', 40),
    "font4": pygame.font.SysFont("segoeprb.ttf", 33),
    "font5": pygame.font.SysFont("inkfree", 38, italic=True)
}
 
# Text used in Information Screen
instructionDictionary = {
    "line1": fontDictionary["font2"].render('Instructions: ', True, colorDict["lightPink"]),
    "line2": fontDictionary["font1"].render('For each Key being pressed,', True, colorDict["white"]),
    "line3": fontDictionary["font1"].render('A sound will play.', True, colorDict["white"]),
    "line4": fontDictionary["font1"].render('If the Key is held, the sound will ', True, colorDict["white"]),
    "line5": fontDictionary["font1"].render('play continuously.', True, colorDict["white"]),
    "line6": fontDictionary["font3"].render('Create your own Tunes !! ', True, colorDict["lightPurple"]),
    "line7": fontDictionary["font4"].render("To go back to Home,", True, colorDict["darkPurple"]),
    "line8": fontDictionary["font4"].render("Press ESC on keyboard", True, colorDict["darkPurple"]),
    "line9": fontDictionary["font5"].render("Create Your Own Tunes!", True, colorDict["darkBlue"])
}
 
# The location of each instruction
infoRectDict = {
    "textRect1": instructionDictionary["line1"].get_rect(),
    "textRect2": instructionDictionary["line2"].get_rect(),
    "textRect3": instructionDictionary["line3"].get_rect(),
    "textRect4": instructionDictionary["line4"].get_rect(),
    "textRect5": instructionDictionary["line5"].get_rect(),
    "textRect6": instructionDictionary["line6"].get_rect(),
    "textRect7": instructionDictionary["line7"].get_rect(),
    "textRect8": instructionDictionary["line8"].get_rect(),
    "textRect9": instructionDictionary["line9"].get_rect()
}
 
 
# LIST FOR ALL THE TEXT RECTANGLES TO BE CALLED
ALL_INFO = [infoRectDict["textRect1"], infoRectDict["textRect2"], infoRectDict["textRect3"],
            infoRectDict["textRect4"], infoRectDict["textRect5"], infoRectDict["textRect6"],
            infoRectDict["textRect7"], infoRectDict["textRect8"], infoRectDict["textRect9"]
]
 
# LOCATION OF ALL THE TEXT RECTANGLES
ALL_INFO[0].center = (width // 2, 200)
ALL_INFO[1].center = (width // 2, 300)
ALL_INFO[2].center = (width // 2, 345)
ALL_INFO[3].center = (width // 2, 390)
ALL_INFO[4].center = (width // 2, 425)
ALL_INFO[5].center = (width // 2, 555)
ALL_INFO[6].center = (width // 2, 470)
ALL_INFO[7].center = (width // 2, 500)
ALL_INFO[8].center = (width // 2, 100)
pygame.display.update()
 
i = 0
FPS = 60
 
 
# game Loop
clock = pygame.time.Clock()
run = True
 
additionalRenders = []
 
while run:
    clock.tick(FPS)
    event = None
 
 
    def random_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)
 
 
    color = random_color()
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                display.blit(imageDictionary["soundMixerLogo"], (-55, 20))
                print("Testing : You have went back")
                additionalRenders.clear()
                initialScreen()
            # Only handle game keys if we're on the game screen
            elif current_state == GAME_SCREEN:
                Boxes()
                soundPlay()
                drawBoard()

        elif event.type == pygame.KEYUP:
            # Only handle key releases if we're on the game screen
            if current_state == GAME_SCREEN:
                clearBoard()
                soundStop()
                clearBoard()
 
    for additionalRender in additionalRenders:
        additionalRender()
 
    if startButton.draw(display):
        # Tests if the program is working
        print('Testing if Start Screen is loading')
        # Fills the screen background
        display.fill(colorDict["darkPurple"])
        startButton.image.fill(colorDict["transparent"])
        exitButton.image.fill(colorDict["transparent"])
        additionalRenders.clear()
        additionalRenders.append(nextScreen)
 
    if exitButton.draw(display):
        run = False
        print('You have Exited the App')
 
    if infoButton.draw(display):
        print(" Testing if Info Screen is loading : Info Screen")
        startButton.image.fill(colorDict["transparent"])
        exitButton.image.fill(colorDict["transparent"])
        additionalRenders.clear()
        additionalRenders.append(info_screen)
    pygame.display.update()
 
    # quit game
    if event is None:
        continue
 
    if event.type == pygame.QUIT:
        run = False
 
    pygame.display.update()
 
pygame.quit()