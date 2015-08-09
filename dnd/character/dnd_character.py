#!/usr/bin/python
import Character

class DNDCharacter(Character):
  
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

  ##
  ##
  def calculateSavingThrows(self, attribute, attribute_dictionary):
    savingThrows[attribute] = sum(attribute_dictionary.value())