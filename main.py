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

    def __init__(self, player, alien_group, player_laser_group, alien_laser_group):
        """Initialize the game"""
        #Set game values
        self.round = 1
        self.score = 0

        self.player = player
        self.alien_group = alien_group
        self.player_laser_group = player_laser_group
        self.alien_laser_group = alien_laser_group

        #Set sounds and music
        self.new_round_sound = pygame.mixer.Sound("new_round.wav")
        self.breach_sound = pygame.mixer.Sound("breach.wav")
        self.alien_hit_sound = pygame.mixer.Sound("alien_hit.wav")
        self.player_hit_sound = pygame.mixer.Sound("player_hit.wav")

        #Set font
        self.font = pygame.font.Font("Facon.ttf", 32)

    def update(self):
        """Update the game"""
        self.shift_aliens()
        self.check_collisions()
        self.check_round_completion()

    def draw(self):
        """Draw the HUD and other information to display"""
        #Set colors
        WHITE = (255,255,255)

        #Set text
        score_text = self.font.render("Score: " + str(self.score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.centerx = WINDOW_WIDTH//2
        score_rect.top = 10

        round_text = self.font.render("Round: " + str(self.round), True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topleft = (20, 10)

        lives_text = self.font.render("Lives: " + str(self.player.lives), True, WHITE)
        lives_rect = lives_text.get_rect()
        lives_rect.topright = (WINDOW_WIDTH - 20, 10)

        #Blit the HUD to the display
        display_surface.blit(score_text, score_rect)
        display_surface.blit(round_text, round_rect)
        display_surface.blit(lives_text, lives_rect)
        pygame.draw.line(display_surface, WHITE, (0,50), (WINDOW_WIDTH, 50), 4)
        pygame.draw.line(display_surface, WHITE, (0, WINDOW_HEIGHT-100), (WINDOW_WIDTH, WINDOW_HEIGHT - 100), 4)

    def shift_aliens(self):
        """Shift a wave of aliens down the screen and reverse directions"""
        pass

    def check_collisions(self):
        """Check for collisions"""
        pass

    def start_new_round(self):
        """Start a new round"""
        #Create a grid of aliens 5 rows by 11 columns
        for i in range(11):
            for j in range (5):
                alien = Alien(64 + i*64, 64 + j*64, self.round, self.alien_laser_group)
                self.alien_group.add(alien)

        #Pause the game and prompt the user to start
        self.new_round_sound.play()
        self.pause_game()


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

    def __init__(self, laser_group):
        """Initialize the player"""
        super().__init__()
        self.image = pygame.image.load("player_ship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT

        self.lives = 5
        self.velocity = 8
        self.laser_group = laser_group

        self.shoot_sound = pygame.mixer.Sound("player_fire.wav")

    def update(self):
        """Update the player"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity

    def fire(self):
        """Fire a laser"""
        #Restrict the number of bullets on screen at a time
        if len(self.laser_group) < 2:
            self.shoot_sound.play()
            PlayerLaser(self.rect.centerx, self.rect.top, self.laser_group)

    def reset(self):
        """Reset the player's position"""
        self.rect.centerx = WINDOW_WIDTH//2


class Alien(pygame.sprite.Sprite):
    """A class to model an enemy alien"""

    def __init__(self, x, y, velocity, laser_group):
        """Initialize the alien"""
        super().__init__()
        self.image = pygame.image.load("alien.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.starting_x = x
        self.starting_y = y

        self.direction = 1
        self.velocity = velocity
        self.laser_group = laser_group

        self.shoot_sound = pygame.mixer.Sound("alien_fire.wav")

    def update(self):
        """Update the alien"""
        self.rect.x += self.velocity * self.direction

        #Randomly fire a laser
        if random.randint(0, 1000) > 999 and len(self.laser_group) < 3:
            self.shoot_sound.play()
            self.fire()

    def fire(self):
        """Fire a laser"""
        AlienLaser(self.rect.centerx, self.rect.bottom, self.laser_group)

    def reset(self):
        """Reset the alien's position"""
        self.rect.topleft = (self.starting_x, self.starting_y)
        self.direction = 1

class PlayerLaser(pygame.sprite.Sprite):
    """A class to model a laser fired by the player"""

    def __init__(self, x, y, laser_group):
        """Initialize the laser"""
        super().__init__()
        self.image = pygame.image.load("green_laser.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.velocity = 10
        laser_group.add(self)
        pass

    def update(self):
        """Update the laser"""
        self.rect.y -= self.velocity
        #If the laser is off the screen, destroy it
        if self.rect.bottom < 0:
            self.kill()

class AlienLaser(pygame.sprite.Sprite):
    """A class to model a laser fired by the player"""

    def __init__(self, x, y, laser_group):
        """Initialize the laser"""
        super().__init__()
        self.image = pygame.image.load("red_laser.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.velocity = 10
        laser_group.add(self)

    def update(self):
        """Update the laser"""
        self.rect.y += self.velocity
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()

#Create laser groups
player_laser_group = pygame.sprite.Group()
alien_laser_group = pygame.sprite.Group()

#Create a player group and player object
player_group = pygame.sprite.Group()
player = Player(player_laser_group)
player_group.add(player)

#Create an alien group. We will add alien objects via the game's start new round method
alien_group = pygame.sprite.Group()

#Create a Game object
game = Game(player, alien_group, player_laser_group, alien_laser_group)
game.start_new_round()


#The main game loop
running = True
while running:
    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #The player wants to fire
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.fire()

    #Fill the display
    display_surface.fill((0,0,0))

    #Update and display all sprite groups
    player_group.update()
    player_group.draw(display_surface)

    alien_group.update()
    alien_group.draw(display_surface)

    player_laser_group.update()
    player_laser_group.draw(display_surface)

    alien_laser_group.update()
    alien_laser_group.draw(display_surface)

    #Update and draw Game object
    game.update()
    game.draw()

    #Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()