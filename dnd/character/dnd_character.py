#!/usr/bin/python
import Character

## DNDCharacter provides necessary utility information for defining playable
## characters.
class DNDCharacter(object):

    dnd_character_races = [
        "Dwarf",
        "Human",
        "Elf",
        "Tiefling",
        "Orc"
    ]

    dnd_character_classes = [
        "rogue",
        "barbarian",
        "bard",
        "wizard",
        "cleric"
    ]

  _attribute_dictionary = {
    'attribute': "name",
    'baseSave': 0,
    'abilityModifier': 0,
    'magicModifier': 0,
    'miscModifier': 0,
    'temporaryModifier': 0
  }

  def __init__(self):
    self.saving_throws = {
      'fortitude': 0,
      'reflex': 0,
      'will': 0
    }


    self.character_base_stats = {
      'STR': 0,
      'DEX': 0,
      'CON': 0,
      'INT': 0,
      'WIS': 0,
      'CHA': 0
    }


  ##
  ##
  def calculateSavingThrows(self, attribute, attribute_dictionary):
    savingThrows[attribute] = sum(attribute_dictionary.value())
