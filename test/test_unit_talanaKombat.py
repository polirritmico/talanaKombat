#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.talanaKombat import TalanaKombat

#@unittest.skip
class TestLoadJSON(unittest.TestCase):
    def setUp(self):
        self.talanaKombat = TalanaKombat()

    #@unittest.skip
    def test_players_on_two_sides(self):
        left = self.talanaKombat.players[0].left_side
        right = self.talanaKombat.players[1].left_side
        self.assertTrue(left)
        self.assertFalse(right)


