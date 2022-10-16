#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.combo import Combo
from config import Players_combo_collection

#@unittest.skip
class TestCombo(unittest.TestCase):
    def setUp(self):
        self.combo = Combo("Toasty", 12, "ASA", "P")

    #@unittest.skip
    def test_check_attack_key(self):
        self.assertTrue(self.combo.check_attack_key("P"))
        self.assertFalse(self.combo.check_attack_key("D"))


    #@unittest.skip
    def test_check_mov_keys(self):
        self.assertTrue(self.combo.check_mov_keys("AASA"))
        self.assertFalse(self.combo.check_mov_keys("ASAA"))


    #@unittest.skip
    def test_parse_pressed_keys(self):
        self.combo.mov_keys = "WSA"
        self.combo.attack_key = "K"
        move_keys = "WSA"
        attack_key = "K"
        output = self.combo.check_pressed_keys(move_keys, attack_key)
        self.assertTrue(output)


    #@unittest.skip
    def test_get_extra_move_keys(self):
        keys = "WAASA"
        expected = "WA"
        output = self.combo.get_extra_move_keys(keys)
        self.assertEqual(expected, output)


    def test_get_extra_move_keys_no_extra(self):
        keys = "ASA"
        expected = ""
        output = self.combo.get_extra_move_keys(keys)
        self.assertEqual(expected, output)


