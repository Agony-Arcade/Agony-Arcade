import pygame

class Level:
    def __init__(self, width, height, maze_type):
        self.width = width
        self.height = height
        self.wall_width = None
        self.wall_height = None
        self.maze_matrix = None
        self.maze_walls = None
        self.maze_type = maze_type

    def generate_level(self):
        if self.maze_type == 1:
            self.generate_maze_type1()
        elif self.maze_type == 2:
            self.generate_maze_type2()
        elif self.maze_type == 3:
            self.generate_maze_type3()

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

    def generate_maze_type1(self):
        # Maze layout for type 1
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

    def generate_maze_type2(self):
        # Maze layout for type 2
        self.maze_matrix = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def generate_maze_type3(self):
        # Maze layout for type 3
        self.maze_matrix = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def is_wall_collision(self, x, y):
        row = int(y // self.wall_height)
        col = int(x // self.wall_width)
        return self.maze_matrix[row][col] == 1

    def is_wall_collision_rect(self, rect):
        for wall in self.maze_walls:
            if rect.colliderect(wall):
                return True
        return False
