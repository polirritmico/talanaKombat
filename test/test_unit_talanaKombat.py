#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.talanaKombat import TalanaKombat

#@unittest.skip
class TestTalanaKombat(unittest.TestCase):
    def setUp(self):
        self.tk = TalanaKombat()


    #@unittest.skip
    def test_players_on_two_sides(self):
        left = self.tk.p1.left_side
        right = self.tk.p2.left_side

        self.assertTrue(left)
        self.assertFalse(right)


    #@unittest.skip
    def test_set_player_hits(self):
        expected_name = "Taladoken"
        expected_power = 3
        expected_comb_mov = "DSD"
        expected_comb_hit = "P"
        player_combo = self.tk.p1.combos_collection[0]

        self.assertEqual(expected_name, player_combo.name)
        self.assertEqual(expected_power, player_combo.power)
        self.assertEqual(expected_comb_mov, player_combo.mov_keys)
        self.assertEqual(expected_comb_hit, player_combo.attack_key)


    #@unittest.skip
    def test_first_player_less_combos(self):
        figh_case = "test/cases/order_case1.json"
        expected_name = "Arnaldor Shuatseneguer"
        expected_combos = 1
        self.tk.load_pressed_keys_json(figh_case)
        first_player_name = self.tk.get_sorted_player_list()[0].name
        first_player_combos = self.tk.p2.count_combos()

        self.assertEqual(expected_name, first_player_name)
        self.assertEqual(expected_combos, first_player_combos)


    #@unittest.skip
    def test_first_player_less_pressed_keys_with_empty(self):
        figh_case = "test/cases/order_case2.json"
        expected = "Arnaldor Shuatseneguer"
        self.tk.load_pressed_keys_json(figh_case)
        first_player_name = self.tk.get_sorted_player_list()[0].name

        self.assertEqual(expected, first_player_name)


    #@unittest.skip
    def test_first_player_less_movements(self):
        figh_case = "test/cases/order_case3.json"
        expected_name = "Tonyn Stallone"
        expected_count = 4
        self.tk.load_pressed_keys_json(figh_case)
        first_player_name = self.tk.get_sorted_player_list()[0].name
        first_player_count = self.tk.p1.count_movements()

        self.assertEqual(expected_name, first_player_name)
        self.assertEqual(expected_count, first_player_count)


    #@unittest.skip
    def test_first_player_less_attacks(self):
        figh_case = "test/cases/order_case4.json"
        expected_name = "Arnaldor Shuatseneguer"
        expected_count = 3
        self.tk.load_pressed_keys_json(figh_case)
        first_player_name = self.tk.get_sorted_player_list()[0].name
        first_player_count = self.tk.p2.count_attacks()

        self.assertEqual(expected_name, first_player_name)
        self.assertEqual(expected_count, first_player_count)


    #@unittest.skip
    def test_first_player_all_equal(self):
        figh_case = "test/cases/order_case5.json"
        expected = "Tonyn Stallone"
        self.tk.load_pressed_keys_json(figh_case)
        first_player_name = self.tk.get_sorted_player_list()[0].name

        self.assertEqual(expected, first_player_name)


