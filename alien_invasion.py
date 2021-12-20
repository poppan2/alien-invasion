import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

    # Initialize pygame, settings and a screen object
    pygame.init()
    ai_settings = Settings()
    # Initialize a window or screen for display
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # Set the current window caption
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings,screen)

    # Make a group to store bullets in
    bullets = Group()

    # Start the main Loop for the game
    while True:
        gf.check_events(ai_settings, screen,ship, bullets)
        gf.update_ship(ship)
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()