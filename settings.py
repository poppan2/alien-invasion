class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (100, 100, 100)
    
        # ship settings
        self.ship_lives = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_limit = 10

        # Alien settings
        self.alien_speed_y = 100
        self.alien_score = 50

        # Game SpeedUp settings
        self.speed_up_scale = 1.2
        self.score_up_scale = 1.5
        self.initial_speed()
    
    def initial_speed(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed_x = 10
        self.alien_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_speed_x *= self.speed_up_scale
        self.alien_score = int(self.alien_score * self.score_up_scale)
