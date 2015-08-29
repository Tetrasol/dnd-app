#!/usr/bin/python
from dnd_classes import DNDClasses
from dnd_races import DNDRaces
from levels import Levels
DND_CLASSES = DNDClasses()
DND_RACES = DNDRaces()
LEVELS = Levels()

class Character(object):
    max_HP = None
    current_HP = None
    current_XP = 0
    next_level_XP = None
    level = 1
    MAX_XP = 1000000
    MAX_LEVEL = 30

    attribute_dictionary = {
      'attribute': "name",
      'baseSave': 0,
      'abilityModifier': 0,
      'magicModifier': 0,
      'miscModifier': 0,
      'temporaryModifier': 0
    }

    ability_scores = {
      'STR': 0,
      'DEX': 0,
      'CON': 0,
      'INT': 0,
      'WIS': 0,
      'CHA': 0
    }

    defenses = {
      'AC':   0,
      'FORT': 0,
      'REF':  0,
      'WILL': 0
    }

    skills = {
      'Acrobatics': 0,
      'Arcana': 0,
      'Athletics': 0,
      'Bluff' : 0,
      'Diplomacy': 0,
      'Dungeoneering': 0,
      'Endurance': 0,
      'Heal': 0,
      'History': 0,
      'Insight': 0,
      'Intimidate': 0,
      'Nature': 0,
      'Perception': 0,
      'Religion': 0,
      'Stealth': 0,
      'Streetwise': 0,
      'Thievery': 0,
      'Alchemy' : 0,
      'Engineering': 0,
      'Profession' :0
    }

    ability_modifiers = {
      'STRMOD': 0,
      'DEXMOD': 0,
      'CONMOD': 0,
      'INTMOD': 0,
      'WISMOD': 0,
      'CHAMOD': 0
    }

    # Initializer method
    #
    def __init__(self, player_name, character_name, race, character_class):
        self.player_name = player_name
        self.character_name = character_name
        self.race = race
        self.character_class = character_class

        calculateBaseStats()
        calculateMaxHP()

    #
    def calculateAbilityScores(self):
      if self.race == DND_RACES.ELF:
          ability_scores["DEX"] += 2
          ability_scores["WIS"] += 2
      elif self.race == DND_RACES.ELADRIN:
          ability_scores["DEX"] += 2
          ability_scores["INT"] += 2
      elif self.race == DND_RACES.DWARF:
          ability_scores["CON"] += 2
          ability_scores["WIS"] += 2
      elif self.race == DND_RACES.HUMAN:
          pass
      elif self.race == DND_RACES.TIEFLING:
          ability_scores["INT"] += 2
          ability_scores["CHA"] += 2
      elif self.race == DND_RACES.DRAGONBORN:
          ability_scores["STR"] += 2
          ability_scores["CHA"] += 2
          skills["History"] +=2
          skills["Intimidate"] +=2
          ##TO-DO: MUST ADD SIZE TO RACES
          ##TO-DO: MUST ADD lANGUAGES
          ##TO-DO: MUST ADD SPEED TO RACES

      elif self.race == DND_RACES.HALFLING:
          ability_scores["DEX"] += 2
          ability_scores["CHA"] += 2
      elif self.race == DND_RACES.HALF_ELF:
          ability_scores["CON"] += 2
          ability_scores["CHA"] += 2
    ##
    def calculateMaxHP(self):
      if self.character_class == DND_CLASSES.ROUGE:
          max_HP += 3
      if self.character_class == DND_CLASSES.FIGHTER:
          pass
      if self.character_class == DND_CLASSES.PALADIN:
          pass
      if self.character_class == DND_CLASSES.BARD:
          pass
      if self.character_class == DND_CLASSES.WIZARD:
          pass
      if self.character_class == DND_CLASSES.CLERIC:
          pass
      if self.character_class == DND_CLASSES.WARLORD:
          pass
      if self.character_class == DND_CLASSES.WARLOCK:
          pass
      if self.character_class == DND_CLASSES.RANGER:
          pass

    ##
    def calculateLevel(self):
        levels = LEVELS.LEVELS
            if self.current_XP == self.MAX_XP:
                return self.MAX_LEVEL
            for xp in levels:
                current_index = levels.index(xp)
                next_index = current_index + 1

                if self.current_XP >= xp and self.current_XP < levels[next_index]:
                    return current_index + 1

    # ##
    # def calculateAbilityModifiers(self, attribute, modified_value):
    #   abilityModifier[attribute] = sum(attribute_dictionary.value())
