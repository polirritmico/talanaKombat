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


    def check_pressed_keys(self, keys) -> bool:
        if not self.check_attack_key(keys[-1]):
            return False
        if not self.check_mov_keys(keys[:-1]):
            return False
        return True


    def get_extra_keys(self, keys) -> str:
        mov_keys_count = len(self.mov_keys)
        keys_count = len(keys)
        if keys_count == mov_keys_count:
            return ""
        return keys[0:keys_count-mov_keys_count]


