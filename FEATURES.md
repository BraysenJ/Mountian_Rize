# Mountain Rise - Complete Game Documentation

## 🎮 What's Included

### Main Game Files
1. **game.py** - The complete game engine with all features
2. **run.sh** - Launcher script for easy execution
3. **config.py** - Configuration settings (customizable)
4. **README.md** - Comprehensive user guide
5. **QUICKSTART.md** - Quick reference guide
6. **LORE.md** - Rich story and world-building

---

## 🚀 Quick Start

### Option 1: Direct Python
```bash
python game.py
```

### Option 2: Use Launcher
```bash
chmod +x run.sh
./run.sh
```

---

## 📋 Core Features Implemented

### ✅ Character System
- Three unique mount types (Moose, Horse, Caribou)
- Each with distinct stat distributions
- Main character customization (name, mount choice)
- Two NPC companions (Aleksandr, Temüjin)
- Full stat tracking: HP, Attack, Defense, Experience

### ✅ Mount Bonuses
| Mount | HP | Attack | Defense | Speed | Best For |
|-------|----|---------|---------|----|-----------|
| Moose | 120 | 18 | 8 | 7 | Damage |
| Horse | 100 | 15 | 6 | 9 | Balanced |
| Caribou | 110 | 12 | 10 | 8 | Defense |

### ✅ Combat System
- **Full party combat**: All 3 characters fight together with AI companions
- **Player-controlled main character** with two intelligent NPC companions
- **Multiple action types**:
  - Attack (with 15% critical hit chance for 1.5x damage)
  - Defend (temporary defense boost for the round)
  - Heal (restores HP to entire party, now weaker to increase challenge)
  - Use Potion (heal 50 HP, extremely limited supply)
  - Special Attack (high-risk, high-reward strike with potential backfire)
- **Potions**: rare loot drops give extra healing items (about 15% chance)
- **Enemies now come with variable troop counts**:
  - Each foe may consist of 1–3 warriors initially; troop size grows as you conquer more lands
  - Health scales with number of troops, and attack damage is multiplied accordingly for more deadly encounters
- **Intelligent AI companions**:
  - Aleksandr: Balanced fighter, attacks and defends
  - Temüjin: Defensive specialist with healing focus
  - Companions adapt to combat conditions (heal when needed, defend when low)
- **Enemy mechanics**:
  - Scales with territory progression and troop count
  - Targets party members randomly
  - Varied attack patterns
- **Damage calculation** with randomization for unpredictability
- **Defense system**: Temporary defense reduces incoming damage
- **Combat continues** until enemy is defeated or all party members fall

### ✅ RPG Progression
- Experience point system
- Level up threshold: Current Level × 100 XP
- Level-up rewards:
  - +10 Max HP
  - +5 Attack Power
  - +2 Defense
- Territory conquest tracking

### ✅ Five Explorable Regions
1. **Siberian Pass** - Starting area, weak enemies
2. **Mongolian Plateau** - Mid-tier difficulty
3. **Ural Mountains** - Advanced challenges
4. **Lake Baikal** - Powerful enemies
5. **Altai Mountains** - End-game bosses
6. **Kamchatka Volcanoes** - Volcanic realm, fire-themed battles
7. **Siberian Fortress** - Military stronghold, armored defenders
8. **Khangai Mountains** - Mystical peaks, spiritual enemies
9. **Gobi Desert** - Ancient desert, mythical guardians
10. **Sakha Tundra** - Frozen wastes, ultimate ice lords

### ✅ Enemy Variety (30+ different enemy types)
**Siberian Pass:**
- Mountain Bandit (40 HP)
- Cossack Raider (50 HP)
- Pirate Scout (35 HP)

**Mongolian Plateau:**
- Mongol Warrior (55 HP)
- Nomadic Archer (45 HP)
- Steppe Warlord (70 HP)

**Ural Mountains:**
- Mountain Shaman (50 HP)
- Yak Herder (60 HP)
- Avalanche Summoner (65 HP)

**Lake Baikal:**
- Ice Wizard (55 HP)
- Fish Merchant (40 HP)
- Frost Giant (80 HP)

**Altai Mountains:**
- Golden Eagle Knight (65 HP)
- Wolf Pack Leader (55 HP)
- Black Dragon Guardian (100 HP)

**Kamchatka Volcanoes:** ⭐ NEW
- Volcanic Elemental (75 HP)
- Lava Drake (85 HP)
- Inferno Titan (110 HP)

**Siberian Fortress:** ⭐ NEW
- Iron Guard Captain (70 HP)
- Siege Knight (80 HP)
- War Golem (120 HP)

**Khangai Mountains:** ⭐ NEW
- Spirit Warrior (65 HP)
- Sky Shaman (75 HP)
- Celestial Dragon (105 HP)

**Gobi Desert:** ⭐ NEW
- Sand Bandit (60 HP)
- Desert Warlord (85 HP)
- Sphinx Guardian (115 HP)

**Sakha Tundra:** ⭐ NEW
- Permafrost Walker (70 HP)
- Blizzard Wraith (90 HP)
- Eternal Winter Lord (130 HP)

### ✅ Game Flow
- 20 turns maximum
- 70% encounter rate when traveling
- **Travel events**: aside from enemies and hazards, you may encounter villagers or mercenaries to recruit companions (25% chance each travel)
- Encounters grow harder as territories are claimed: expect more troops and stronger foes
- Random environmental hazards (avalanches, blizzards, ambushes, sickness) can injure or kill party members — another way to die
- Territory conquest: 1 per victory
- Victory condition: 20+ territories conquered **or defeat of the final boss (Eternal Winter Lord)**
- Progression tracking with visual indicators

