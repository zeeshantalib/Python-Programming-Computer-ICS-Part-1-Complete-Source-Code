import tkinter as tk
import random

# Constants
WIDTH = 600
HEIGHT = 400
BALL_SIZE = 20
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
BRICK_ROWS = 5
BRICK_COLS = 8
BRICK_WIDTH = WIDTH // BRICK_COLS
BRICK_HEIGHT = 20
SPEED = 4

class BrickBreakerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🧱 Brick Breaker Game")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#1f2937", highlightthickness=0)
        self.canvas.pack()

        self.dx = SPEED
        self.dy = -SPEED
        self.score = 0

        # Create paddle
        self.paddle = self.canvas.create_rectangle(250, HEIGHT - 40, 250 + PADDLE_WIDTH, HEIGHT - 40 + PADDLE_HEIGHT, fill="#34d399", outline="")

        # Create ball
        self.ball = self.canvas.create_oval(290, 250, 290 + BALL_SIZE, 250 + BALL_SIZE, fill="#facc15", outline="")

        # Create bricks
        self.bricks = []
        colors = ["#f87171", "#fb923c", "#facc15", "#4ade80", "#60a5fa"]
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                x1 = col * BRICK_WIDTH
                y1 = row * BRICK_HEIGHT
                x2 = x1 + BRICK_WIDTH
                y2 = y1 + BRICK_HEIGHT
                brick = self.canvas.create_rectangle(x1+2, y1+2, x2-2, y2-2, fill=colors[row % len(colors)], outline="")
                self.bricks.append(brick)

        # Controls
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        self.move_ball()

    def move_left(self, event):
        self.canvas.move(self.paddle, -20, 0)

    def move_right(self, event):
        self.canvas.move(self.paddle, 20, 0)

    def move_ball(self):
        self.canvas.move(self.ball, self.dx, self.dy)
        ball_coords = self.canvas.coords(self.ball)
        paddle_coords = self.canvas.coords(self.paddle)

        # Wall collisions
        if ball_coords[0] <= 0 or ball_coords[2] >= WIDTH:
            self.dx = -self.dx
        if ball_coords[1] <= 0:
            self.dy = -self.dy

        # Paddle collision
        if self.intersects(ball_coords, paddle_coords):
            self.dy = -self.dy

        # Brick collision
        for brick in self.bricks:
            if self.intersects(ball_coords, self.canvas.coords(brick)):
                self.canvas.delete(brick)
                self.bricks.remove(brick)
                self.dy = -self.dy
                self.score += 1
                break

        # Game over
        if ball_coords[3] >= HEIGHT:
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="🎮 Game Over", font=("Segoe UI", 24), fill="white")
            return

        # Win
        if not self.bricks:
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="🏆 You Win!", font=("Segoe UI", 24), fill="white")
            return

        self.root.after(15, self.move_ball)

    def intersects(self, a, b):
        return not (a[2] < b[0] or a[0] > b[2] or a[3] < b[1] or a[1] > b[3])

# Start game
root = tk.Tk()
game = BrickBreakerGame(root)
root.mainloop()
