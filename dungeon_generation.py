import random

# Constants
DUNGEON_WIDTH = 50
DUNGEON_HEIGHT = 30
ROOM_MIN_SIZE = 5
ROOM_MAX_SIZE = 10
MAX_ROOMS = 15
MAX_TRAPS = 5
MAX_SECRETS = 3

# Dungeon tile types
EMPTY = ' '
WALL = '#'
FLOOR = '.'
TRAP = '^'
SECRET = '?'

# Room class
class Room:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

# Generate a random dungeon map
def generate_dungeon():
    dungeon = [[WALL] * DUNGEON_WIDTH for _ in range(DUNGEON_HEIGHT)]
    rooms = []

    # Generate rooms
    for _ in range(MAX_ROOMS):
        width = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        height = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        x = random.randint(1, DUNGEON_WIDTH - width - 1)
        y = random.randint(1, DUNGEON_HEIGHT - height - 1)

        new_room = Room(x, y, width, height)

        # Check if the new room overlaps with existing rooms
        if any(room_intersects(new_room, room) for room in rooms):
            continue

        # Carve out the room in the dungeon
        for i in range(y, y + height):
            for j in range(x, x + width):
                dungeon[i][j] = FLOOR

        # Add the room to the list
        rooms.append(new_room)

    # Connect rooms with tunnels
    for i in range(len(rooms) - 1):
        current_room = rooms[i]
        next_room = rooms[i + 1]

        # Randomly choose a starting point in the current room
        start_x = random.randint(current_room.x + 1, current_room.x + current_room.width - 2)
        start_y = random.randint(current_room.y + 1, current_room.y + current_room.height - 2)

        # Randomly choose an ending point in the next room
        end_x = random.randint(next_room.x + 1, next_room.x + next_room.width - 2)
        end_y = random.randint(next_room.y + 1, next_room.y + next_room.height - 2)

        # Carve out the tunnel
        carve_tunnel(dungeon, start_x, start_y, end_x, end_y)

    # Place traps randomly
    for _ in range(MAX_TRAPS):
        place_trap(dungeon, rooms)

    # Place secrets randomly
    for _ in range(MAX_SECRETS):
        place_secret(dungeon, rooms)

    return dungeon

# Check if two rooms intersect
def room_intersects(room1, room2):
    return (
        room1.x <= room2.x + room2.width and
        room1.x + room1.width >= room2.x and
        room1.y <= room2.y + room2.height and
        room1.y + room1.height >= room2.y
    )

# Carve a tunnel between two points
def carve_tunnel(dungeon, x1, y1, x2, y2):
    # Determine the direction of the tunnel
    if random.random() < 0.5:
        # Carve horizontally, then vertically
        carve_horizontal_tunnel(dungeon, x1, x2, y1)
        carve_vertical_tunnel(dungeon, y1, y2, x2)
    else:
        # Carve vertically, then horizontally
        carve_vertical_tunnel(dungeon, y1, y2, x1)
        carve_horizontal_tunnel(dungeon, x1, x2, y2)

# Carve a horizontal tunnel
def carve_horizontal_tunnel(dungeon, x1, x2, y):
    for x in range(min(x1, x2), max(x1, x2) + 1):
        dungeon[y][x] = FLOOR

# Carve a vertical tunnel
def carve_vertical_tunnel(dungeon, y1, y2, x):
    for y in range(min(y1, y2), max(y1, y2) + 1):
        dungeon[y][x] = FLOOR

# Place a trap in a random location
def place_trap(dungeon, rooms):
    room = random.choice(rooms)
    x = random.randint(room.x + 1, room.x + room.width - 2)
    y = random.randint(room.y + 1, room.y + room.height - 2)
    dungeon[y][x] = TRAP

# Place a secret in a random location
def place_secret(dungeon, rooms):
    room = random.choice(rooms)
    x = random.randint(room.x + 1, room.x + room.width - 2)
    y = random.randint(room.y + 1, room.y + room.height - 2)
    dungeon[y][x] = SECRET

# Print the dungeon map
def print_dungeon(dungeon):
    for row in dungeon:
        print(''.join(row))

# Generate and print the dungeon map
dungeon = generate_dungeon()
print_dungeon(dungeon)
