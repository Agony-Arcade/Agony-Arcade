# main.py
import pygame
import sys
from character import Character
from level import Level

# Initialize Pygame
pygame.init()

# Window dimensions
width, height = 1000, 800

# Create the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Agony Arcade")

# Create a Character instance
ball = Character(50, 50, 5)

# Create a Level instance
level = Level(width, height, 3)
level.generate_level()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    ball.move(keys, level.maze_walls)

    # Draw on the screen
    screen.fill((255, 255, 255))  # Fill the screen with white color

    # Draw the level
    level.draw(screen)

    ball.draw(screen)  # Draw the character

    # Update the display
    pygame.display.flip()

    # Control the update speed
    pygame.time.Clock().tick(60)

