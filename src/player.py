#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.narration import Narration

class Player:
    def __init__(self, name: str="default_name",
                       on_left_side: bool=False, hp: int=6):
        self.combos_collection = None
        self.hp = hp
        self.left_side = on_left_side
        self.name = name
        self.pressed_attacks = []
        self.pressed_moves = []
        self.narrator = Narration(self, on_left_side)


    def harm_target_player(self, combo, target_player, extra_move_keys):
        self.narrator.attack(combo, target_player, extra_move_keys)
        damage = combo.power
        target_player.take_damage(damage)


    def take_damage(self, damage):
        self.hp -= damage
        self.narrator.take_damage(damage)


    def end_combat(self, loser: str):
        """ Return winner name """
        self.narrator.end_combat(loser, self.hp)
        return self.name


    def take_action(self, round, target_player):
        if round >= len(self.pressed_moves):
            self.narrator.nothing()
            return
        key_attack = self.pressed_attacks[round]
        keys_moves = self.pressed_moves[round]

        if key_attack == "" and keys_moves == "":
            self.narrator.nothing()
            return "nothing"
        if key_attack == "":
            self.narrator.move_only(target_player)
            return "move_only"
        for combo in self.combos_collection:
            if not (combo.check_attack_key(key_attack) and
                    combo.check_mov_keys(keys_moves)):
                continue
            extra_move_keys = combo.get_extra_move_keys(keys_moves)
            self.harm_target_player(combo, target_player, extra_move_keys)
            return combo.name
        raise Exception("Unknown action...\nCheck JSON data")


    def is_unconscious(self) -> bool:
        if self.hp <= 0:
            self.narrator.falls_unconscious()
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


