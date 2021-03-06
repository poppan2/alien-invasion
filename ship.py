import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to create a Space Ship"""

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the ship image and get its rect.
        # pygame let us treat game elements like rectangles (rects)
        self.image = pygame.image.load('./images/Spaceship_1.bmp')
        # image rect
        self.rect = self.image.get_rect()
        # screen rect
        self.screen_rect = screen.get_rect()

        # Start a new ship at the bottom center of the screen
        # the x-coordinate & and y-coordinate of the ship's center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom - 50
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value
        # Check the position of the ship before changing the value
        # Stop moving right if the x-coordinate value has reached the right edge of the screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed
        # Stop moving left if the x-coordinate value has reached 0
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed
        # Stop moving up when the y-coordinate value reached half the screen height
        if self.moving_up and self.rect.top > (self.screen_rect.bottom/1.3):
            self.centery -= self.ai_settings.ship_speed
        # Stop moving down when the ship reaches the bottom of the screen
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom - 50:
            self.centery += self.ai_settings.ship_speed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def center(self):
        """Center the ship on the screen"""
        self.centerx = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom - 50
    def blit_ship(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) 