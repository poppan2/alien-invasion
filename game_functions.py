import sys
import pygame

def check_events(ship):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        # Exit the game when the user clicks the game window's close button
        if event.type == pygame.QUIT:
            sys.exit()
        # If the arrow Keys are pressed, we move the ship
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right.
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                # Move the ship to the left
                ship.moving_left = True
        # When the arrow keys are released, we stop the movement
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen"""
    # Change the backround color of the screen 
    screen.fill(ai_settings.bg_color)

    # Draw the ship on screen
    ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()