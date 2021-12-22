import pygame.font
class Play_Button():
    """A Class to create a play button"""
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width = 200
        self.height = 50
        self.color = (0,0,255)
        self.text_color = (255, 255, 255)
        self.text_font = pygame.font.SysFont("Arial", 25)
        # Create the button and center 
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # Render the text and center
        self.message_img = self.text_font.render("Play", True, self.text_color)
        self.message_img_rect = self.message_img.get_rect()
        self.message_img_rect.center = self.rect.center
        
    def draw_button_and_text(self):
        """Fill the button and draw text onto the screen"""
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.message_img, self.message_img_rect)
