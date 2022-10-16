#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.talanaKombat import TalanaKombat

#@unittest.skip
class TestLoadJSON(unittest.TestCase):
    def setUp(self):
        self.tk = TalanaKombat()

    #@unittest.skip
    def test_load_json_input1(self):
        file_path = "test/cases/input_test1.json"
        expected_p1_mov = "W"
        expected_p1_hit = "P"
        expected_p2_mov = "D"
        expected_p2_hit = "K"
        self.tk.load_pressed_keys_json(file_path)

        self.assertEqual(expected_p1_mov, self.tk.p1.pressed_moves[0])
        self.assertEqual(expected_p1_hit, self.tk.p1.pressed_attacks[0])
        self.assertEqual(expected_p2_mov, self.tk.p2.pressed_moves[0])
        self.assertEqual(expected_p2_hit, self.tk.p2.pressed_attacks[0])


    def test_load_json_input2(self):
        file_path = "test/cases/input_test2.json"
        expected_p1_mov = "A"
        expected_p1_hit = ""
        expected_p2_mov = "S"
        expected_p2_hit = "P"
        self.tk.load_pressed_keys_json(file_path)

        self.assertEqual(expected_p1_mov, self.tk.p1.pressed_moves[0])
        self.assertEqual(expected_p1_hit, self.tk.p1.pressed_attacks[0])
        self.assertEqual(expected_p2_mov, self.tk.p2.pressed_moves[0])
        self.assertEqual(expected_p2_hit, self.tk.p2.pressed_attacks[0])


    #@unittest.skip
    def test_load_json_fight_case1(self):
        file_path = "test/cases/fight_case1.json"
        expected_p1_mov = ["D", "DSD", "S", "DSD", "SD"]
        expected_p1_hit = ["K", "P", "", "K", "P"]
        expected_p2_mov = ["SA", "SA", "SA", "ASA", "SA"]
        expected_p2_hit = ["K", "", "K", "P", "P"]
        self.tk.load_pressed_keys_json(file_path)

        self.assertEqual(expected_p1_mov, self.tk.p1.pressed_moves)
        self.assertEqual(expected_p1_hit, self.tk.p1.pressed_attacks)
        self.assertEqual(expected_p2_mov, self.tk.p2.pressed_moves)
        self.assertEqual(expected_p2_hit, self.tk.p2.pressed_attacks)


    #@unittest.skip
    def test_load_json_fight_case2(self):
        file_path = "test/cases/fight_case2.json"
        expected_p1_mov = ["SDD", "DSD", "SA", "DSD"]
        expected_p1_hit = ["K", "P", "K", "P"]
        expected_p2_mov = ["DSD", "WSAW", "ASA", "", "ASA", "SA"]
        expected_p2_hit = ["P", "K", "K", "K", "P", "k"]
        self.tk.load_pressed_keys_json(file_path)

        self.assertEqual(expected_p1_mov, self.tk.p1.pressed_moves)
        self.assertEqual(expected_p1_hit, self.tk.p1.pressed_attacks)
        self.assertEqual(expected_p2_mov, self.tk.p2.pressed_moves)
        self.assertEqual(expected_p2_hit, self.tk.p2.pressed_attacks)


