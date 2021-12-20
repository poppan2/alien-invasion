import sys
import pygame
from bullet import Bullet

def check_keydown_event(event, ai_settings, screen, ship, bullets):
    """Respond to key press"""
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        # Move the ship to the Up
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # Move the ship to the Down
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_event(event, ship):
    """Respond to key release"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        # Exit the game when the user clicks the game window's close button
        if event.type == pygame.QUIT:
            sys.exit()
        # If the arrow Keys are pressed, we move the ship
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        # When the arrow keys are released, we stop the movement
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)

def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen"""
    # Change the backround color of the screen 
    screen.fill(ai_settings.bg_color)

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Draw the ship on screen
    ship.blit_ship()

    # Make the most recently drawn screen visible
    pygame.display.flip()