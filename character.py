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
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self, keys):
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
