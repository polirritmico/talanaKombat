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


    #@unittest.skip
    def test_count_combinations(self):
        figh_case = "test/fight_case3.json"
        expected = 3

        self.tk.load_pressed_keys_json(figh_case)
        player = self.tk.players[1]
        output = player.count_combinations()

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_count_movements(self):
        figh_case = "test/fight_case3.json"
        expected = 2

        self.tk.load_pressed_keys_json(figh_case)
        player = self.tk.players[0]
        output = player.count_movements()

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_count_attacks(self):
        figh_case = "test/fight_case3.json"
        expected = 5

        self.tk.load_pressed_keys_json(figh_case)
        player = self.tk.players[1]
        output = player.count_attacks()

        self.assertEqual(expected, output)


    @unittest.skip
    def test_first_player_less_pressed_keys(self):
        figh_case = "test/order_case_1.json"
        expected = "Arnaldor Shuatseneguer"
        self.tk.load_pressed_keys_json(figh_case)
        first_player_name = self.tk.get_ordered_player_list()[0].name

        self.assertEqual(expected, first_player_name)


    @unittest.skip
    def test_first_player_less_pressed_keys_with_empty(self):
        figh_case = "test/"
        expected = "Arnaldor Shuatseneguer"
        self.tk.load_pressed_keys_json(figh_case)
        first_player_name = self.tk.get_ordered_player_list()[0].name

        self.assertEqual(expected, first_player_name)


    @unittest.skip
    def test_first_player_less_movements(self):
        figh_case = "test/"
        expected = "Arnaldor Shuatseneguer"
        self.tk.load_pressed_keys_json(figh_case)
        first_player_name = self.tk.get_ordered_player_list()[0].name

        self.assertEqual(expected, first_player_name)


    @unittest.skip
    def test_first_player_less_attacks(self):
        figh_case = "test/"
        expected = "Arnaldor Shuatseneguer"
        self.tk.load_pressed_keys_json(figh_case)
        first_player_name = self.tk.get_ordered_player_list()[0].name

        self.assertEqual(expected, first_player_name)


    @unittest.skip
    def test_first_player_all_equal(self):
        figh_case = "test/"
        expected = "Arnaldor Shuatseneguer"
        self.tk.load_pressed_keys_json(figh_case)
        first_player_name = self.tk.get_ordered_player_list()[0].name

        self.assertEqual(expected, first_player_name)









