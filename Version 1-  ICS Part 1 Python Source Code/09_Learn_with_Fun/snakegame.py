import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Game variables
snake_block = 20
snake_speed = 10

font_style = pygame.font.SysFont("Segoe UI", 25)
score_font = pygame.font.SysFont("Segoe UI", 30)

clock = pygame.time.Clock()

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])

def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [x, y])

def gameLoop():
    game_over = False
    game_close = False

    x1 = WIDTH // 2
    y1 = HEIGHT // 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, HEIGHT - snake_block) / snake_block) * snake_block

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("You Lost! Press C-Play Again or Q-Quit", RED, WIDTH / 6, HEIGHT / 3)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)

        pygame.draw.rect(screen, RED, [foodx, foody, snake_block, snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if snake hits itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)

        # Show score
        score = length_of_snake - 1
        value = score_font.render("Score: " + str(score), True, WHITE)
        screen.blit(value, [0, 0])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, HEIGHT - snake_block) / snake_block) * snake_block
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

if __name__ == "__main__":
    gameLoop()
