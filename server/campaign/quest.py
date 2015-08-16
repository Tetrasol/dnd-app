#!/usr/bin/python
from encounter import Encounter

## A Quest is defined as collection of Encounters
##
class Quest(object):

  # textual quest plot, setting, and objective
  __description = None

  # list of quest encounters
  __encounters = []

  __success_condition = None
  __failure_condition = None

  # inventory object describing rewards after encounter completion
  __loot_drop = None # items, xp, money

  def __init__(self, title):
    self.title = title

  def addEncounterToQuest(self, title):
      # creates many encounters
      encounter = Encounter(title)
      __encounters.insert(encounter)

  def removeEncounterFromQuest(self, title):
      pass
