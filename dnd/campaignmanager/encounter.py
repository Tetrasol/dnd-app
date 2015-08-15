#!/usr/bin/python
from event_check import EventCheck

## An Encounter is described as a collections of tasks needed to be completed
## by the players. The Encounters only exist within the context of a Quest.
class Encounter(object):

  # textual encounter plot, setting, and objective
  description = None

  monster_fight = False
  monster = None # monster list object

  # event checks are a variety of triggers
  # they depend on various conditions defined by the dungeon master
  event_check = None # need Event Object
  success_condition = None
  failure_condition = None

  # inventory object describing rewards after encounter completion
  loot_drop = None # items, xp, money

  def __init__(self, title):
    self.title = title

  def addMonsterToEncounter(self):
