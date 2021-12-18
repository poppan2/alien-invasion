import pygame

class Ship():
    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        # Load the ship image and get its rect.
        # pygame let us treat game elements like rectangles (rects)
        self.image = pygame.image.load('./images/Spaceship_1.bmp')
        # image rect
        self.rect = self.image.get_rect()
        # screen rect
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        # the x-coordinate of the ship's center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) 