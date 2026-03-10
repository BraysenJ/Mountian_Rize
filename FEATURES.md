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
- Turn-based battles with strategic depth
- Three action types:
  - Attack (with critical hit chance: 15%)
  - Defend (temporary defense boost)
  - Heal (recover 30 HP)
- Enemy AI with varied attack patterns
- Damage calculation with randomization
- Combat continues until player or enemy is defeated

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

### ✅ Enemy Variety (15+ different enemy types)
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

### ✅ Game Flow
- 20 turns maximum
- 70% encounter rate when traveling
- Territory conquest: 1 per victory
- Victory condition: 20+ territories conquered
- Progression tracking with visual indicators

### ✅ User Interface
- Clear menu system (numbered options)
- Status displays with health indicators
- Region descriptions
- Combat narration with emoji icons
- Experience progress bars
- Party health overview

### ✅ Party Management
- Heal all party members with "Rest" action
- Individual status viewing
- Character level tracking
- Shared rest benefits (50 HP recovery)

---

## 🎯 Game Objectives

### Primary Goal
Conquer 20 territories across 5 mountain regions

### Secondary Goals
- Level up all characters
- Survive all 20 turns
- Defeat the Black Dragon Guardian
- Build your legend

---

## 🎓 How to Win

1. **Start** in Siberian Pass with weak enemies
2. **Gain XP** and level up (reach Level ~ 5-6)
3. **Progress** through regions systematically
4. **Build Power** with each level increase
5. **Challenge** Altai Mountains boss battles
6. **Achieve** 20 territories conquered

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

- **Total Code Lines**: ~320 (game.py)
- **Total Enemies**: 15+
- **Total Regions**: 5
- **Max Characters**: 3 (1 player, 2 NPC)
- **Mount Options**: 3
- **Combat Actions**: 3
- **Menu Options**: 5 main, multiple sub-menus

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
| Altai Mountains | Very Hard | 75+ | 11+ |

---

Enjoy your adventure! 🏔️⛰️🎮
