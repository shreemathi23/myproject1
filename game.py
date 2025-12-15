import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Blocks")

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 50, 50)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

# Player
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - 70
player_speed = 7

# Enemy
enemy_size = 50
enemy_x = random.randint(0, WIDTH - enemy_size)
enemy_y = -enemy_size
enemy_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 40)

def show_score(value):
    text = font.render(f"Score: {value}", True, BLACK)
    screen.blit(text, (10, 10))

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Enemy movement
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -enemy_size
        enemy_x = random.randint(0, WIDTH - enemy_size)
        score += 1
        enemy_speed += 0.2  # increase difficulty

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)

    if player_rect.colliderect(enemy_rect):
        running = False

    # Draw objects
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, enemy_rect)
    show_score(score)

    pygame.display.update()

# Game over screen
screen.fill(WHITE)
game_over_text = font.render("Game Over!", True, RED)
screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
pygame.display.update()
pygame.time.delay(2000)

pygame.quit()
