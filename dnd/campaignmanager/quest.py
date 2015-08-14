#!/usr/bin/python
from encounter import Encounter

## A Quest is defined as collection of Encounters
##
class Quest(object):

  # textual quest plot, setting, and objective
  description = None

  # list of quest encounters
  encounters = []

  success_condition = None
  failure_condition = None

  # inventory object describing rewards after encounter completion
  loot_drop = None # items, xp, money

  def __init__(self, title):
    self.title = title

  def addEncounterToQuest(self, title):
      # creates many encounters
      encounter = Encounter(title)

  def removeEncounterFromQuest(self, title):
      pass
