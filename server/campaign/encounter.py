#!/usr/bin/python
#from event_check import EventCheck

## An Encounter is described as a collections of tasks needed to be completed
## by the players. The Encounters only exist within the context of a Quest.
class Encounter(object):

    # textual encounter plot, setting, and objective
    __description = None

    __monster_list = None # monster list object

    # event checks are a variety of triggers
    # they depend on various conditions defined by the dungeon master
    __event_check = None # need Event Object
    __success_condition = None
    __failure_condition = None

    # inventory object describing rewards after encounter completion
    __loot_drop = None # items, xp, money

    def __init__(self, title, monster_fight):
        self.title = title
        self.__monster_fight = False

    def addMonsterToEncounter(self, monster_id):
        if monster_fight == True:
            # add monster
        else:
            # handle no monster error
