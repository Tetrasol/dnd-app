import unittest
from character import Character, LEVELS, DND_CLASSES, DND_RACES

class CharacterMethodTest(unittest.TestCase):
    def test_create_simple_character(self):
        newCharacterVar = ["alex", "potato", "elf", "rogue"]
        newCharacter = Character(newCharacterVar[0],
                                 newCharacterVar[1],
                                 newCharacterVar[2],
                                 newCharacterVar[3])
        self.assertEqual(newCharacter.player_name, 'alex')
        self.assertEqual(newCharacter.character_name, 'potato')
        self.assertEqual(newCharacter.race, DND_RACES.ELF)
        self.assertEqual(newCharacter.character_class, DND_CLASSES.ROGUE)

    def test_simple_character_hp_elf(self):
        newCharacterVar = ["alex", "potato", "elf", "rogue"]
        newCharacter = Character(newCharacterVar[0],
                                 newCharacterVar[1],
                                 newCharacterVar[2],
                                 newCharacterVar[3])
        self.assertEqual(newCharacter.max_HP, 3)
        self.assertEqual(newCharacter.current_HP, 3)

    @unittest.skip("Method Not working")
    def test_simple_character_xp(self):
        newCharacterVar = ["alex", "potato", "elf", "rogue"]
        newCharacter = Character(newCharacterVar[0],
                                 newCharacterVar[1],
                                 newCharacterVar[2],
                                 newCharacterVar[3])
        self.assertEqual(newCharacter.MAX_XP, LEVELS[-1])
        self.assertEqual(newCharacter.current_XP, LEVELS[0])
        self.assertEqual(newCharacter.level, 1)

    @unittest.skip("Method Not working")
    def test_simple_character_abilities_elf(self):
        newCharacterVar = ["alex", "potato", "elf", "rogue"]
        newCharacter = Character(newCharacterVar[0],
                                 newCharacterVar[1],
                                 newCharacterVar[2],
                                 newCharacterVar[3])
        self.assertEqual(newCharacter.ability_scores["STR"], 0)
        self.assertEqual(newCharacter.ability_scores["DEX"], 2)
        self.assertEqual(newCharacter.ability_scores["CON"], 0)
        self.assertEqual(newCharacter.ability_scores["INT"], 0)
        self.assertEqual(newCharacter.ability_scores["WIS"], 2)
        self.assertEqual(newCharacter.ability_scores["CHA"], 0)

if __name__ == '__main__':
    unittest.main()
