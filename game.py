import random
import time
from enum import Enum

class Mount(Enum):
    MOOSE = 1
    HORSE = 2
    CARIBOU = 3

class Character:
    def __init__(self, name, mount):
        self.name = name
        self.mount = mount
        self.health = 100
        self.max_health = 100
        self.attack_power = 0
        self.defense = 0
        self.experience = 0
        self.level = 1
        
        # Mount bonuses
        if mount == Mount.MOOSE:
            self.attack_power = 18
            self.defense = 8
            self.health = 120
            self.max_health = 120
            self.mount_name = "Moose"
            self.speed = 7
        elif mount == Mount.HORSE:
            self.attack_power = 15
            self.defense = 6
            self.health = 100
            self.max_health = 100
            self.mount_name = "Horse"
            self.speed = 9
        elif mount == Mount.CARIBOU:
            self.attack_power = 12
            self.defense = 10
            self.health = 110
            self.max_health = 110
            self.mount_name = "Caribou"
            self.speed = 8
    
    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense // 2)
        self.health -= actual_damage
        return actual_damage
    
    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)
    
    def is_alive(self):
        return self.health > 0
    
    def level_up(self):
        self.level += 1
        self.max_health += 10
        self.health = self.max_health
        self.attack_power += 5
        self.defense += 2
    
    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= self.level * 100:
            self.level_up()
            self.experience = 0
    
    def __str__(self):
        return f"{self.name} (Level {self.level}) - {self.mount_name}\nHP: {self.health}/{self.max_health} | ATK: {self.attack_power} | DEF: {self.defense}"

class Enemy:
    def __init__(self, name, health, attack, defense, experience_reward):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defense = defense
        self.experience_reward = experience_reward
    
    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense // 2)
        self.health -= actual_damage
        return actual_damage
    
    def is_alive(self):
        return self.health > 0
    
    def __str__(self):
        return f"{self.name} - HP: {self.health}/{self.max_health}"

