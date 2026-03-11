import random
import time
from enum import Enum
import config

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
        self.potions = 1  # each character starts with a healing potion
        self.weapon = None  # assigned for recruits
        
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
    
    def use_potion(self):
        """Consume a healing potion if available."""
        if self.potions > 0:
            self.potions -= 1
            heal_amt = config.POTION_HEAL_AMOUNT
            self.heal(heal_amt)
            return heal_amt
        return 0

    def __str__(self):
        weapon_str = f" | WEAPON: {self.weapon}" if self.weapon else ""
        return f"{self.name} (Level {self.level}) - {self.mount_name}{weapon_str}\nHP: {self.health}/{self.max_health} | ATK: {self.attack_power} | DEF: {self.defense} | POTIONS: {self.potions}"

class Enemy:
    def __init__(self, name, health, attack, defense, experience_reward, troops=1):
        # health provided is per-troop base; total health scales with troops
        self.name = name
        self.troops = troops
        self.health = health * troops
        self.max_health = health * troops
        self.attack = attack
        self.defense = defense
        self.experience_reward = experience_reward
    
    def take_damage(self, damage):
        # simple reduction, troops just influence starting health
        actual_damage = max(1, damage - self.defense // 2)
        self.health -= actual_damage
        return actual_damage
    
    def is_alive(self):
        return self.health > 0
    
    def __str__(self):
        return f"{self.name} (Troops: {self.troops}) - HP: {self.health}/{self.max_health}"

class Game:
    def __init__(self):
        self.characters = []
        self.lands_conquered = 0
        self.current_region = "Starting Camp"
        self.turn = 0
        self.game_over = False
        self.story_progress = 0
        # recruited companions will be stored in self.characters alongside the initial party
        # party cap is calculated based on main character level
        
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
        """Generate enemy based on region. Troop counts increase with territory progress."""
        # define a helper to wrap enemies with troop count
        def make(name, health, attack, defense, xp):
            # base troop range has variability from the start and scales upwards
            base_max = 3  # small groups of enemies even early on
            extra = self.lands_conquered // 5
            max_troops = base_max + extra
            troops = random.randint(1, max(1, max_troops))
            return Enemy(name, health, attack, defense, xp, troops)
        encounters = {
            "Siberian Pass": [
                make("Mountain Bandit", 40, 12, 3, 50),
                make("Cossack Raider", 50, 14, 4, 75),
                make("Pirate Scout", 35, 10, 2, 40),
            ],
            "Mongolian Plateau": [
                make("Mongol Warrior", 55, 16, 5, 100),
                make("Nomadic Archer", 45, 18, 3, 90),
                make("Steppe Warlord", 70, 20, 6, 150),
            ],
            "Ural Mountains": [
                make("Mountain Shaman", 50, 15, 4, 85),
                make("Yak Herder", 60, 13, 5, 95),
                make("Avalanche Summoner", 65, 17, 6, 120),
            ],
            "Lake Baikal": [
                make("Ice Wizard", 55, 19, 3, 110),
                make("Fish Merchant", 40, 11, 2, 60),
                make("Frost Giant", 80, 22, 7, 160),
            ],
            "Altai Mountains": [
                make("Golden Eagle Knight", 65, 18, 6, 130),
                make("Wolf Pack Leader", 55, 20, 4, 115),
                make("Black Dragon Guardian", 100, 25, 8, 200),
            ],
            "Kamchatka Volcanoes": [
                make("Volcanic Elemental", 75, 23, 5, 180),
                make("Lava Drake", 85, 26, 6, 220),
                make("Inferno Titan", 110, 28, 7, 280),
            ],
            "Siberian Fortress": [
                make("Iron Guard Captain", 70, 19, 8, 160),
                make("Siege Knight", 80, 22, 9, 200),
                make("War Golem", 120, 24, 10, 300),
            ],
            "Khangai Mountains": [
                make("Spirit Warrior", 65, 21, 6, 145),
                make("Sky Shaman", 75, 24, 5, 190),
                make("Celestial Dragon", 105, 27, 7, 270),
            ],
            "Gobi Desert": [
                make("Sand Bandit", 60, 20, 4, 140),
                make("Desert Warlord", 85, 23, 6, 210),
                make("Sphinx Guardian", 115, 26, 8, 290),
            ],
            "Sakha Tundra": [
                make("Permafrost Walker", 70, 22, 7, 165),
                make("Blizzard Wraith", 90, 25, 6, 240),
                make("Eternal Winter Lord", 130, 29, 8, 320),
            ]
        }
        return random.choice(encounters.get(region, encounters["Siberian Pass"]))

    def recruit_event(self):
        """Encounter potential recruits while traveling. You may choose some subject to party cap."""
        # 25% chance to meet a group of potential recruits
        if random.random() < 0.25:
            print("\n🏕️ Along the road you meet a group of fighters seeking a leader.")
            # decide if potion payment is required to recruit any
            need_potion = random.random() < 0.3
            if need_potion:
                print("They demand a potion in exchange for joining.")
            # generate between 1 and 3 candidates
            candidates = []
            possible_names = ["Boris","Yuri","Mikhail","Oleg","Ivan","Svetlana","Anya","Katya","Nikolai","Dmitri"]
            random.shuffle(possible_names)
            for i in range(random.randint(1, 3)):
                name = possible_names.pop()
                mount = random.choice(list(Mount))
                # base recruit stats are weaker than main characters
                recruit = Character(name, mount)
                # downgrade stats
                recruit.max_health = int(recruit.max_health * 0.8)
                recruit.health = recruit.max_health
                recruit.attack_power = int(recruit.attack_power * 0.7)
                recruit.defense = int(recruit.defense * 0.7)
                recruit.weapon = random.choice(["Sword","Axe","Spear","Bow"])
                candidates.append(recruit)
            # display candidates
            print("Potential recruits:")
            for idx, rec in enumerate(candidates, 1):
                print(f"  [{idx}] {rec.name} ({rec.mount_name}) Weapon: {rec.weapon} | HP: {rec.health} | ATK: {rec.attack_power} | DEF: {rec.defense}")
            # compute party cap
            cap = self.characters[0].level + 3
            current_size = len(self.characters)
            remaining = max(0, cap - current_size)
            if remaining <= 0:
                print("Your party is already at capacity; you cannot recruit more.")
                return
            print(f"You may recruit up to {remaining} more companions (party cap {cap}).")
            pick = input("Enter numbers to recruit separated by commas (or none): ").strip()
            if not pick or pick.lower().startswith('n'):
                print("You decide not to recruit anyone.")
                return
            choices = []
            for part in pick.split(','):
                try:
                    n = int(part.strip())
                    if 1 <= n <= len(candidates):
                        choices.append(n-1)
                except ValueError:
                    continue
            selections = []
            for idx in choices:
                if len(selections) >= remaining:
                    break
                selections.append(candidates[idx])
            if not selections:
                print("No valid recruits chosen.")
                return
            # check potion cost
            if need_potion:
                if self.characters[0].potions > 0:
                    self.characters[0].potions -= 1
                    print("You give a potion as payment.")
                else:
                    print("You lack a potion, so none will join.")
                    return
            # add to party
            for rec in selections:
                self.characters.append(rec)
                print(f"{rec.name} joins your party riding a {rec.mount_name} with a {rec.weapon}!")

    def random_event(self, context="travel"):
        """Occasionally trigger events that can injure or kill characters.
        `context` may be 'travel' or 'rest' to vary events."""
        # roughly 20% chance of something happening
        if random.random() < 0.2:
            events = ["avalanche", "blizzard", "ambush", "sickness"]
            event = random.choice(events)
            if event == "avalanche":
                print("\n🌨️ An avalanche thunders down the mountain!")
                for c in self.characters:
                    if c.is_alive():
                        damage = random.randint(20, 50)
                        c.take_damage(damage)
                        print(f"  ❄️ {c.name} is hit for {damage} damage!")
            elif event == "blizzard":
                print("\n🌬️ A sudden blizzard strikes!")
                for c in self.characters:
                    if c.is_alive():
                        loss = random.randint(10, 30)
                        c.take_damage(loss)
                        print(f"  ❄️ {c.name} loses {loss} health to cold!")
            elif event == "ambush":
                print("\n🚨 Bandits ambush your party!")
                victim = random.choice(self.characters)
                if victim.is_alive():
                    damage = random.randint(30, 60)
                    victim.take_damage(damage)
                    print(f"  ⚔️ {victim.name} was injured for {damage} damage!")
            elif event == "sickness":
                print("\n🤒 Your party falls ill from tainted water!")
                for c in self.characters:
                    if c.is_alive():
                        c.health = max(1, c.health - 40)
                        print(f"  🤢 {c.name} is weakened by illness!")
            # check for wipe-out
            if not any(c.is_alive() for c in self.characters):
                print("\n✗ All members have perished in the catastrophe...")
                self.game_over = True
    
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
                print(f"4. 🧪 Use Potion ({char.potions} left)")
                print("5. 💥 Special Attack")
                
                action = input("Choose (1-5): ").strip()
                
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
                        heal_amount = config.HEAL_ACTION_AMOUNT  # use config value
                        old_health = ally.health
                        ally.heal(heal_amount)
                        actual_heal = ally.health - old_health
                        total_heal += actual_heal
                    print(f"\n🍃 {char.name} uses healing magic! Party recovers {total_heal} total HP!")
                elif action == "4":
                    # Use potion
                    heal_amt = char.use_potion()
                    if heal_amt > 0:
                        print(f"\n🧪 {char.name} drinks a potion and recovers {heal_amt} HP!")
                    else:
                        print(f"\n{char.name} has no potions left!")
                elif action == "5":
                    # Special attack
                    if random.random() < 0.5:
                        damage = random.randint(int(char.attack_power * 1.5), int(char.attack_power * 2))
                        actual_damage = enemy.take_damage(damage)
                        print(f"\n🔥 {char.name} unleashes a powerful strike for {actual_damage} damage!")
                    else:
                        self_damage = random.randint(5, 15)
                        char.take_damage(self_damage)
                        print(f"\n❗Special attack backfires! {char.name} takes {self_damage} damage!")
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
                        heal_amount = config.HEAL_ACTION_AMOUNT
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
                    char.heal(config.HEAL_ACTION_AMOUNT)
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
                # damage scales with number of troops
                base_damage = random.randint(int(enemy.attack * 0.7), int(enemy.attack * 1.3))
                enemy_damage = base_damage * enemy.troops
                actual_damage = target.take_damage(enemy_damage)
                print(f"→ {enemy.name} ({enemy.troops} troops) strikes {target.name} for {actual_damage} damage!")
            
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

            # chance to find a potion as loot
            if random.random() < 0.15:  # rarer loot
                alive_chars = [c for c in self.characters if c.is_alive()]
                if alive_chars:
                    finder = random.choice(alive_chars)
                    finder.potions += 1
                    print(f"\n🎁 {finder.name} found a healing potion after the battle!")

            # check final boss / win condition
            if enemy.name == "Eternal Winter Lord" or self.lands_conquered >= 20:
                print("\n🏆 You have defeated the final threat and conquered the mountains!")
                self.show_victory()
                self.game_over = True
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
        
        # random travel events
        self.random_event(context="travel")
        if self.game_over:
            return
        # possible recruitment opportunity
        self.recruit_event()
        if self.game_over:
            return
        
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
            print(f"    Potions: {char.potions}")
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
                    char.heal(config.REST_ACTION_AMOUNT)  # use config
                print("\n✓ Your party rests and recovers strength.")
                self.turn += 1
                # possibility of mishap while resting
                if random.random() < 0.2:
                    print("\n😱 While resting something goes wrong...")
                    self.random_event(context="rest")
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
