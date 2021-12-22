import pygame.font

class Score_Board():
    """A class to store score information"""
    def __init__(self, ai_settings, screen, stats):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.color = (0,255,0)
        self.font = pygame.font.SysFont("Ariel", 25)
        self.show_score()

    def show_score(self):
        """Render the text and show it as the score"""
        score_str = str(self.stats.score)
        self.score_img = self.font.render(score_str, True, self.color)
        self.score_img_rect = self.score_img.get_rect()
        self.score_img_rect.right = self.screen_rect.right - 20
        self.score_img_rect.top = 20
    
    def blit_score(self):
        """Draw the rendered image on the screen"""
        self.screen.blit(self.score_img, self.score_img_rect)
