# Configuration file for Mountain Rise

# Combat settings
COMBAT_ESCAPE_CHANCE = 0.2  # 20% chance to escape combat
COMBAT_CRIT_CHANCE = 0.15   # 15% chance for critical hit (1.5x damage)
CRIT_MULTIPLIER = 1.5

# Encounter rates
ENEMY_ENCOUNTER_CHANCE = 0.7  # 70% chance of enemy when traveling
ITEM_ENCOUNTER_CHANCE = 0.2   # 20% chance of finding items
SAFE_PASSAGE_CHANCE = 0.1     # 10% chance of completely safe passage

# Game rules
VICTORY_TERRITORY_GOAL = 20
MAX_TURNS = 20
STARTING_HEALTH_MOOSE = 120
STARTING_HEALTH_HORSE = 100
STARTING_HEALTH_CARIBOU = 110

# Experience multipliers
BASE_EXP_MULTIPLIER = 1.0
LEVEL_UP_EXP_BASE = 100

# Healing amounts (tweak to adjust difficulty)
HEAL_ACTION_AMOUNT = 20   # amount restored by the heal action in combat
REST_ACTION_AMOUNT = 30   # amount restored when resting
POTION_HEAL_AMOUNT = 50   # amount a potion heals

# Difficulty scaling
ENEMY_SCALING_PER_TURN = 1.05  # Enemies get 5% stronger each turn
TROOP_BASE_MAX = 3          # base maximum troops an enemy group can have
