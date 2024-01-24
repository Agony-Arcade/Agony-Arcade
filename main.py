import pygame
import sys
import random
import time
from character import Character
from circle_enemy import CircleEnemy

# Initialize Pygame
pygame.init()

# Window dimensions
width, height = 1000, 800

# Create the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Agony Arcade")

# Create a Character instance
character = Character(width // 2, height // 2, 5)

# List to store enemies
num_enemies = 7
enemies = [CircleEnemy(random.randint(0, width), random.randint(0, height), 5) for _ in range(num_enemies)]

# Main loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    character.move(keys)

    # Move and check collisions for each enemy
    for enemy in enemies:
        enemy.move(character)

    # Check collisions after all enemies have moved
    collision = any(enemy.check_collision(character) for enemy in enemies)
    if collision:
        time.sleep(0.3)
        sys.exit()
    else:
        screen.fill((255, 255, 255))  # Fill the screen with white color

    # Draw character
    character.draw(screen)

    # Draw and update all enemies
    for enemy in enemies:
        enemy.draw(screen)

    # Update the display
    pygame.display.flip()

    # Control the update speed
    clock.tick(60)

