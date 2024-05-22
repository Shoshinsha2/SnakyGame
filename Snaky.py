import random
import pygame

# Define constants
GRID_WIDTH = 30
GRID_HEIGHT = 20
CELL_SIZE = 20

# Define snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (0, -1)

    def move(self):
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def collides_with_self(self):
        return self.body[0] in self.body[1:]

    def collides_with_boundary(self):
        x, y = self.body[0]
        return x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT
    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0, 255, 0), (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Define food class
class Food:
    def __init__(self, snake):
        self.position = self.generate_position(snake)

    def generate_position(self, snake):
        while True:
            position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if position not in snake.body:
                return position

    def draw(self, screen):
        pygame.draw.rect(screen, pygame.Color(255, 0, 0), (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
