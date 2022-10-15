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
        player = self.tk.players[0]
        output = player.count_movements()

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_count_attacks(self):
        figh_case = "test/cases/fight_case3.json"
        expected = 5

        self.tk.load_pressed_keys_json(figh_case)
        player = self.tk.players[1]
        output = player.count_attacks()

        self.assertEqual(expected, output)


