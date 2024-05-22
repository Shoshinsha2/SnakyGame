import random
import pygame

# Define constants
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
BORDER_SIZE = 2

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Define snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (0, -1)
        self.health = 100

    def move(self):
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()
        

    def grow(self):
        self.body.append(self.body[-1])
        print(self.body)

    def collides_with_self(self):
        return self.body[0] in self.body[1:]

    def collides_with_boundary(self):
        x, y = self.body[0]
        return x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Draw borders
        pygame.draw.rect(screen, BLACK, (0, 0, GRID_WIDTH * CELL_SIZE, BORDER_SIZE), BORDER_SIZE)
        pygame.draw.rect(screen, BLACK, (0, 0, BORDER_SIZE, GRID_HEIGHT * CELL_SIZE), BORDER_SIZE)
        pygame.draw.rect(screen, BLACK, (GRID_WIDTH * CELL_SIZE - BORDER_SIZE, 0, BORDER_SIZE, GRID_HEIGHT * CELL_SIZE), BORDER_SIZE)
        pygame.draw.rect(screen, BLACK, (0, GRID_HEIGHT * CELL_SIZE - BORDER_SIZE, GRID_WIDTH * CELL_SIZE, BORDER_SIZE), BORDER_SIZE)
        
    def life_bar(self, screen):
        pygame.draw.rect(screen, GREEN, (10, 10, self.health, 20))
        pygame.draw.rect(screen, RED, (10 + self.health, 10, 100 - self.health, 20))
        
    def game_over(self, screen):
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over", True, (255, 255, 255))
        screen.blit(text, (GRID_WIDTH * CELL_SIZE // 2 - text.get_width() // 2, GRID_HEIGHT * CELL_SIZE // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(2000)


        

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
        pygame.draw.rect(screen, RED, (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
