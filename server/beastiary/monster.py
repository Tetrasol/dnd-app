#!/usr/bin/pthon
from monster_list import MonsterList
MONSTER_LIST = MonsterList()

class Monster(object):

    def __init__(self, name, max_HP):
        self.name = name
        self.monster_ID = None
        self.max_HP = max_HP
        self.current_HP = max_HP

    def addMonsterIDToIDList(self):
        unique = True

        if len(MONSTER_LIST.IDs) == 0: # if the list is empty
            # add monster id to list
            MONSTER_LIST.IDs.insert(self.name.upper() + str(self.max_HP))
        elif len(MONSTER_LIST.IDs) > 0: # list not empty
            # make sure the id is unique
            for ID in MONSTER_LIST.IDs:
                if ID == self.name.upper():
                    unique = False

            if unique:
                # add monster id to list
                MONSTER_LIST.IDs.insert(self.name.upper() + str(self.max_HP))
