# Mountain Rise: A Legend of the Russian Mountains

## Overview
Mountain Rise is a text-based adventure game inspired by Oregon Trail, set in the majestic mountains of Russia and Mongolia. Lead a party of three warriors on horseback/mounted creatures as you battle enemies, conquer territories, and build your legend across the Siberian wilderness.

## Features

### 3 Unique Mount Types with Different Abilities
- **Moose**: High HP (120) and Attack Power (18) - Slower but powerful
- **Horse**: Balanced stats - Fast and versatile (speed 9)
- **Caribou**: High Defense (10) and decent HP (110) - Energy efficient

### Dynamic Combat System
- **Turn-based combat with 3-character party**:
  - Player controls the main character each turn
  - Two NPC companions (Aleksandr, Temüjin) use intelligent AI
  - All three characters can attack, defend, heal, use items, or perform special attacks
- **Strategic choices**:
  - Attack: Deal damage to enemy
  - Defend: Increase defense for this round (temporary)
  - Heal: Heal entire party with medicinal magic
  - Use Potion: consume a limited potion to heal yourself during battle
  - Special Attack: a powerful, risky strike with chance to backfire
- **Intelligent AI**:
  - Companions heal when party is low on HP
  - Companions defend when their own HP is low
  - Companions prioritize attacking otherwise
- **Party-based damage**: All three characters contribute to combat
- **Defense system**: Temporary defense boosts reduce incoming damage
- **Enemy targeting**: Enemies randomly target party members
- **Party defeat condition**: Victory only if enemy is defeated before all allies fall

### RPG Progression System
- **Enemies become tougher** as you progress; they may arrive in groups and wield greater strength
- **Potions and Loot**: enemies occasionally drop healing potions after victory (now very rare, ~15%)
- **Potions and Loot**: enemies occasionally drop healing potions after victory
- **Experience and Leveling**: Defeat enemies to gain experience
- **Level Up Benefits**: Increased max HP, attack power, and defense
- **Territory Conquering**: Each victory expands your controlled lands

### Diverse Regions to Explore
1. **Siberian Pass** - Mountain Bandits, Cossack Raiders
2. **Mongolian Plateau** - Mongol Warriors, Nomadic Archers
3. **Ural Mountains** - Mountain Shamans, Yak Herders
4. **Lake Baikal** - Ice Wizards, Frost Giants
5. **Altai Mountains** - Eagle Knights, Wolf Packs, Black Dragon Guardian
6. **Kamchatka Volcanoes** - Volcanic Elementals, Lava Drakes, Inferno Titans
7. **Siberian Fortress** - Iron Guard Captains, Siege Knights, War Golems
8. **Khangai Mountains** - Spirit Warriors, Sky Shamans, Celestial Dragons
9. **Gobi Desert** - Sand Bandits, Desert Warlords, Sphinx Guardians
10. **Sakha Tundra** - Permafrost Walkers, Blizzard Wraiths, Eternal Winter Lords

### Enemy Variety
Different enemies in each region with varying stats and experience rewards. Tougher enemies yield greater rewards!

## How to Play

### Starting the Game
```bash
python game.py
```

### Character Setup
1. Choose your mount (Moose, Horse, or Caribou)
2. Enter your character's name
3. Two companion warriors join (Aleksandr and Temüjin)

### Main Actions
- **Travel**: Journey to new regions and encounter enemies — foes may now travel in groups, making battles much harder. On the road you might also meet potential recruits; choose which to add to your party (subject to a cap based on your level). Beware of environmental hazards that can injure or kill your party
- **Rest**: Heal your party between battles (also chance of mishaps)
- **View Stats**: Check detailed character information
- **Save Game**: Keep your progress
- **Quit**: Exit the game

### Combat Tips
- Monitor enemy patterns and adapt your strategy
- Heal when your HP drops low
- Use defend strategically when facing strong attacks
- Different enemies have different difficulty levels
- Recruited companions join your party and act like additional characters during combat

## Game Objectives
- Conquer 20+ territories across the Russian Mountains
- Level up your characters and improve their stats
- Defeat increasingly powerful enemies
- Build your legend and achieve victory!

> ⚙️ **Difficulty Tuning**: edit `config.py` to adjust healing amounts, potion strength, enemy scaling and base troop sizes.

## Game Mechanics

### Experience System
- XP = Level × 100 to level up
- Each level grants:
  - +10 Max HP
  - +5 Attack Power
  - +2 Defense

### Healing System
- Defend action grants temporary defense boost
- Heal action recovers 20 HP (weaker than before)
- Use Potion action heals 50 HP to the user (consumed)
- Resting recovers 30 HP for the entire party (less effective)

### Territory Conquest
- Winning a battle = 1 territory conquered
- Display shows current progress toward victory condition

## Victory Condition
Complete 20 turns and conquer as many territories as possible — or defeat the ultimate boss, the **Eternal Winter Lord** in the Sakha Tundra. The more you conquer, the greater your legend!

## Story Context
You lead a coalition of warriors from different backgrounds across the treacherous Russian and Mongolian mountains. Each battle won represents territory claimed and influence gained. Your journey will be remembered as the time a legendary warrior united the mountains!

---

Enjoy your adventure in the Mountains! Will you rise to become a legend?
