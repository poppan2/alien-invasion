import sys
import pygame
from bullet import Bullet
from alien import Alien

def create_alien_fleet(ai_settings, screen, aliens):
    """Create a fleet of aliens"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    # Find out how many aliens can fit the screen across x-axis
    space_x = ai_settings.screen_width - (2 * alien_width)
    number_of_aliens = int(space_x/(2 * alien_width))
    # Create the first row of aliens
    for num_alien in range(number_of_aliens):
        alien = Alien(ai_settings, screen)
        alien.rect.x = alien_width * (1 + 2 * num_alien)
        aliens.add(alien)

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
        # Check if the length of bullets is less than the bullets limit
        if len(bullets) < ai_settings.bullets_limit:
            # Create a new bullet and add it to the bullets group
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
    # Create shortcut key for quitting the game
    elif event.key == pygame.K_q:
        sys.exit()

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

def update_screen(ai_settings, screen, ship, aliens,  bullets):
    """Update images on the screen and flip to the new screen"""
    # Change the backround color of the screen 
    screen.fill(ai_settings.bg_color)

    # Redraw the bullets on the screen
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Draw the ship on screen
    ship.blit_ship()
    # Draw the alien on the screen
    # aliens.draw(screen)
    for alien in aliens.sprites():
        alien.blit_alien()
    # Update the display surface to the screen
    pygame.display.flip()

def update_ship(ship):
    """Update the position of the ship"""
    ship.update()

def update_bullets(bullets):
    """Update the position of and remove the bullets"""
    # Update bullet position
    bullets.update()
    # Get rid of bullets that went out of screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)