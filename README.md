[# COMP 163 - Project 2: Character Abilities Showcase

**Name:** Matthew Solomon  
**Date:** [Insert Submission Date]  
**AI Usage:** AI assisted with inheritance structure and method overriding concepts.

---

## Overview

This project demonstrates:

- **Inheritance**: `Character` base class and `Player` subclasses (`Warrior`, `Mage`, `Rogue`).  
- **Polymorphism**: Same `attack()` method behaves differently for each subclass.  
- **Method Overriding**: Each player class overrides base methods to implement unique behavior.  
- **Special Abilities**:  
  - Warrior: `power_strike()`  
  - Mage: `fireball()`  
  - Rogue: `sneak_attack()`  
- **Composition**: Characters can have weapons (`Weapon` class) with damage bonuses.  
- **Battle System**: `SimpleBattle` class provided to simulate fights.

---

## Classes

### Character (Base Class)
- Attributes: `name`, `health`, `strength`, `magic`  
- Methods: `attack(target)`, `take_damage(damage)`, `display_stats()`

### Player (Subclass of Character)
- Adds `character_class` attribute.  
- Overrides `display_stats()` to include class information.

### Warrior, Mage, Rogue (Subclasses of Player)
- **Warrior**: High health and strength, low magic. Special ability: `power_strike()`.  
- **Mage**: Low health and strength, high magic. Special ability: `fireball()`.  
- **Rogue**: Medium health, strength, and magic. Special ability: `sneak_attack()`.

### Weapon
- Attributes: `name`, `damage_bonus`  
- Method: `display_info()`

---

## How to Run

1. Run `python project2_starter.py` to test characters, abilities, and the battle system.  
2. Example output includes character stats, attacks, special abilities, and a battle simulation.

---

## Testing

- All tests are included in the `tests` folder.  
- Run tests with `pytest` to confirm all functionality works.  
- ✅ All tests pass (53/53) in local testing.

---

## Notes

- This project follows the provided template and instructions from COMP 163 Project 2.  
- AI assistance was used only for guidance on inheritance and method overriding.  
 