import random

# Player character stats
class Player:
    def __init__(self, name):
        self.name = name
        self.max_health = 100
        self.health = self.max_health
        self.attack_power = 10
        self.defense = 5

    def attack(self, target):
        damage = self.attack_power - target.defense
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage.")

# Monster generation
class Monster:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.max_health = 50 + (level * 10)
        self.health = self.max_health
        self.attack_power = 5 + (level * 2)
        self.defense = 2 + level

    def attack(self, target):
        damage = self.attack_power - target.defense
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage.")

def generate_monster(level):
    monster_names = ["Goblin", "Orc", "Troll", "Skeleton", "Zombie"]
    name = random.choice(monster_names)
    return Monster(name, level)

# Monster behaviors
def monster_action(monster, player):
    action = random.choice(["attack", "defend", "flee"])
    if action == "attack":
        monster.attack(player)
    elif action == "defend":
        monster.defense += 2
        print(f"{monster.name} defends and increases its defense.")
    else:
        print(f"{monster.name} tries to flee!")

# Game loop
def game_loop():
    player_name = input("Enter your character's name: ")
    player = Player(player_name)
    level = 1

    while True:
        print(f"\nLevel: {level}")
        print(f"{player.name}'s Health: {player.health}/{player.max_health}")

        monster = generate_monster(level)
        print(f"A {monster.name} appears!")

        while monster.health > 0:
            print(f"\n{monster.name}'s Health: {monster.health}/{monster.max_health}")
            action = input("Enter your action (attack/flee): ")

            if action == "attack":
                player.attack(monster)
            else:
                print(f"{player.name} tries to flee!")
                break

            if monster.health > 0:
                monster_action(monster, player)

            if player.health <= 0:
                print(f"\n{player.name} has been defeated. Game over!")
                return

        print(f"\n{monster.name} has been defeated!")
        level += 1
        player.max_health += 20
        player.health = player.max_health
        player.attack_power += 2
        player.defense += 1

# Start the game
game_loop()
