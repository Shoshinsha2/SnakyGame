import pygame
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
        snake.health -= 10
        if snake.health <= 0:
            snake.game_over(screen)
            pygame.quit()
            sys.exit()
        else:
            snake.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
            snake.direction = (0, -1)
    else:
        new_head = (snake.body[0][0] + snake.direction[0], snake.body[0][1] + snake.direction[1])
        snake.body.insert(0, new_head)
        snake.body.pop()


    # Draw everything
    screen.fill((255, 255, 255))
    snake.draw(screen)
    food.draw(screen)
    snake.life_bar(screen)

    pygame.display.flip()

    # Wait for next frame
    clock.tick(10)
