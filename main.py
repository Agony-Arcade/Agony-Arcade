import pygame
import sys
import random
import time
from character import Character
from circle_enemy import CircleEnemy
from level import Level

# Initialize Pygame
pygame.init()

# Window dimensions
width, height = 1000, 800

# Create the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Agony Arcade")

# Create a Level instance
level = Level(width, height, 1)
level.generate_level()

# Generate enemies in valid positions
num_enemies = 1
enemies = []

# Create a Character instance
ball = Character(100, 100, 5)
ball.set_position(100, 100)

# Camera variables
camera_x = 0
camera_y = 0


def generate_enemy_positions(player_x, player_y, min_distance, num_enemies):
    enemy_positions = []
    for _ in range(num_enemies):
        valid_position = False
        while not valid_position:
            x = random.randint(0, width)
            y = random.randint(0, height)

            # Verificar si la posición es válida y no colisiona con las posiciones existentes de los enemigos
            if not level.is_wall_collision(x, y) and \
                    all(pygame.math.Vector2(x, y).distance_to(pygame.math.Vector2(enemy_x, enemy_y)) >= min_distance
                        for (enemy_x, enemy_y) in enemy_positions):
                valid_position = True

        enemy_positions.append((x, y))

        # Verificar si la nueva posición cumple con la distancia mínima respecto a los otros enemigos
        for i in range(len(enemy_positions) - 1):
            if pygame.math.Vector2(x, y).distance_to(pygame.math.Vector2(*enemy_positions[i])) < min_distance:
                valid_position = False
                enemy_positions.pop()  # Eliminar la posición si no cumple con la distancia mínima
                break

    return enemy_positions


enemy_positions = generate_enemy_positions(ball.x, ball.y, min_distance=20, num_enemies=num_enemies)
for pos in enemy_positions:
    enemies.append(CircleEnemy(pos[0], pos[1], 5))

# Main loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    ball.move(keys, level.maze_walls)

    # Check if the character is on the red zone
    if level.check_character_on_zone(ball.x, ball.y):
        if not level.maze_type == 3:
            level.maze_type += 1
            level.generate_level()

            # Reset enemy positions with minimum distance
            enemy_positions = generate_enemy_positions(ball.x, ball.y, min_distance=20, num_enemies=num_enemies)
            for i, pos in enumerate(enemy_positions):
                enemies[i].x = pos[0]
                enemies[i].y = pos[1]

        ball.set_position(100, 100)

    # Calculate the camera offset based on the ball's position
    camera_offset_x = width // 2 - ball.x
    camera_offset_y = height // 2 - ball.y

    # Move and check collisions for each enemy
    for enemy in enemies:
        enemy.move(ball, level)
        if level.is_wall_collision(enemy.x, enemy.y):
            # Ajusta la posición del enemigo si colisiona con un muro
            enemy.undo_move()

    # Check collisions after all enemies have moved
    collision = any(enemy.check_collision(ball) for enemy in enemies)
    if collision:
        time.sleep(0.3)
        sys.exit()
    else:
        screen.fill((255, 255, 255))  # Fill the screen with white color

    # Draw character with adjusted position based on camera offset
    ball.draw(screen, camera_offset_x, camera_offset_y)

    # Draw the level with adjusted position based on camera offset
    level.draw(screen, camera_offset_x, camera_offset_y)

    # Draw and update all enemies with adjusted position based on camera offset
    for enemy in enemies:
        enemy.draw(screen, camera_offset_x, camera_offset_y)

    # Update the display
    pygame.display.flip()

    # Control the update speed
    clock.tick(60)
