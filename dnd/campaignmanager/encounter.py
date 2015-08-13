#!/usr/bin/python

## An Encounter is described as a collections of tasks needed to be completed
## by the players. The Encounters only exist within the context of a Quest.
class Encounter(object):
  loot_drop = None # items, xp, money
  description = None

  monster_fight = False
  monster = None # if monsters - how many? object list?

  event_check = None # need Event Object
  # event checks are a variety of triggers
  # they depend on various conditions defined by the player

  success_check = None

  failure_check = None



  def __init__(self, title):
    self.title = title

  def createEncounter(self):
    pass
