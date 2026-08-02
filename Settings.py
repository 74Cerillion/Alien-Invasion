class Settings(): #Defines a class containing all of the configuration settings for the game
    """All settings for Alien Invasion"""

    def __init__(self): # initializes the class
        self.screen_width = 1000 # Sets the screen width to 1000px
        self.screen_height = 600 # Sets screen height to 600px
        self.bg_color = (200, 200, 200) # Sets background color to rgb(200, 200, 200)

        self.ship_speed_factor = 0.4

        self.bullet_speed_factor = 0.45
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        self.alien_speed_factor = 0.10
        self.fleet_drop_speed = 30
        self.fleet_direction = 1

        self.ship_limit = 3

        self.speedup_scale = 1.15

        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 0.4
        self.bullet_speed_factor = 0.45
        self.alien_speed_factor = 0.15

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)