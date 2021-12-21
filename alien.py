import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A Class to create an alien"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and get its rect
        self.image = pygame.image.load('images/alien_1.bmp')
        self.rect = self.image.get_rect()

        # Place an alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def check_alien_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the aliens across the screen left right"""
        self.x = float(self.rect.x)
        self.x += (self.ai_settings.alien_speed_x * self.ai_settings.alien_direction)
        self.rect.x = self.x


    def blit_alien(self):
        """Draw the alien on the screen"""
        self.screen.blit(self.image, self.rect)