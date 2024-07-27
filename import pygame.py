import pygame
import sys
from datetime import datetime

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Digital Clock')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to draw text on the screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Get the current time
    current_time = datetime.now().strftime("%H:%M:%S")

    # Draw the time on the screen
    font = pygame.font.Font(None, 100)
    draw_text(current_time, font, WHITE, screen, WIDTH // 2, HEIGHT // 2)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
