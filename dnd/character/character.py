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

  character_base_stats = {
    'STR': 0,
    'DEX': 0,
    'CON': 0,
    'INT': 0,
    'WIS': 0,
    'CHA': 0
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
  def calculateBaseStats(self):
      if self.race == DNDRaces.ELF:
        character_base_stats["STR"] += 2

  ##
  def calculateMaxHP(self):
      if self.character_class == DNDClasses.ROUGE:
          max_HP += 3

  ##
  ##
  def calculateAbilityModifiers(self, attribute, modified_value):
    abilityModifier[attribute] = sum(attribute_dictionary.value())
