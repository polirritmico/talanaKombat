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


    def count_combos(self):
        # TODO: Ask if P or K alone is considered an combination.
        #       Now assume no.
        counter = 0
        for round in range(len(self.pressed_moves)):
            if (self.pressed_moves[round] == "" or
                self.pressed_attacks[round] == ""):
                continue
            counter += 1
        return counter


    def _count_non_empty(self, key_list: list) -> int:
        counter = 0
        for round in range(len(key_list)):
            if key_list[round] != "":
                counter += 1
        return counter


    def count_movements(self):
        return self._count_non_empty(self.pressed_moves)

    
    def count_attacks(self):
        return self._count_non_empty(self.pressed_attacks)


