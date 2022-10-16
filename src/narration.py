#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class Narration():
    def __init__(self, player, on_left_side: bool=False):
        self.player_name = player.name
        self.on_left = on_left_side


    @staticmethod
    def greetings(p1, p2):
        print("\n--- TALANA KOMBAT --------------------------------------")
        print("Welcome to the fight beetwen:")
        length = 30
        p1_name = p1.name.center(length)
        vs = "vs".center(length)
        p2_name = p2.name.center(length)
        print("\n".join([p1_name, vs, p2_name]))
        print("\nAnd the battle begins!!:\n")


    def take_damage(self):
        messages = ["{} take damage".format(self.player_name),]
        print(random.choice(messages))


    def hit(self, combo, target_player, extra_move_keys):
        messages = ["{} hit {}".format(self.player_name, target_player.name),]
        print(random.choice(messages))


    def move_only(self):
        messages = ["Move only",]
        print(random.choice(messages))


    def nothing(self):
        messages = ["Does nothing",]
        print(random.choice(messages))

    
    def falls_unconscious(self):
        messages = ["{} is unconscious".format(self.player_name),]
        print(random.choice(messages))


    def end_combat(self):
        messages = ["The combat ends",]
        print(random.choice(messages))


