#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Player:
    def __init__(self, name: str="default_name",
                       on_left_side: bool=False, hp: int=6):
        self.combos_collection = None
        self.hp = hp
        self.left_side = on_left_side
        self.name = name
        self.pressed_attacks = []
        self.pressed_moves = []


    def take_action(self, round) -> int:
        damage = 0
        key_attack = self.pressed_attacks[round]
        keys_moves = self.pressed_moves[round]
        for combo in self.combos_collection:
            if not (combo.check_attack_key(key_attack) or
                    combo.check_mov_keys(keys_moves)):
                continue
        return damage


    def is_unconscious(self) -> bool:
        if self.hp <= 0:
            return True
        return False


    def set_combos_collection(self, combos):
        sort_by_len = lambda combo: len(combo.mov_keys)
        self.combos_collection = sorted(combos, key=sort_by_len, reverse=True)


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


