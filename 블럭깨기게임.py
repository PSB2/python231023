#cmd
#pip install pygame
import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
BLOCK_WIDTH, BLOCK_HEIGHT = 80, 30
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Block Breaking Game")

# Game variables
ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
ball_radius = 10
ball_velocity = [5, 5]

paddle_pos = [(SCREEN_WIDTH - PADDLE_WIDTH) // 2, SCREEN_HEIGHT - PADDLE_HEIGHT - 10]

block_rows = 5
block_cols = SCREEN_WIDTH // BLOCK_WIDTH
blocks = []
for row in range(block_rows):
    for col in range(block_cols):
        block = pygame.Rect(col * BLOCK_WIDTH, row * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
        blocks.append(block)

clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_pos[0] > 0:
        paddle_pos[0] -= 5
    if keys[pygame.K_RIGHT] and paddle_pos[0] < SCREEN_WIDTH - PADDLE_WIDTH:
        paddle_pos[0] += 5

    # Update ball position
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Ball and wall collisions
    if ball_pos[0] <= ball_radius or ball_pos[0] >= SCREEN_WIDTH - ball_radius:
        ball_velocity[0] = -ball_velocity[0]
    if ball_pos[1] <= ball_radius:
        ball_velocity[1] = -ball_velocity[1]

    # Ball and paddle collision
    if ball_pos[1] >= SCREEN_HEIGHT - ball_radius - PADDLE_HEIGHT and \
       paddle_pos[0] <= ball_pos[0] <= paddle_pos[0] + PADDLE_WIDTH:
        ball_velocity[1] = -ball_velocity[1]

    # Ball and block collisions
    for block in blocks:
        if block.colliderect(pygame.Rect(ball_pos[0] - ball_radius, ball_pos[1] - ball_radius, ball_radius * 2, ball_radius * 2)):
            blocks.remove(block)
            ball_velocity[1] = -ball_velocity[1]
            break

    # Clear the screen
    screen.fill(WHITE)

    # Draw blocks
    for block in blocks:
        pygame.draw.rect(screen, BLUE, block)

    # Draw paddle
    pygame.draw.rect(screen, BLUE, pygame.Rect(paddle_pos[0], paddle_pos[1], PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw ball
    pygame.draw.circle(screen, BLUE, (ball_pos[0], ball_pos[1]), ball_radius)

    # Update the display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)
