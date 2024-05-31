import random

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

class Weapon(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage

class Consumable(Item):
    def __init__(self, name, description, effect):
        super().__init__(name, description)
        self.effect = effect

class Player:
    def __init__(self, name, health, base_damage):
        self.name = name
        self.health = health
        self.base_damage = base_damage
        self.inventory = []
        self.equipped_weapon = None

    def attack(self, enemy):
        damage = self.base_damage
        if self.equipped_weapon:
            damage += self.equipped_weapon.damage
        enemy.health -= damage
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")

    def equip_weapon(self, weapon):
        if weapon in self.inventory:
            self.equipped_weapon = weapon
            print(f"{self.name} equips {weapon.name}.")
        else:
            print(f"{weapon.name} is not in the inventory.")

    def use_item(self, item):
        if item in self.inventory:
            if isinstance(item, Consumable):
                self.health += item.effect
                self.inventory.remove(item)
                print(f"{self.name} uses {item.name} and gains {item.effect} health.")
            else:
                print(f"{item.name} is not a consumable item.")
        else:
            print(f"{item.name} is not in the inventory.")

    def combine_items(self, item1, item2):
        if item1 in self.inventory and item2 in self.inventory:
            # Define item combination logic here
            # Example: Create a new item based on the combination
            new_item = Item("Combined Item", "A powerful combined item.")
            self.inventory.remove(item1)
            self.inventory.remove(item2)
            self.inventory.append(new_item)
            print(f"{self.name} combines {item1.name} and {item2.name} to create {new_item.name}.")
        else:
            print("One or both items are not in the inventory.")

class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, player):
        player.health -= self.damage
        print(f"{self.name} attacks {player.name} for {self.damage} damage!")

# Example usage
player = Player("Hero", 100, 10)
enemy = Enemy("Goblin", 50, 5)

sword = Weapon("Sword", "A sharp sword.", 15)
potion = Consumable("Health Potion", "Restores 20 health.", 20)

player.inventory.append(sword)
player.inventory.append(potion)

player.equip_weapon(sword)
player.attack(enemy)
enemy.attack(player)

player.use_item(potion)

item1 = Item("Item 1", "The first item.")
item2 = Item("Item 2", "The second item.")
player.inventory.append(item1)
player.inventory.append(item2)
player.combine_items(item1, item2)
