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

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blit_alien(self):
        """Draw the alien on the screen"""
        self.screen.blit(self.image, self.rect)