import pygame
from listclass import *
from variables import *
import time
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Aidez MacGyver à s'échapper ! ")
window = pygame.display.set_mode((window_side, window_side))

#########################################  Building  ####################################################

# Build Labyrinth:
laby = Labyrinth("15x15")
laby.construct()
laby.display_laby(window)

# Build Background
background = pygame.image.load("images/background.jpg").convert()

# Build Objects
GoldCoin = Objects("images/goldcoin.png")
SilverCoin = Objects("images/silvercoin.png")
BronzeCoin = Objects("images/bronzecoin.png")

list_coin = [GoldCoin, SilverCoin, BronzeCoin]

# Build Player
MacGyver = Player("images/MacGyver.png")

# Font
font = pygame.font.Font(None, 24)
font_victory_defeat = pygame.font.Font(None, 100)


#######################################  Game loop  ########################################################

launched = True
while launched:

    pygame.time.Clock().tick(30)

    #### listclass.py ####
    event_quit_move = event_quit_or_move(laby, MacGyver)
    if event_quit_move == False:
        launched = False

    ########################### Text Variable ##########################
    ### counter ###
    remaining_items = get_number_remaining_items(list_coin)
    Score = font.render("Objets restant(s) : " + str(remaining_items), 1, (255, 0, 0))
    ### victory or defeat ###
    Victory = font_victory_defeat.render("Victoire !", 1, (0, 170, 40))
    Defeat = font_victory_defeat.render("Défaite !", 1, (255, 0, 0))

    ########################### Position display ###########################
    window.blit(background, (0, 0))
    laby.display_laby(window)
    window.blit(MacGyver.image, (MacGyver.x, MacGyver.y))
    window.blit(Score, (300, 440))

    #### listclass.py ####
    items_dont_appear_on_wall(laby, window, list_coin)

    pygame.display.flip()

    #### listclass.py ####
    # When player is on items, items disappears
    take_items(MacGyver, list_coin)

    ############################# Victory or Defeat ############################
    if laby.structure[MacGyver.case_y][MacGyver.case_x] == "G":
        display_victory_or_defeat(window, Victory, Defeat, remaining_items)
        launched = False