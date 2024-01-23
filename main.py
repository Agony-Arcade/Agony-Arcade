import pygame
import sys

# Initialize Pygame
pygame.init()

# Window dimensions
width, height = 1000, 800

# Create the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Agony Arcade")

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw on the screen
    screen.fill((255, 255, 255))  # Fill the screen with white color

    # Update the display
    pygame.display.flip()

    # Control the update speed
    pygame.time.Clock().tick(60)
