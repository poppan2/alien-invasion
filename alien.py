import pygame

class Alien(pygame.sprite.Sprite):
    """A class to create aliens"""
    def __init__(self, ai_settings, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.ai_settings = ai_settings
        # Create an image of the block
        self.image = pygame.image.load('images/alien_1.bmp')
        self.rect = self.image.get_rect()

        # Place an alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def update(self):
        """Move the aliens across the screen left right"""
        self.x = float(self.rect.x)
        self.x += (self.ai_settings.alien_speed_x * self.ai_settings.alien_direction)
        self.rect.x = self.x

    def blit_alien(self):
        """Draw the alien on the screen"""
        self.screen.blit(self.image, self.rect)