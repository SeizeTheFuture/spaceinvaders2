import pygame
import random

#Initialize pygame
pygame.init()

#Set display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Define Classes
class Game():
    """A class to help control and update gameplay"""

    def __init__(self):
        """Initialize the game"""
        pass

    def update(self):
        """Update the game"""
        pass

    def draw(self):
        """Draw the HUD and other information to display"""
        pass

    def shift_aliens(self):
        """Shift a wave of aliens down the screen and reverse directions"""
        pass

    def check_collisions(self):
        """Check for collisions"""
        pass

    def start_new_round(self):
        """Start a new round"""
        pass

    def check_round_completion(self):
        """Check to see if a player has completed a single round"""
        pass

    def check_game_status(self):
        """Check to see the status of the game and how the player died"""
        pass

    def pause_game(self):
        """Pause the game"""
        pass

    def reset_game(self):
        """Reset the game"""
        pass

class Player(pygame.sprite.Sprite):
    """A class to model a spaceship the user can control"""

    def __init__(self):
        """Initialize the player"""
        pass

    def update(self):
        """Update the player"""
        pass

    def fire(self):
        """Fire a laser"""
        pass

    def reset(self):
        """Reset the player's position"""
        pass


class Alien(pygame.sprite.Sprite):
    """A class to model an enemy alien"""

    def __init__(self):
        """Initialize the alien"""
        pass

    def update(self):
        """Update the alien"""
        pass

    def fire(self):
        """Fire a laser"""
        pass

    def reset(self):
        """Reset the alien's position"""
        pass

class PlayerLaser(pygame.sprite.Sprite):
    pass
#The main game loop
running = True
while running:
    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()