#!/usr/bin/python

## A Campaign is defined as collection of Quests
##
class Campaign(object):

    description = None
    win_condition = None
    lose_condition = None


  def __init__(self, title):
    self.title = title

  def createCampaign(self):
    pass
