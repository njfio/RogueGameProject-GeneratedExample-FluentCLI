import random

# Game constants
MAP_WIDTH = 20
MAP_HEIGHT = 20
PLAYER_SYMBOL = '@'
ENEMY_SYMBOL = 'E'
ITEM_SYMBOL = 'i'

# Game variables
player_pos = [0, 0]
enemies = []
items = []

# Function to initialize the game
def init_game():
    # Place the player at a random position
    player_pos[0] = random.randint(0, MAP_WIDTH - 1)
    player_pos[1] = random.randint(0, MAP_HEIGHT - 1)

    # Generate random enemies
    num_enemies = random.randint(5, 10)
    for _ in range(num_enemies):
        enemy_pos = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]
        enemies.append(enemy_pos)

    # Generate random items
    num_items = random.randint(3, 7)
    for _ in range(num_items):
        item_pos = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]
        items.append(item_pos)

# Function to draw the game map
def draw_map():
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if [x, y] == player_pos:
                print(PLAYER_SYMBOL, end=' ')
            elif [x, y] in enemies:
                print(ENEMY_SYMBOL, end=' ')
            elif [x, y] in items:
                print(ITEM_SYMBOL, end=' ')
            else:
                print('.', end=' ')
        print()

# Function to handle player input
def handle_input():
    action = input("Enter an action (up, down, left, right): ")
    if action == 'up':
        player_pos[1] -= 1
    elif action == 'down':
        player_pos[1] += 1
    elif action == 'left':
        player_pos[0] -= 1
    elif action == 'right':
        player_pos[0] += 1

# Main game loop
def main_loop():
    init_game()
    while True:
        draw_map()
        handle_input()

        # TODO: Add game logic, collision detection, etc.

# Start the game
main_loop()
