import pygame.font

class Score_Board():
    """A class to store score information"""
    def __init__(self, ai_settings, screen, stats):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.score_color = (0,255,0)
        self.high_score_color = (0, 0, 255)
        self.lvl_color = (255, 0, 255)
        self.font = pygame.font.SysFont("Ariel", 25)
        self.show_score()
        self.show_level()
        self.show_high_score()

    def show_score(self):
        """Render the text and show it as the score"""
        score_str = "Score"
        score_value = str(self.stats.score)
        # Score Text
        self.score_str_img = self.font.render(score_str, True, self.score_color)
        self.score_str_img_rect = self.score_str_img.get_rect()
        self.score_str_img_rect.right = self.screen_rect.right - 20
        self.score_str_img_rect.bottom = self.screen_rect.bottom - 30
        # Score Value
        self.score_value_img = self.font.render(score_value, True, self.score_color)
        self.score_value_img_rect = self.score_value_img.get_rect()
        self.score_value_img_rect.centerx = self.score_str_img_rect.centerx
        self.score_value_img_rect.bottom = self.screen_rect.bottom - 10
    
    def show_high_score(self):
        """Render the text and show it as the score"""
        high_score_str = "Highest Score"
        high_score_value = str(self.stats.high_score)
        # High Score Text
        self.high_score_str_img = self.font.render(high_score_str, True, self.high_score_color)
        self.high_score_str_img_rect = self.high_score_str_img.get_rect()
        self.high_score_str_img_rect.centerx = self.screen_rect.centerx
        self.high_score_str_img_rect.bottom = self.screen_rect.bottom - 30
        # High Score Value
        self.high_score_value_img = self.font.render(high_score_value, True, self.high_score_color)
        self.high_score_value_img_rect = self.high_score_value_img.get_rect()
        self.high_score_value_img_rect.centerx = self.high_score_str_img_rect.centerx
        self.high_score_value_img_rect.bottom = self.screen_rect.bottom - 10
    
    
    def show_level(self):
        """Render the text and show it as the lvl"""
        lvl_str = "Level"
        lvl_value = str(self.stats.lvl)
        # Level Text
        self.lvl_str_img = self.font.render(lvl_str, True, self.lvl_color)
        self.lvl_str_img_rect = self.lvl_str_img.get_rect()
        self.lvl_str_img_rect.right = self.screen_rect.right - 10
        self.lvl_str_img_rect.top = self.screen_rect.top + 10
        # Level Value
        self.lvl_value_img = self.font.render(lvl_value, True, self.lvl_color)
        self.lvl_value_img_rect = self.lvl_value_img.get_rect()
        self.lvl_value_img_rect.centerx = self.lvl_str_img_rect.centerx
        self.lvl_value_img_rect.top = self.screen_rect.top + 30


    def blit_score(self):
        """Draw the rendered image on the screen"""
        self.screen.blit(self.score_str_img, self.score_str_img_rect)
        self.screen.blit(self.score_value_img, self.score_value_img_rect)
        self.screen.blit(self.high_score_str_img, self.high_score_str_img_rect)
        self.screen.blit(self.high_score_value_img, self.high_score_value_img_rect)
        self.screen.blit(self.lvl_str_img, self.lvl_str_img_rect)
        self.screen.blit(self.lvl_value_img, self.lvl_value_img_rect)
