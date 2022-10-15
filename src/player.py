#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Player:
    def __init__(self, name: str="default_name",
                       on_left_side: bool=True, hp: int=6):
        self.combos_collection = None
        self.hp = hp
        self.left_side = on_left_side
        self.name = name
        self.pressed_attacks = []
        self.pressed_moves = []

