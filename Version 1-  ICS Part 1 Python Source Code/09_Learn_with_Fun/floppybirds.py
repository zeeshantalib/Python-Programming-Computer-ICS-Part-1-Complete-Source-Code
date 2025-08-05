import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 400
HEIGHT = 600
FPS = 60

# Game settings
GRAVITY = 0.5
JUMP_STRENGTH = -10
PIPE_SPEED = 4
GAP_SIZE = 150

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
GREEN = (0, 200, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Floppy Bird")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 40)

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0
        self.radius = 20

    def jump(self):
        self.velocity = JUMP_STRENGTH

    def move(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 0), (self.x, int(self.y)), self.radius)

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2)

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = 60
        self.gap_y = random.randint(100, HEIGHT - 200)
    
    def move(self):
        self.x -= PIPE_SPEED

    def draw(self):
        top_rect = pygame.Rect(self.x, 0, self.width, self.gap_y)
        bottom_rect = pygame.Rect(self.x, self.gap_y + GAP_SIZE, self.width, HEIGHT)
        pygame.draw.rect(screen, GREEN, top_rect)
        pygame.draw.rect(screen, GREEN, bottom_rect)

    def get_rects(self):
        top_rect = pygame.Rect(self.x, 0, self.width, self.gap_y)
        bottom_rect = pygame.Rect(self.x, self.gap_y + GAP_SIZE, self.width, HEIGHT)
        return top_rect, bottom_rect

# Game loop
def main():
    bird = Bird()
    pipes = [Pipe(WIDTH + 100)]
    score = 0
    running = True

    while running:
        clock.tick(FPS)
        screen.fill(BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.jump()

        bird.move()
        bird.draw()

        # Update pipes
        for pipe in pipes:
            pipe.move()
            pipe.draw()

        # Add new pipes
        if pipes[-1].x < WIDTH - 200:
            pipes.append(Pipe(WIDTH))

        # Remove off-screen pipes
        if pipes[0].x + pipes[0].width < 0:
            pipes.pop(0)
            score += 1

        # Collision detection
        bird_rect = bird.get_rect()
        if bird.y > HEIGHT or bird.y < 0:
            main()  # Restart game on collision
        for pipe in pipes:
            top_rect, bottom_rect = pipe.get_rects()
            if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
                main()

        # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.update()

# Start game
main()
