#!/usr/bin/python
from encounter import Encounter
## A Quest is defined as collection of Encounters
##
class Quest(object):
  description = None
  encounters = None # uses the encounters object to define
  loot = None

  success_check = None
  failure_check = None
  
  def __init__(self, title):
    self.title = title

  def createQuest(self):
      # creates many encounters
    pass
