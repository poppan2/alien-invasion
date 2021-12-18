import sys
import pygame
from settings import Settings

def run_game():
    # Initialize pygame, settings and a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Start the main Loop for the game
    while True:
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            # Exit the game when the user clicks the game window's close button
            if event.type == pygame.QUIT:
                sys.exit()
            # Change the backround color of the screen
            screen.fill(ai_settings.bg_color)
            # Make the most recently drawn screen visible
            pygame.display.flip()

run_game()