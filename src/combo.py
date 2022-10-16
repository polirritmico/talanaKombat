#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Combo():
    def __init__(self, name, power, mov_keys, attack_key):
        self.name = name
        self.power = power
        self.mov_keys = mov_keys
        self.attack_key = attack_key


    def check_attack_key(self, key):
        if key == self.attack_key:
            return True
        return False


    def check_mov_keys(self, keys) -> bool:
        mov_keys_count = len(self.mov_keys)
        if len(keys) < mov_keys_count:
            return False
        reversed_keys = keys[::-1]
        reversed_mov_keys = self.mov_keys[::-1]
        for i in range(mov_keys_count):
            if reversed_keys[i] != reversed_mov_keys[i]:
                return False
        return True


    def check_pressed_keys(self, move_keys, attack_key) -> bool:
        if not self.check_attack_key(attack_key):
            return False
        if not self.check_mov_keys(move_keys):
            return False
        return True


    def get_extra_move_keys(self, pressed_move_keys) -> str:
        mov_keys_count = len(self.mov_keys)
        pressed_keys_count = len(pressed_move_keys)
        if pressed_keys_count == mov_keys_count:
            return ""
        return pressed_move_keys[0:pressed_keys_count-mov_keys_count]


