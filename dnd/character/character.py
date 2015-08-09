#!/usr/bin/python

class Character(object):
  
  def __init__(self, player_name, character_name):
    self.player_name = player_name
    self.character_name = character_name
    self.max_HP = 1
    self.current_HP = 1
    self.character_level = None
    self.character_class = None
    self.character_race = None
    self.character_base_stats = {
      'STR': 0,
      'DEX': 0,
      'CON': 0,
      'INT': 0,
      'WIS': 0,
      'CHA': 0
    }
    