### ✅ User Interface
- Clear menu system (numbered options)
- Status displays with health indicators
- Region descriptions
- Combat narration with emoji icons
- Experience progress bars
- Party health overview

### ✅ Party Management
- **All three characters actively fight** in every battle
- **Player controls main character** each turn
- **Two NPC companions** fight with intelligent AI
- **Shared healing** - heal action restores entire party HP
- **Unified experience** - all party members gain XP from victories
- **Individual level tracking** - each character levels independently
- **Rest action** - heals all party members simultaneously (50 HP recovery)
- **Party status display** - see all three allies' HP and status at once

---

## 🎯 Game Objectives

### Primary Goal
Conquer 20 territories across 10 mountain regions

### Secondary Goals
- Level up all characters
- Survive all 20 turns
- Defeat the mightiest bosses (War Golem, Sphinx Guardian, Eternal Winter Lord)
- Explore all 10 regions
- Build your legend

---

## 🎓 How to Win

1. **Start** in Siberian Pass with weak enemies
2. **Gain XP** and level up (reach Level ~ 8-10)
3. **Progress** through regions systematically
4. **Build Power** with each level increase
5. **Challenge** mid-tier regions (Ural, Lake Baikal, Altai)
6. **Master** end-game regions (Kamchatka, Fortress, Khangai, Desert, Tundra)
7. **Defeat** ultimate bosses (War Golem, Sphinx Guardian, Eternal Winter Lord)
8. **Achieve** 20+ territories conquered and legendary status!

---

## 🛠️ Customization

Edit `config.py` to adjust:
- Encounter rates
- Enemy scaling difficulty
- Healing amounts
- Experience multipliers
- Victory conditions
- Damage calculations

---

## 📊 Game Statistics

- **Total Code Lines**: ~380 (game.py)
- **Total Enemies**: 30+
- **Total Regions**: 10 (5 original + 5 NEW)
- **Max Characters**: 3 (1 player, 2 NPC)
- **Mount Options**: 3
- **Combat Actions**: 3
- **Menu Options**: 5 main, multiple sub-menus
- **Highest Enemy HP**: 130 (Eternal Winter Lord)
- **Highest Enemy Attack Power**: 29 (Eternal Winter Lord)

---

## 🎭 Story Elements

Each region has:
- Unique flavor text and descriptions
- Thematic enemies
- Progressive difficulty
- Narrative progression from weak to powerful enemies
- Legendary final boss battle

---

## 🔄 Game Loop

```
Setup → Main Menu → Choose Action →
├─ Travel (70% combat, 30% safe passage)
│  └─ Combat → Win/Lose
├─ Rest (heal party)
├─ View Stats (detail screen)
├─ Save Game (manual save)
└─ Quit

Repeat until: Turn 20 or Game Over
```

---

## 🎮 Example Gameplay

```
1. Create character (choose Moose/Horse/Caribou)
2. Enter name (e.g., "Aleksandr")
3. Start at Turn 0 with all party healthy
4. Travel to region (e.g., Siberian Pass)
5. Encounter enemy (e.g., Mountain Bandit)
6. Battle with attack/defend/heal
7. Win → +XP, +1 territory, advance to next turn
8. Repeat for 20 turns
9. Achieve 20+ territories = Victory!
```

---

## 🌟 Features Requested vs Delivered

### ✅ Text-based game
- Full terminal UI with menu system

### ✅ Oregon Trail style
- Turn-based travel and encounters
- Party management
- Resource management (HP, healing)
- Progressive difficulty

### ✅ Russia/Mongolia mountains setting
- 5 regions with thematic names
- Culturally appropriate enemies (Cossacks, Mongols, etc.)
- Regional descriptions and lore

### ✅ 3 characters with different mounts
- Moose, Horse, Caribou
- Unique stat distributions
- Different gameplay styles

### ✅ Fight enemies
- Full combat system
- 15+ different enemies
- Strategic mechanics

### ✅ Grow/expand lands
- Territory tracking
- Victory condition based on territories
- Visible progress counter

---

## 📝 Files Overview

| File | Purpose | Lines |
|------|---------|-------|
| game.py | Main game engine | 320+ |
| run.sh | Launcher script | 10 |
| config.py | Configuration settings | 20+ |
| README.md | Full user guide | 150+ |
| QUICKSTART.md | Quick reference | 200+ |
| LORE.md | Story & world-building | 250+ |

---

## 🎪 Next Steps for Players

1. Run `python game.py` 
2. Choose your mount (Moose recommended for first playthrough)
3. Enter a character name
4. Select "Travel to new region"
5. Fight enemies and gain experience
6. Level up and become stronger
7. Conquer all 20 territories
8. Achieve your legend!

---

## 💾 Save System

- Manual save via "Save game" option
- Saves: territories conquered, character levels
- Load by starting new game (tutorial will explain)

---

## 🏆 Difficulty Progression

| Region | Difficulty | Avg Enemy HP | Recommended Level |
|--------|-----------|----------|-------------------|
| Siberian Pass | Very Easy | 40 | 1-2 |
| Mongolian Plateau | Easy | 50 | 3-4 |
| Ural Mountains | Medium | 55 | 5-7 |
| Lake Baikal | Hard | 60 | 8-10 |
| Altai Mountains | Very Hard | 75 | 11-12 |
| Kamchatka Volcanoes | Extreme | 90 | 13-14 |
| Siberian Fortress | Extreme | 90 | 14-15 |
| Khangai Mountains | Extreme | 82 | 15-16 |
| Gobi Desert | Extreme | 87 | 16-17 |
| Sakha Tundra | Legendary | 97 | 17+ |

---

Enjoy your adventure! 🏔️⛰️🎮
