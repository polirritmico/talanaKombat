#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Narration():
    def __init__(self, on_left_side: bool=False):
        self.on_left = on_left_side


    def attack(self, player, mov, attack):
        print("{} golpea")

    def gretings(self, p1, p2):
        print("Bienvenidos a la pelea entre {} y {}".format(p1, p2))
