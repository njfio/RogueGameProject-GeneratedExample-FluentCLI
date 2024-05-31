import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Rogue-like Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load sprite images
player_image = pygame.image.load("player.png")
enemy_image = pygame.image.load("enemy.png")
wall_image = pygame.image.load("wall.png")

# Define sprite classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (window_width // 2, window_height // 2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_A]:
            self.rect.x -= 5
        if keys[pygame.K_D]:
            self.rect.x += 5
        if keys[pygame.K_W]:
            self.rect.y -= 5
        if keys[pygame.K_S]:
            self.rect.y += 5

        # Keep the player within the screen boundaries
        self.rect.clamp_ip(window.get_rect())

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, window_width - self.rect.width)
        self.rect.y = random.randint(0, window_height - self.rect.height)

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = wall_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Create sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
walls = pygame.sprite.Group()

# Create player sprite
player = Player()
all_sprites.add(player)

# Create enemy sprites
for _ in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Create wall sprites
for _ in range(10):
    wall_x = random.randint(0, window_width - wall_image.get_width())
    wall_y = random.randint(0, window_height - wall_image.get_height())
    wall = Wall(wall_x, wall_y)
    all_sprites.add(wall)
    walls.add(wall)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update sprites
    all_sprites.update()

    # Check for collisions
    if pygame.sprite.spritecollide(player, enemies, False):
        # Handle collision with enemies
        pass

    if pygame.sprite.spritecollide(player, walls, False):
        # Handle collision with walls
        pass

    # Clear the screen
    window.fill(BLACK)

    # Draw sprites
    all_sprites.draw(window)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
