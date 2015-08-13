#!/usr/bin/python
from dnd_classes import DNDClasses
from dnd_races import DNDRaces

class Character(object):
  max_HP = None
  current_HP = None
  current_XP = None
  next_level_XP = None
  level = 1

  attribute_dictionary = {
    'attribute': "name",
    'baseSave': 0,
    'abilityModifier': 0,
    'magicModifier': 0,
    'miscModifier': 0,
    'temporaryModifier': 0
  }

  character_ability_scores = {
    'STR': 0,
    'DEX': 0,
    'CON': 0,
    'INT': 0,
    'WIS': 0,
    'CHA': 0
  }

  character_skills = {
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

  character_ability_modifiers{
    'STRMOD': 0,
    'DEXMOD': 0,
    'CONMOD': 0,
    'INTMOD': 0,
    'WISMOD': 0,
    'CHAMOD': 0
  }

  ## Initializer method
  ##
  def __init__(self, player_name, character_name, race, character_class):
    self.player_name = player_name
    self.character_name = character_name
    self.race = race
    self.character_class = character_class

    calculateBaseStats()
    calculateMaxHP()

  ##
  def calculateAbilityScores(self):
    if self.race == DNDRaces.ELF:
        character_ability_scores["DEX"] += 2
        character_ability_scores["WIS"] += 2
    elif self.race == DNDRaces.ELADRIN:
        character_ability_scores["DEX"] += 2
        character_ability_scores["INT"] += 2
    elif self.race == DNDRaces.DWARF:
        character_ability_scores["CON"] += 2
        character_ability_scores["WIS"] += 2
    elif self.race == DNDRaces.HUMAN:
    elif self.race == DNDRaces.TIEFLING:
        character_ability_scores["INT"] += 2
        character_ability_scores["CHA"] += 2
    elif self.race == DNDRaces.DRAGONBORN:
        character_ability_scores["STR"] += 2
        character_ability_scores["CHA"] += 2
    elif self.race == DNDRaces.HALFLING:
        character_ability_scores["DEX"] += 2
        character_ability_scores["CHA"] += 2
    elif self.race == DNDRaces.HALF-ELF:
        character_ability_scores["CON"] += 2
        character_ability_scores["CHA"] += 2

  ##
  def calculateMaxHP(self):
      if self.character_class == DNDClasses.ROUGE:
          max_HP += 3

  ##
  ##
  def calculateAbilityModifiers(self, attribute, modified_value):
    abilityModifier[attribute] = sum(attribute_dictionary.value())
