#!/usr/bin/python
from quest import Quest

## A Campaign is defined as collection of Quests
##
class Campaign(object):
  # overall plot and goal for the players to achieve
  description = None

  # a list of quest objects
  quests = None

  win_condition = None
  lose_condition = None

  def __init__(self, title):
    self.title = title

  def createCampaign(self):
    pass
