#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Player:
    def __init__(self, _name: str="default_name", on_left_side: bool=True, _hp: int=6):
        self.name = _name
        self.hp = _hp
        self.movemets = []
        self.hits = []
        self.left_side = on_left_side

