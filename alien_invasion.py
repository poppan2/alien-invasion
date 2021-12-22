import pygame
from pygame.sprite import Group
from settings import Settings
from stats import Game_Stats
from ship import Ship
from button import Play_Button
from score import Score_Board
import game_functions as gf

def run_game():

    # Initialize pygame, settings and a screen object
    pygame.init()
    ai_settings = Settings()
    # Initialize a window or screen for display
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # Set the current window caption
    pygame.display.set_caption("Alien Invasion")
    # Make the play button
    play_button = Play_Button(screen)
    # Make a stats object
    stats = Game_Stats(ai_settings)
    # Make a ship object
    ship = Ship(ai_settings,screen)
    # Make a group to store bullets in
    bullets = Group()
    # Make a group to store aliens in
    aliens = Group()
    # Make a score board
    score_board = Score_Board(ai_settings, screen, stats)
    gf.create_alien_fleet(ai_settings, screen, aliens, ship)
    # Start the main Loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets, play_button, stats, aliens)
        if stats.run_game:
            gf.update_ship(ship)
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens, stats, score_board)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, play_button, stats, score_board)

run_game()