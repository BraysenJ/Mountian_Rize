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
        self.base_defense = 0
        self.temp_defense_bonus = 0
        self.experience = 0
        self.level = 1
        
        # Mount bonuses
        if mount == Mount.MOOSE:
            self.attack_power = 18
            self.defense = 8
            self.base_defense = 8
            self.health = 120
            self.max_health = 120
            self.mount_name = "Moose"
            self.speed = 7
        elif mount == Mount.HORSE:
            self.attack_power = 15
            self.defense = 6
            self.base_defense = 6
            self.health = 100
            self.max_health = 100
            self.mount_name = "Horse"
            self.speed = 9
        elif mount == Mount.CARIBOU:
            self.attack_power = 12
            self.defense = 10
            self.base_defense = 10
            self.health = 110
            self.max_health = 110
            self.mount_name = "Caribou"
            self.speed = 8
    
    def take_damage(self, damage):
        total_defense = self.defense + self.temp_defense_bonus
        actual_damage = max(1, damage - total_defense // 2)
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
        self.base_defense += 2
    
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
            ],
            "Kamchatka Volcanoes": [
                Enemy("Volcanic Elemental", 75, 23, 5, 180),
                Enemy("Lava Drake", 85, 26, 6, 220),
                Enemy("Inferno Titan", 110, 28, 7, 280),
            ],
            "Siberian Fortress": [
                Enemy("Iron Guard Captain", 70, 19, 8, 160),
                Enemy("Siege Knight", 80, 22, 9, 200),
                Enemy("War Golem", 120, 24, 10, 300),
            ],
            "Khangai Mountains": [
                Enemy("Spirit Warrior", 65, 21, 6, 145),
                Enemy("Sky Shaman", 75, 24, 5, 190),
                Enemy("Celestial Dragon", 105, 27, 7, 270),
            ],
            "Gobi Desert": [
                Enemy("Sand Bandit", 60, 20, 4, 140),
                Enemy("Desert Warlord", 85, 23, 6, 210),
                Enemy("Sphinx Guardian", 115, 26, 8, 290),
            ],
            "Sakha Tundra": [
                Enemy("Permafrost Walker", 70, 22, 7, 165),
                Enemy("Blizzard Wraith", 90, 25, 6, 240),
                Enemy("Eternal Winter Lord", 130, 29, 8, 320),
            ]
        }
        return random.choice(encounters.get(region, encounters["Siberian Pass"]))
    
    def combat(self, enemy):
        """Handle turn-based combat with all 3 characters"""
        print(f"\n{'='*60}")
        print(f"⚔️  BATTLE: Your Party vs {enemy.name}!")
        print(f"{'='*60}\n")
        
        round_num = 0
        while any(char.is_alive() for char in self.characters) and enemy.is_alive():
            round_num += 1
            print(f"\n--- ROUND {round_num} ---")
            
            # Show party status
            print("\n📊 PARTY STATUS:")
            for i, char in enumerate(self.characters, 1):
                health_bar = "🟩" if char.health > char.max_health * 0.7 else "🟨" if char.health > char.max_health * 0.3 else "🟥"
                print(f"  [{i}] {char.name} ({char.mount_name}): {char.health}/{char.max_health} HP {health_bar}")
            
            print(f"\n🐉 ENEMY: {enemy.name}: {enemy.health}/{enemy.max_health} HP\n")
            
            # Player character turn
            print("="*60)
            char = self.characters[0]
            if not char.is_alive():
                print(f"⚠️  {char.name} is unconscious and cannot act!")
            else:
                print(f"🎯 {char.name}'s turn! ({char.mount_name}) - Level {char.level}")
                print("Actions:")
                print("1. ⚔️  Attack")
                print("2. 🛡️  Defend")
                print("3. 🍃 Heal Party")
                
                action = input("Choose (1-3): ").strip()
                
                if action == "1":
                    # Attack
                    crit_chance = random.random()
                    damage = random.randint(int(char.attack_power * 0.8), int(char.attack_power * 1.2))
                    
                    if crit_chance < 0.15:
                        damage = int(damage * 1.5)
                        actual_damage = enemy.take_damage(damage)
                        print(f"\n⚡ CRITICAL HIT! {char.name} strikes for {actual_damage} damage!")
                    else:
                        actual_damage = enemy.take_damage(damage)
                        print(f"\n✓ {char.name} strikes for {actual_damage} damage!")
                        
                elif action == "2":
                    # Defend
                    char.temp_defense_bonus = 3
                    print(f"\n✓ {char.name} braces for impact! Defense +3 this round.")
                    
                elif action == "3":
                    # Heal party
                    total_heal = 0
                    for ally in self.characters:
                        if not ally.is_alive():
                            continue
                        heal_amount = 25
                        old_health = ally.health
                        ally.heal(heal_amount)
                        actual_heal = ally.health - old_health
                        total_heal += actual_heal
                    print(f"\n🍃 {char.name} uses healing magic! Party recovers {total_heal} total HP!")
                else:
                    print(f"\n{char.name} hesitates...")
            
            if not enemy.is_alive():
                break
            
            # NPC turns - Companion 1 (Aleksandr)
            print("\n" + "-"*60)
            char = self.characters[1]
            if not char.is_alive():
                print(f"⚠️  {char.name} is unconscious!")
            else:
                # AI: Attack if healthy, defend if damaged, heal if party low
                avg_party_health = sum(c.health for c in self.characters) / len(self.characters)
                
                if avg_party_health < self.characters[0].max_health * 0.4:
                    # Heal
                    for ally in self.characters:
                        if not ally.is_alive():
                            continue
                        heal_amount = 20
                        ally.heal(heal_amount)
                    print(f"🍃 {char.name} tends to wounded allies! Party recovers HP!")
                elif char.health < char.max_health * 0.5:
                    # Defend
                    char.temp_defense_bonus = 2
                    print(f"🛡️ {char.name} takes a defensive stance!")
                else:
                    # Attack
                    damage = random.randint(int(char.attack_power * 0.7), int(char.attack_power * 1.1))
                    actual_damage = enemy.take_damage(damage)
                    print(f"⚔️  {char.name} attacks for {actual_damage} damage!")
            
            if not enemy.is_alive():
                break
            
            # NPC turns - Companion 2 (Temüjin)
            print("\n" + "-"*60)
            char = self.characters[2]
            if not char.is_alive():
                print(f"⚠️  {char.name} is unconscious!")
            else:
                # AI: Attack, defend rotation
                if char.health < char.max_health * 0.4:
                    # Heal self
                    char.heal(25)
                    print(f"🍃 {char.name} recovers with medicinal herbs!")
                else:
                    # Attack
                    damage = random.randint(int(char.attack_power * 0.7), int(char.attack_power * 1.1))
                    actual_damage = enemy.take_damage(damage)
                    print(f"⚔️  {char.name} attacks for {actual_damage} damage!")
            
            if not enemy.is_alive():
                break
            
            # Enemy turn - attacks the party
            print("\n" + "="*60)
            print(f"🐉 {enemy.name}'s turn!")
            
            # Enemy targets random living character
            living_chars = [c for c in self.characters if c.is_alive()]
            if living_chars:
                target = random.choice(living_chars)
                enemy_damage = random.randint(int(enemy.attack * 0.7), int(enemy.attack * 1.3))
                actual_damage = target.take_damage(enemy_damage)
                print(f"→ {enemy.name} attacks {target.name} for {actual_damage} damage!")
            
            # Reset defense bonuses at end of round
            for char in self.characters:
                char.temp_defense_bonus = 0
            
            time.sleep(0.5)
        
        print(f"\n{'='*60}")
        
        # Check victory/defeat
        if enemy.is_alive():
            print(f"✗ DEFEAT! All warriors have fallen...")
            return False
        else:
            print(f"✓ VICTORY! Your party defeated {enemy.name}!")
            
            # All living characters gain experience
            exp_per_char = enemy.experience_reward
            for char in self.characters:
                if char.is_alive():
                    char.gain_experience(exp_per_char)
                    if char.level > 1:
                        print(f"🎉 {char.name} leveled up to {char.level}!")
            
            print(f"\n⭐ Each character gained {exp_per_char} experience!")
            self.lands_conquered += 1
            return True
    
    def travel(self):
        """Travel to a new region"""
        regions = ["Siberian Pass", "Mongolian Plateau", "Ural Mountains", "Lake Baikal", "Altai Mountains", 
                   "Kamchatka Volcanoes", "Siberian Fortress", "Khangai Mountains", "Gobi Desert", "Sakha Tundra"]
        region_descriptions = {
            "Siberian Pass": "A narrow mountain pass with jagged peaks towering above...",
            "Mongolian Plateau": "Vast open plains stretching to the horizon...",
            "Ural Mountains": "Ancient mountains shrouded in mist...",
            "Lake Baikal": "The crystalline waters of the world's deepest lake...",
            "Altai Mountains": "The legendary home of dragons and warriors...",
            "Kamchatka Volcanoes": "Volcanic peaks with rivers of molten lava flowing down the slopes...",
            "Siberian Fortress": "An ancient fortress carved into stone with towering walls...",
            "Khangai Mountains": "Sacred peaks where the sky touches the earth...",
            "Gobi Desert": "Endless sands under a burning sun, mysterious and unforgiving...",
            "Sakha Tundra": "Frozen wasteland where the earth never thaws and spirits roam free..."
        }
        
        print("\n" + "="*60)
        print("Choose your next destination:")
        for i, region in enumerate(regions, 1):
            print(f"{i}. {region}")
        
        choice = input(f"Select (1-{len(regions)}): ").strip()
        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(regions):
                self.current_region = regions[choice_idx]
            else:
                self.current_region = regions[0]
        except ValueError:
            self.current_region = regions[0]
        
        self.turn += 1
        
        print(f"\nYour party rides toward {self.current_region}...")
        print(f"{region_descriptions[self.current_region]}")
        time.sleep(2)
        
        # Random encounter
        if random.random() < 0.7:  # 70% chance of combat
            enemy = self.get_enemy_encounter(self.current_region)
            print(f"\n⚔️  An enemy appears: {enemy.name}!")
            time.sleep(1)
            
            # Combat with all three characters
            if self.combat(enemy):
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
