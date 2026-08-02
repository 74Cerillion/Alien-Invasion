import pygame # Import pygame module- pygame draws the game visually

from Settings import * #import Settings file where we're storing game settings and configuration
from Ship import * #import Ship, where the Ship class is stored
import gameFunctions as gf #Import gameFunctions, where the game's mechanics are stored
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from Button import Button
from scoreboard import Scoreboard
#Leaves this document to be exclusively for actual game logic
def run_game(): #Define function to make the game run
    # Initialize game and create screen object

    pygame.init() #initialize the visual game
    ai_settings = Settings() #create an instance of the Settings class
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) #Class and Module in pygame that creates a window.
    pygame.display.set_caption("Alien Invasion") #class and module in pygame that names the window
    alien = Alien(ai_settings, screen)

    ship = Ship(ai_settings, screen) #Creates an instance of the Ship class as defined in Ship.py
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, "Play")
    sb = Scoreboard(ai_settings, screen, stats)

    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    while True: #Loop with the game logic that runs while the game is open, hence while True
        #Watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets) #Watches for keyboard and mouse events in the gameFunctions doc
        if stats.game_active:
            ship.update() # calls the Ship's update method every time the loop is ran
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button) #updates and formats the screen using the defined variables above
        #Make the most recently drawn screen visible
        pygame.display.flip() #tells python to make only the most recently drawn screen visible (update with movement)

run_game() # Calls the run_game function defined above that contains all of the game's logic