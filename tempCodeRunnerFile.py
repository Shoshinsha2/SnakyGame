me
import sys
from Snaky import Snake, Food

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")



# Set up snake
snake = Snake()

# Set up food
food = Food(snake)

# Set up game clock
clock = pygame.time.Clock()

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != (0, 1):
                snake.direction = (0, -1)
            if event.key == pygame.K_DOWN and snake.direction != (0, -1):
                snake.direction = (0, 1)
            if event.key == pygame.K_LEFT and snake.direction != (1, 0):
                snake.direction = (-1, 0)
            if event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                snake.direction = (1, 0)

    # Move snake
    snake.move()

    # Check for collision with food
    if snake.body[0] == food.position:
        snake.grow()
        food = Food(snake)
        # Move snake
        snake.move()

    # Check for game over
    if snake.collides_with_self() or snake.collides_with_boundary():
        while snake.health > 0