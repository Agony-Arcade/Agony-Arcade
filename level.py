# level.py
import pygame

class Level:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.wall_width = None
        self.wall_height = None
        self.maze_matrix = None
        self.maze_walls = None

    def generate_level(self):
        # Define maze walls using a matrix (1 represents a wall, 0 represents an open path)
        self.maze_matrix = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        # Calculate wall dimensions based on the maze matrix
        self.wall_width = self.width // len(self.maze_matrix[0])
        self.wall_height = self.height // len(self.maze_matrix)

        # Create a list to store Rect objects representing walls
        self.maze_walls = []
        for row_index, row in enumerate(self.maze_matrix):
            for col_index, cell in enumerate(row):
                if cell == 1:
                    wall_rect = pygame.Rect(col_index * self.wall_width, row_index * self.wall_height,
                                            self.wall_width, self.wall_height)
                    self.maze_walls.append(wall_rect)

    def draw(self, screen):
        # Draw maze walls
        for wall in self.maze_walls:
            pygame.draw.rect(screen, (0, 0, 0), wall)

