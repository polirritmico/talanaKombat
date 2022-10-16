#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.player import Player
from src.talanaKombat import TalanaKombat

#@unittest.skip
class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.tk = TalanaKombat()


    #@unittest.skip
    def test_take_action(self):
        fight_case = "test/cases/fight_case1.json"
        self.tk.load_pressed_keys_json(fight_case)

        round = 1
        expected = "Taladoken"
        output = self.tk.p1.take_action(round, self.tk.p2)
        self.assertEqual(expected, output)
        round = 3
        expected = "Remeyuken"
        output = self.tk.p1.take_action(round, self.tk.p2)
        self.assertEqual(expected, output)


    #@unittest.skip
    def test_count_movements(self):
        fight_case = "test/cases/fight_case3.json"
        expected = 2

        self.tk.load_pressed_keys_json(fight_case)
        player = self.tk.p1
        output = player.count_movements()

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_count_attacks(self):
        fight_case = "test/cases/fight_case3.json"
        expected = 5

        self.tk.load_pressed_keys_json(fight_case)
        player = self.tk.p2
        output = player.count_attacks()

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_count_combos(self):
        fight_case = "test/cases/fight_case3.json"
        expected = 3

        self.tk.load_pressed_keys_json(fight_case)
        player = self.tk.p2
        output = player.count_combos()

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_is_unconsciouts(self):
        self.assertFalse(self.tk.p1.is_unconscious())
        self.tk.p1.hp = 0
        self.assertTrue(self.tk.p1.is_unconscious())


