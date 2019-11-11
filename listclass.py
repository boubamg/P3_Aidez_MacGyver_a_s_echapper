import pygame
import random
import time
from variables import *
from pygame.locals import *


class Labyrinth:
    def __init__(self, file):
        self.file = file
        self.structure = 0

    def construct(self):
        with open(self.file, "r") as file:
            structure_level = []
            for line in file:
                line_level = []
                for sprite in line:
                    if sprite != '\n':
                        line_level.append(sprite)
                structure_level.append(line_level)
            self.structure = structure_level

    def display_laby(self, window):
        wall = pygame.image.load("images/structures1.png").convert()
        start = pygame.image.load("images/start.png").convert()
        guard = pygame.image.load("images/Guard.png").convert_alpha()

        line_number = 0
        for line in self.structure:
            num_case = 0
            for sprite in line:
                x = num_case * sprite_pixel
                y = line_number * sprite_pixel
                if sprite == 'm':  # m = wall
                    window.blit(wall, (x, y))
                elif sprite == 'S':  # S = Start
                    window.blit(start, (x, y))
                elif sprite == 'G':  # G = Guard
                    window.blit(guard, (x, y))
                num_case += 1
            line_number += 1

class Objects:
    nombre_objet = 0
    def __init__(self, image):
        Objects.nombre_objet += 1
        self.image = pygame.image.load(image).convert_alpha()

        # Objects position (case and pixels)
        self.case_x = random.randint(1, side_number - 1)
        self.case_y = random.randint(1, side_number - 1)
        self.x = self.case_x * sprite_pixel
        self.y = self.case_y * sprite_pixel

    @staticmethod
    def get_nombre_objet():
        return Objects.nombre_objet

class Player(Objects):

    def __init__(self, image):
        super().__init__(image)
        self.case_x = 1
        self.case_y = 14
        self.x = self.case_x * sprite_pixel
        self.y = self.case_y * sprite_pixel

    def move(self, direction):

        if direction == "right":
            if self.case_x < (side_number - 1):
                self.case_x += 1
                self.x = self.case_x * sprite_pixel
        if direction == "left":
            if self.case_x > 0:
                self.case_x -= 1
                self.x = self.case_x * sprite_pixel
        if direction == "top":
            if self.case_y > 0:
                self.case_y -= 1
                self.y = self.case_y * sprite_pixel
        if direction == "bottom":
            if self.case_y < (side_number - 1):
                self.case_y += 1
                self.y = self.case_y * sprite_pixel

def event_quit_or_move(Labyrinth, player):
    ########################  QUIT GAME ##################################
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            return False

        elif event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                return False

            ####################### Player Move Touch ########################

            elif event.key == K_RIGHT:
                if Labyrinth.structure[player.case_y][player.case_x + 1] != 'm':
                    player.move('right')
            elif event.key == K_LEFT:
                if Labyrinth.structure[player.case_y][player.case_x - 1] != 'm':
                    player.move('left')
            elif event.key == K_UP:
                if Labyrinth.structure[player.case_y - 1][player.case_x] != 'm':
                    player.move('top')
            elif event.key == K_DOWN:
                if Labyrinth.structure[player.case_y + 1][player.case_x] != 'm':
                    player.move('bottom')

def items_dont_appear_on_wall(Labyrinth, window, list):
    ###### Condition for objects don't appear on the wall and delete if not  #######

    for objects in list:
        if Labyrinth.structure[objects.case_y][objects.case_x] != 'm':
            window.blit(objects.image, (objects.x, objects.y))
        else:
            list.remove(objects)

def take_items(player, list):
    for objects in list:
        if player.case_x == objects.case_x and player.case_y == objects.case_y:
            list.remove(objects)

def get_number_remaining_items(list_items):
    return len(list_items)

def display_victory_or_defeat(window, Victory,Defeat,remaining_items):
    if remaining_items == 0:
        window.blit(Victory, (window_side/2-140, window_side/2-100))
    else:
        window.blit(Defeat, (window_side/2-140, window_side/2-100))
    pygame.display.flip()
    time.sleep(3)