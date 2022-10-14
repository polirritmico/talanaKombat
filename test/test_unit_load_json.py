#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.talanaKombat import TalanaKombat

#@unittest.skip
class TestLoadJSON(unittest.TestCase):
    def setUp(self):
        self.talanaKombat = TalanaKombat()

    #@unittest.skip
    def test_load_json_input1(self):
        file_path = "test/input_test1.json"
        expected_p1_mov = "W"
        expected_p1_hit = "P"
        expected_p2_mov = "D"
        expected_p2_hit = "K"
        talanaKombat = TalanaKombat()
        talanaKombat.load_fight_json(file_path)

        self.assertEqual(expected_p1_mov, talanaKombat.players[0].movements[0])
        self.assertEqual(expected_p1_hit, talanaKombat.players[0].hits[0])
        self.assertEqual(expected_p2_mov, talanaKombat.players[1].movements[0])
        self.assertEqual(expected_p2_hit, talanaKombat.players[1].hits[0])


    def test_load_json_input2(self):
        file_path = "test/input_test2.json"
        expected_p1_mov = "A"
        expected_p1_hit = ""
        expected_p2_mov = "S"
        expected_p2_hit = "P"
        talanaKombat = TalanaKombat()
        talanaKombat.load_fight_json(file_path)

        self.assertEqual(expected_p1_mov, talanaKombat.players[0].movements[0])
        self.assertEqual(expected_p1_hit, talanaKombat.players[0].hits[0])
        self.assertEqual(expected_p2_mov, talanaKombat.players[1].movements[0])
        self.assertEqual(expected_p2_hit, talanaKombat.players[1].hits[0])


    #@unittest.skip
    def test_load_json_fight_case1(self):
        file_path = "test/fight_case1.json"
        expected_p1_mov = ["D", "DSD", "S", "DSD", "SD"]
        expected_p1_hit = ["K", "P", "", "K", "P"]
        expected_p2_mov = ["SA", "SA", "SA", "ASA", "SA"]
        expected_p2_hit = ["K", "", "K", "P", "P"]
        talanaKombat = TalanaKombat()
        talanaKombat.load_fight_json(file_path)

        self.assertEqual(expected_p1_mov, talanaKombat.players[0].movements)
        self.assertEqual(expected_p1_hit, talanaKombat.players[0].hits)
        self.assertEqual(expected_p2_mov, talanaKombat.players[1].movements)
        self.assertEqual(expected_p2_hit, talanaKombat.players[1].hits)


    #@unittest.skip
    def test_load_json_fight_case2(self):
        file_path = "test/fight_case2.json"
        expected_p1_mov = ["SDD", "DSD", "SA", "DSD"]
        expected_p1_hit = ["K", "P", "K", "P"]
        expected_p2_mov = ["DSD", "WSAW", "ASA", "", "ASA", "SA"]
        expected_p2_hit = ["P", "K", "K", "K", "P", "k"]
        talanaKombat = TalanaKombat()
        talanaKombat.load_fight_json(file_path)

        self.assertEqual(expected_p1_mov, talanaKombat.players[0].movements)
        self.assertEqual(expected_p1_hit, talanaKombat.players[0].hits)
        self.assertEqual(expected_p2_mov, talanaKombat.players[1].movements)
        self.assertEqual(expected_p2_hit, talanaKombat.players[1].hits)


