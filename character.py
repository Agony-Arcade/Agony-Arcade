# character.py
import pygame

class Character:
    def __init__(self, x, y, speed, radius=20, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius
        self.color = color
        self.momentum_x = 0
        self.momentum_y = 0
        self.friction = 0.90

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def move(self, keys, maze_walls):
        if keys[pygame.K_LEFT]:
            self.momentum_x = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.momentum_x = self.speed
        else:
            self.momentum_x *= self.friction

        if keys[pygame.K_UP]:
            self.momentum_y = -self.speed
        elif keys[pygame.K_DOWN]:
            self.momentum_y = self.speed
        else:
            self.momentum_y *= self.friction

        self.x += self.momentum_x
        self.y += self.momentum_y

        # Colisión con las paredes del laberinto
        self.handle_wall_collision(maze_walls)

    def handle_wall_collision(self, walls):
        for wall in walls:
            if self.get_rect().colliderect(wall):
                self.resolve_collision(wall)

    def resolve_collision(self, wall):
        overlap_x = max(0, min(self.x + self.radius, wall.right) - max(self.x - self.radius, wall.left))
        overlap_y = max(0, min(self.y + self.radius, wall.bottom) - max(self.y - self.radius, wall.top))

        if overlap_x > overlap_y:
            if self.y < wall.centery:
                self.y -= overlap_y
            else:
                self.y += overlap_y
            self.momentum_y = -self.momentum_y
        else:
            if self.x < wall.centerx:
                self.x -= overlap_x
            else:
                self.x += overlap_x
            self.momentum_x = -self.momentum_x

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)

