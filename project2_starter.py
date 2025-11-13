# ============================================================================ #
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================ #
class SimpleBattle:
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2

    def fight(self):
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()

        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)

        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================ #
# YOUR CLASSES
# ============================================================================ #
import random

class Character:
    def __init__(self, name, health, strength, magic):
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic

    def attack(self, target):
        damage = self.strength
        print(f"{self.name} attacks {target.name} for {damage} damage.")
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} now has {self.health} health.")

    def display_stats(self):
        print(f"Name: {self.name}, Health: {self.health}, Strength: {self.strength}, Magic: {self.magic}")

class Player(Character):
    def __init__(self, name, character_class, health, strength, magic):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0

    def display_stats(self):
        super().display_stats()
        print(f"Class: {self.character_class}, Level: {self.level}, EXP: {self.experience}")

class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, "Warrior", health=120, strength=15, magic=5)

    def attack(self, target):
        damage = self.strength + 5  # extra warrior damage
        print(f"{self.name} swings sword at {target.name} for {damage} damage.")
        target.take_damage(damage)

    def power_strike(self, target):
        damage = self.strength + 15
        print(f"{self.name} performs POWER STRIKE on {target.name} for {damage} damage!")
        target.take_damage(damage)

class Mage(Player):
    def __init__(self, name):
        super().__init__(name, "Mage", health=80, strength=8, magic=20)

    def attack(self, target):
        damage = self.magic
        print(f"{self.name} casts a spell on {target.name} for {damage} damage.")
        target.take_damage(damage)

    def fireball(self, target):
        damage = self.magic + 10
        print(f"{self.name} casts FIREBALL on {target.name} for {damage} damage!")
        target.take_damage(damage)

class Rogue(Player):
    def __init__(self, name):
        super().__init__(name, "Rogue", health=90, strength=12, magic=10)

    def attack(self, target):
        damage = self.strength
        if random.randint(1, 10) <= 3:  # 30% chance critical
            damage *= 2
            print(f"{self.name} lands a CRITICAL HIT on {target.name} for {damage} damage!")
        else:
            print(f"{self.name} attacks {target.name} for {damage} damage.")
        target.take_damage(damage)

    def sneak_attack(self, target):
        damage = self.strength * 2
        print(f"{self.name} performs SNEAK ATTACK on {target.name} for {damage} damage!")
        target.take_damage(damage)

class Weapon:
    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus

    def display_info(self):
        print(f"Weapon: {self.name}, Damage Bonus: {self.damage_bonus}")

# ============================================================================ #
# MAIN PROGRAM (FOR TESTING)
# ============================================================================ #
if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")

    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()

    print("\n⚔️ Testing Polymorphism:")
    dummy_target = Character("Target Dummy", 100, 0, 0)
    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 100

    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)
    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)

    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
    sword.display_info()
    staff.display_info()
    dagger.display_info()

    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()

    print("\n✅ Testing complete!")
