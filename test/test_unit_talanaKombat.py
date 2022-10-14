#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.talanaKombat import TalanaKombat

#@unittest.skip
class TestRepository(unittest.TestCase):
    def setUp(self):
        self.talanaKombat = TalanaKombat()


    #@unittest.skip
    def test_load_json_basic(self):
        file_path = "test/input_test1.json"
        expected_p1_mov = "W"
        expected_p1_hit = "P"
        expected_p2_mov = "D"
        expected_p2_hit = "K"
        self.talanaKombat.load_fight_json(file_path)

        self.assertEqual(expected_p1_mov, self.talanaKombat.players[0].movements_list[0])
        self.assertEqual(expected_p1_hit, self.talanaKombat.players[0].hits_list[0])
        self.assertEqual(expected_p2_mov, self.talanaKombat.players[1].movements_list[0])
        self.assertEqual(expected_p2_hit, self.talanaKombat.players[1].hits_list[0])



