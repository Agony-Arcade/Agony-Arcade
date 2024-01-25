import pygame
import math
from enemy import Enemy

class CircleEnemy(Enemy):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, (255, 255, 0))  # Yellow color for circles
        self.speed = 3
        
    def draw(self, screen, camera_offset_x=0, camera_offset_y=0):
        pygame.draw.circle(screen, self.color, (int(self.x + camera_offset_x), int(self.y + camera_offset_y)), self.radius)

    def move(self, character, level):
        angle = math.atan2(character.y - self.y, character.x - self.x)
        move_x = self.speed * math.cos(angle)
        move_y = self.speed * math.sin(angle)

        new_rect = self.get_rect().move(move_x, move_y)

        if not level.is_wall_collision_rect(new_rect):
            # Si no hay colisión, moverse directamente hacia el objetivo
            self.x += move_x
            self.y += move_y
        else:

            if not level.is_wall_collision_rect(self.get_rect().move(move_x, 0)):
                self.x += move_x
            elif not level.is_wall_collision_rect(self.get_rect().move(0, move_y)):
                self.y += move_y
            else:

                if not level.is_wall_collision_rect(self.get_rect().move(0, -self.speed)):
                    self.y -= self.speed
                elif not level.is_wall_collision_rect(self.get_rect().move(0, self.speed)):
                    self.y += self.speed

                elif not level.is_wall_collision_rect(self.get_rect().move(-self.speed, 0)):
                    self.x -= self.speed
                elif not level.is_wall_collision_rect(self.get_rect().move(self.speed, 0)):
                    self.x += self.speed
                else:
                    pass

    def check_collision(self, character):
        distance = math.sqrt((character.x - self.x)**2 + (character.y - self.y)**2)
        if distance < self.radius + character.radius:
            return True
        return False

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)

