#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.talanaKombat import TalanaKombat

#@unittest.skip
class TestLoadJSON(unittest.TestCase):
    def setUp(self):
        self.tk = TalanaKombat()


    #@unittest.skip
    def test_players_on_two_sides(self):
        left = self.tk.players[0].left_side
        right = self.tk.players[1].left_side
        self.assertTrue(left)
        self.assertFalse(right)


    #@unittest.skip
    def test_set_player_hits(self):
        expected_name = "Taladoken"
        expected_power = 3
        expected_comb_mov = "DSD"
        expected_comb_hit = "P"
        player_combo = self.tk.players[0].combos_collection[0]


        self.assertEqual(expected_name, player_combo.name)
        self.assertEqual(expected_power, player_combo.power)
        self.assertEqual(expected_comb_mov, player_combo.key_combination[0])
        self.assertEqual(expected_comb_hit, player_combo.key_combination[1])