class Game:
    def __init__(self):
        self.characters = []
        self.lands_conquered = 0
        self.current_region = "Starting Camp"
        self.turn = 0
        self.game_over = False
        self.story_progress = 0
        
    def setup_characters(self):
        print("\n" + "="*60)
        print("MOUNTAIN RISE: A Legend of the Russian Mountains")
        print("="*60)
        print("\nYou begin your journey in the Siberian Mountains with three warriors.")
        print("Choose your primary character:\n")
        print("1. Ride a MOOSE (High HP, High Attack, Slower)")
        print("2. Ride a HORSE (Balanced, Fast)")
        print("3. Ride a CARIBOU (High Defense, Energy Efficient)")
        
        choice = input("\nSelect (1-3): ").strip()
        
        mount_choice = int(choice) if choice in ['1', '2', '3'] else 1
        mount_map = {1: Mount.MOOSE, 2: Mount.HORSE, 3: Mount.CARIBOU}
        
        player_name = input("Enter your character's name: ").strip() or "Warrior"
        
        self.characters.append(Character(player_name, mount_map[mount_choice]))
        self.characters.append(Character("Aleksandr", Mount.HORSE if mount_choice != 2 else Mount.MOOSE))
        self.characters.append(Character("Temüjin", Mount.CARIBOU if mount_choice != 3 else Mount.MOOSE))
        
        print("\n" + "="*60)
        for char in self.characters:
            print(char)
        print("="*60)
    
    def get_enemy_encounter(self, region):
        """Generate enemy based on region"""
        encounters = {
            "Siberian Pass": [
                Enemy("Mountain Bandit", 40, 12, 3, 50),
                Enemy("Cossack Raider", 50, 14, 4, 75),
                Enemy("Pirate Scout", 35, 10, 2, 40),
            ],
            "Mongolian Plateau": [
                Enemy("Mongol Warrior", 55, 16, 5, 100),
                Enemy("Nomadic Archer", 45, 18, 3, 90),
                Enemy("Steppe Warlord", 70, 20, 6, 150),
            ],
            "Ural Mountains": [
                Enemy("Mountain Shaman", 50, 15, 4, 85),
                Enemy("Yak Herder", 60, 13, 5, 95),
                Enemy("Avalanche Summoner", 65, 17, 6, 120),
            ],
            "Lake Baikal": [
                Enemy("Ice Wizard", 55, 19, 3, 110),
                Enemy("Fish Merchant", 40, 11, 2, 60),
                Enemy("Frost Giant", 80, 22, 7, 160),
            ],
            "Altai Mountains": [
                Enemy("Golden Eagle Knight", 65, 18, 6, 130),
                Enemy("Wolf Pack Leader", 55, 20, 4, 115),
                Enemy("Black Dragon Guardian", 100, 25, 8, 200),
            ]
        }
        return random.choice(encounters.get(region, encounters["Siberian Pass"]))
    
    def combat(self, player_char, enemy):
        """Handle turn-based combat"""
        print(f"\n{'='*60}")
        print(f"⚔️  BATTLE: {player_char.name} ({player_char.mount_name}) vs {enemy.name}")
        print(f"{'='*60}\n")
        
        round_num = 0
        while player_char.is_alive() and enemy.is_alive():
            round_num += 1
            print(f"\n--- ROUND {round_num} ---")
            print(f"{player_char.name}: {player_char.health}/{player_char.max_health} HP")
            print(f"{enemy.name}: {enemy.health}/{enemy.max_health} HP\n")
            
            print("Your turn! Actions:")
            print("1. ⚔️  Attack - Strike with your weapon")
            print("2. 🛡️  Defend - Brace for impact") 
            print("3. 🍃 Heal - Use medicinal herbs")
            
            action = input("Choose (1-3): ").strip()
            
            # Player turn
            if action == "1":
                # Check for critical hit
                crit_chance = random.random()
                damage = random.randint(int(player_char.attack_power * 0.8), int(player_char.attack_power * 1.2))
                
                if crit_chance < 0.15:  # 15% crit chance
                    damage = int(damage * 1.5)
                    actual_damage = enemy.take_damage(damage)
                    print(f"\n⚡ CRITICAL HIT! You strike for {actual_damage} damage!")
                else:
                    actual_damage = enemy.take_damage(damage)
                    print(f"\n✓ You strike for {actual_damage} damage!")
            elif action == "2":
                player_char.defense += 3
                print(f"\n✓ You brace yourself! Defense increased temporarily.")
            elif action == "3":
                heal_amount = 30
                player_char.heal(heal_amount)
                print(f"\n🍃 You use medicinal herbs and recover {heal_amount} HP!")
            else:
                print("\nYou hesitate...")
            
            if not enemy.is_alive():
                break
            
            # Enemy turn
            print(f"\n{enemy.name} counters!")
            enemy_damage = random.randint(int(enemy.attack * 0.7), int(enemy.attack * 1.3))
            actual_damage = player_char.take_damage(enemy_damage)
            print(f"→ You take {actual_damage} damage!")
            
            time.sleep(0.5)
        
        print(f"\n{'='*60}")
        if player_char.is_alive():
            print(f"✓ VICTORY! {player_char.name} defeated {enemy.name}!")
            experience_gained = enemy.experience_reward
            player_char.gain_experience(experience_gained)
            print(f"⭐ Gained {experience_gained} experience!")
            if player_char.level > 1:
                print(f"🎉 Level UP! Now level {player_char.level}!")
            self.lands_conquered += 1
            return True
        else:
            print(f"✗ DEFEAT! {player_char.name} has fallen in battle...")
            return False
    
    def travel(self):
        """Travel to a new region"""
        regions = ["Siberian Pass", "Mongolian Plateau", "Ural Mountains", "Lake Baikal", "Altai Mountains"]
        region_descriptions = {
            "Siberian Pass": "A narrow mountain pass with jagged peaks towering above...",
            "Mongolian Plateau": "Vast open plains stretching to the horizon...",
            "Ural Mountains": "Ancient mountains shrouded in mist...",
            "Lake Baikal": "The crystalline waters of the world's deepest lake...",
            "Altai Mountains": "The legendary home of dragons and warriors..."
        }
        
        print("\n" + "="*60)
        print("Choose your next destination:")
        for i, region in enumerate(regions, 1):
            print(f"{i}. {region}")
        
        choice = input("Select (1-5): ").strip()
        choice_idx = int(choice) - 1 if choice in ['1', '2', '3', '4', '5'] else 0
        
        self.current_region = regions[choice_idx]
        self.turn += 1
        
        print(f"\nYour party rides toward {self.current_region}...")
        print(f"{region_descriptions[self.current_region]}")
        time.sleep(2)
        
        # Random encounter
        if random.random() < 0.7:  # 70% chance of combat
            enemy = self.get_enemy_encounter(self.current_region)
            print(f"\n⚔️  An enemy appears: {enemy.name}!")
            time.sleep(1)
            
            # Combat with main character
            if self.combat(self.characters[0], enemy):
                print(f"\n✓ You have conquered {self.lands_conquered} territories!")
            else:
                self.game_over = True
        else:
            print("Your passage is peaceful and you rest well.")
            # Heal characters
            for char in self.characters:
                char.heal(20)
            print("All party members recover 20 HP.")
    
    def show_status(self):
        """Display party status"""
        print("\n" + "="*60)
        print(f"TURN {self.turn} | Region: {self.current_region}")
        print(f"Territories Conquered: {self.lands_conquered}/20")
        print("="*60)
        for i, char in enumerate(self.characters, 1):
            status = "🟩" if char.health > char.max_health * 0.7 else "🟨" if char.health > char.max_health * 0.3 else "🟥"
            print(f"\n[{i}] {char.name}")
            print(f"    Mount: {char.mount_name} | Level: {char.level}")
            print(f"    HP: {char.health}/{char.max_health} {status}")
            print(f"    ATK: {char.attack_power} | DEF: {char.defense} | EXP: {char.experience}/{char.level * 100}")
        print()
    
    def save_game(self):
        """Save progress"""
        print(f"Game saved! You have conquered {self.lands_conquered} territories.")
    
    def show_victory(self):
        """Show victory screen"""
        print("\n" + "="*60)
        print("CONGRATULATIONS! MOUNTAIN RISE COMPLETE!")
        print("="*60)
        print(f"\nYou conquered {self.lands_conquered} territories!")
        for char in self.characters:
            print(f"{char.name}: Level {char.level}")
        print("\nYour legend spreads across the Russian Mountains!")
        print("="*60 + "\n")
    
    def run(self):
        """Main game loop"""
        self.setup_characters()
        
        while not self.game_over and self.turn < 20:
            self.show_status()
            
            print("What do you do?")
            print("1. 🏔️  Travel to new region")
            print("2. 🏕️  Rest and heal")
            print("3. 📊 View detailed stats")
            print("4. 💾 Save game")
            print("5. 🚪 Quit")
            
            choice = input("\nChoose (1-5): ").strip()
            
            if choice == "1":
                self.travel()
            elif choice == "2":
                for char in self.characters:
                    char.heal(50)
                print("\n✓ Your party rests and recovers strength.")
                self.turn += 1
            elif choice == "3":
                print("\n" + "="*60)
                print("DETAILED CHARACTER STATS")
                print("="*60)
                for char in self.characters:
                    print(f"\n{char}")
                    print(f"Experience: {char.experience}/{char.level * 100}")
                print()
            elif choice == "4":
                self.save_game()
            elif choice == "5":
                print("\n✓ Thanks for playing Mountain Rise! Your legend lives on...")
                break
        
        if self.turn >= 20 and not self.game_over:
            self.show_victory()

if __name__ == "__main__":
    game = Game()
    game.run()
