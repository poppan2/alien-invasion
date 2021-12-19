import sys
import pygame

def check_keydown_event(event, ship):
    """Respond to key press"""
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left
        ship.moving_left = True

def check_keyup_event(event, ship):
    """Respond to key release"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        # Exit the game when the user clicks the game window's close button
        if event.type == pygame.QUIT:
            sys.exit()
        # If the arrow Keys are pressed, we move the ship
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship)
        # When the arrow keys are released, we stop the movement
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen"""
    # Change the backround color of the screen 
    screen.fill(ai_settings.bg_color)

    # Draw the ship on screen
    ship.blitship()

    # Make the most recently drawn screen visible
    pygame.display.flip()