import sys
import pygame

def check_events():
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        # Exit the game when the user clicks the game window's close button
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen"""
    # Change the backround color of the screen 
    screen.fill(ai_settings.bg_color)
    
    # Draw the ship on screen
    ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()