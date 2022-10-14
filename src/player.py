#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Player:
    def __init__(self, _name: str="default_name", _hp: int=6):
        self.name = _name
        self.hp = _hp
        self.movemets = []
        self.hits = []

