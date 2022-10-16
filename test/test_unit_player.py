#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.player import Player
from src.talanaKombat import TalanaKombat

#@unittest.skip
class TestTalanaKombat(unittest.TestCase):
    def setUp(self):
        self.tk = TalanaKombat()


    #@unittest.skip
    def test_count_movements(self):
        figh_case = "test/cases/fight_case3.json"
        expected = 2

        self.tk.load_pressed_keys_json(figh_case)
        player = self.tk.p1
        output = player.count_movements()

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_count_attacks(self):
        figh_case = "test/cases/fight_case3.json"
        expected = 5

        self.tk.load_pressed_keys_json(figh_case)
        player = self.tk.p2
        output = player.count_attacks()

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_count_combinations(self):
        figh_case = "test/cases/fight_case3.json"
        expected = 3

        self.tk.load_pressed_keys_json(figh_case)
        player = self.tk.p2
        output = player.count_combos()

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_is_unconsciouts(self):
        self.assertFalse(self.tk.p1.is_unconscious())
        self.tk.p1.hp = 0
        self.assertTrue(self.tk.p1.is_unconscious())


