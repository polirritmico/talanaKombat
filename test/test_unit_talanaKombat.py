#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.talanaKombat import TalanaKombat

#@unittest.skip
class TestRepository(unittest.TestCase):
    def setUp(self):
        self.talanaKombat = TalanaKombat()


    #@unittest.skip
    def test_dummy(self):
        expected = "Expected output"
        output = self.talanaKombat.a_function()
        self.assertEqual(expected, output)


