import pygame
import sys
from pygame import mixer

# Define some colors
WHITE = (255, 255, 255)
GOLDEN = (218, 165, 32)

# Set the dimensions of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the title of the window
pygame.display.set_caption('Welcome to HALO')
icon = pygame.image.load('mcchelm.png')
pygame.display.set_icon(icon)

# Load the menu background image
background_image = pygame.image.load("background1.png").convert()

mixer.music.load("halotheme.mp3")
mixer.music.play()

# Create a font object
font = pygame.font.Font('Halo.ttf', 36)

# Create a font object with a green color
highlight_font = pygame.font.Font('Halo.ttf', 36)
highlight_color = (0, 255, 0)
highlight_button = highlight_font.render('Start HALO', True, highlight_color)

# Get the rect of the highlighted button and center it
highlight_rect = highlight_button.get_rect()
highlight_rect.centerx = SCREEN_WIDTH // 2
highlight_rect.centery = SCREEN_HEIGHT // 2 - 50

# Blit the highlighted button onto the screen
screen.blit(highlight_button, highlight_rect)

# Create the start button
start_button = font.render('Start HALO', True, GOLDEN)
start_rect = start_button.get_rect()
start_rect.centerx = SCREEN_WIDTH // 2
start_rect.centery = SCREEN_HEIGHT // 2 - 50

# Create the quit button
quit_button = font.render('Quit HALO', True, GOLDEN)
quit_rect = quit_button.get_rect()
quit_rect.centerx = SCREEN_WIDTH // 2
quit_rect.centery = SCREEN_HEIGHT // 2 + 50

# Create the HALO title
title_font = pygame.font.Font('Halo.ttf', 72)
title_color = GOLDEN
title_text = 'HALO'
title = title_font.render(title_text, True, title_color)
title_rect = title.get_rect()
title_rect.centerx = SCREEN_WIDTH // 2
title_rect.centery = SCREEN_HEIGHT // 4

# Create a variable to keep track of whether the game is running or not
game_running = False

# Start the menu loop
menu_running = True
while menu_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the start button was clicked
            if start_rect.collidepoint(event.pos):
                game_running = True
                menu_running = False
                mixer.music.stop() # Stop the music
            # Check if the quit button was clicked
            elif quit_rect.collidepoint(event.pos):
                menu_running = False
                pygame.quit()
                sys.exit()

    # Blit the menu background image onto the screen
    screen.blit(background_image, (0, 0))

    # Draw the start button, quit button, and HALO title
    screen.blit(start_button, start_rect)
    screen.blit(quit_button, quit_rect)
    screen.blit(title, title_rect)

    # Update the screen
    pygame.display.update()

# Start the game loop
while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            pygame.quit()
            sys.exit()

    # Fill the screen with white
    if __name__ == '__main__':
        import main

    # Draw objects here

    # Update the screen
    pygame.display.update()

# Quit the game
pygame.quit()
sys.exit()
