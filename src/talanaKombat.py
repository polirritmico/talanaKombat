#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__version__ = "0.0"

import os
import json

from src.player import Player
from src.narration import Narration
from config import Players_combo_collection
from config import Players_names

class TalanaKombat():
    def __init__(self):
        # Set players data
        self.p1 = Player(Players_names[0], on_left_side=True)
        self.p2 = Player(Players_names[1])
        self.p1.set_combos_collection(Players_combo_collection[0])
        self.p2.set_combos_collection(Players_combo_collection[1])

        self.winner = None
        self.rounds = 0


    def load_pressed_keys_json(self, filename: str):
        with open(filename, "r") as stream:
            try:
                keylog = json.load(stream)
            except json.JSONDecodeError as err:
                print("ERROR: Bad JSON file: ")
                raise err
        # Parse the json data
        self.p1.pressed_moves = keylog.get("player1").get("movimientos")
        self.p2.pressed_moves = keylog.get("player2").get("movimientos")
        self.p1.pressed_attacks = keylog.get("player1").get("golpes")
        self.p2.pressed_attacks = keylog.get("player2").get("golpes")
        self.rounds = max(len(self.p1.pressed_moves), len(self.p2.pressed_moves))


    def get_sorted_player_list(self) -> list[Player]:
        # First player is the one with less <movements + hits>
        ordered_list = self._sort_by_criteria(self.p1.count_combos(),
                                              self.p2.count_combos())
        if ordered_list != None:
            return ordered_list
        # If equal, first the one with less moves
        ordered_list = self._sort_by_criteria(self.p1.count_movements(),
                                              self.p2.count_movements())
        if ordered_list != None:
            return ordered_list
        # If equal, first the one with less attacks
        ordered_list = self._sort_by_criteria(self.p1.count_attacks(),
                                              self.p2.count_attacks())
        if ordered_list != None:
            return ordered_list
        # If equal, first player1
        return [self.p1, self.p2]


    def _sort_by_criteria(self, p1_count, p2_count):
        if p1_count < p2_count:
            return [self.p1, self.p2]
        if p1_count > p2_count:
            return [self.p2, self.p1]
        return None


    def fight(self):
        players_turn = self.get_sorted_player_list()
        first_player = players_turn[0]
        second_player = players_turn[1]

        Narration.greetings(first_player, second_player)
        for round in range(self.rounds):
            first_player.take_action(round, second_player)
            if second_player.is_unconscious():
                self.winner = first_player.end_combat()
                break
            second_player.take_action(round, first_player)
            if first_player.is_unconscious():
                self.winner = second_player.end_combat()
                break
        if self.winner == None:
            raise Exception("ERROR: Missing inputs. Check JSON")
        return self.winner


    def run(self):
        self.fight()

