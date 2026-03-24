import pygame
import constants

class ScoreDisplay(pygame.sprite.Sprite):
    """Display the current score at the bottom middle of the screen."""
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.font_size = 36
        self.color = (255, 255, 255)
        self.position = pygame.Vector2(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT - 30)
        self._font = None
    
    @property
    def font(self):
        """Lazy-load font to ensure pygame.font is initialized."""
        if self._font is None:
            self._font = pygame.font.Font(None, self.font_size)
        return self._font
        
    def update_score(self, points):
        """Update the current score by the given points."""
        self.score += points
        
    def draw(self, screen):
        """Draw the score on the screen."""
        score_text = f"Score: {self.score}"
        text_surface = self.font.render(score_text, True, self.color)
        text_rect = text_surface.get_rect(center=(self.position.x, self.position.y))
        screen.blit(text_surface, text_rect)

class ScorePopup(pygame.sprite.Sprite):
    """Visual feedback showing score increase at asteroid hit location."""
    
    def __init__(self, x, y, points):
        super().__init__()
        self.points = points
        self.font_size = 24
        self.color = (255, 255, 0)  # Yellow color for popups
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, -50)  # Move upward
        self.lifetime = 1.0  # 1 second lifetime
        self.timer = 0
        self.alpha = 255  # Start fully opaque
        self._font = None
    
    @property
    def font(self):
        """Lazy-load font to ensure pygame.font is initialized."""
        if self._font is None:
            self._font = pygame.font.Font(None, self.font_size)
        return self._font
        
    def update(self, dt):
        """Update popup position and animation."""
        self.timer += dt
        self.position += self.velocity * dt
        
        # Fade out over time
        self.alpha = max(0, int(255 * (1 - (self.timer / self.lifetime))))
        
        # Remove when lifetime expires
        if self.timer >= self.lifetime:
            self.kill()
            
    def draw(self, screen):
        """Draw the score popup with transparency."""
        if self.alpha <= 0:
            return
            
        popup_text = f"+{self.points}"
        text_surface = self.font.render(popup_text, True, self.color)
        text_surface.set_alpha(self.alpha)
        text_rect = text_surface.get_rect(center=(int(self.position.x), int(self.position.y)))
        screen.blit(text_surface, text_rect)