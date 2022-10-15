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
    players = []

    def __init__(self):
        # Set players data
        self.players = [Player(Players_names[0]),
                        Player(Players_names[1], on_left_side=False)]
        self.players[0].combos_collection = Players_combo_collection[0]
        self.players[1].combos_collection = Players_combo_collection[1]
        # Set narrator
        self.narrator = Narration(self.players)


    def load_pressed_keys_json(self, filename: str):
        with open(filename, "r") as stream:
            try:
                keylog = json.load(stream)
            except json.JSONDecodeError as err:
                print("ERROR: Bad JSON file: ")
                raise err
        # Parse the json data
        self.players[0].pressed_moves = keylog.get("player1").get("movimientos")
        self.players[1].pressed_moves = keylog.get("player2").get("movimientos")
        self.players[0].pressed_attacks = keylog.get("player1").get("golpes")
        self.players[1].pressed_attacks = keylog.get("player2").get("golpes")


    def _sort_less_count(self, p1_count, p2_count):
        if p1_count < p2_count:
            return [self.players[0], self.players[1]]
        if p1_count > p2_count:
            return [self.players[1], self.players[0]]
        return None


    def get_sorted_player_list(self) -> list[Player]:
        # First player is the one with less <movements + hits>
        ordered_list = self._sort_less_count(self.players[0].count_combos(),
                                            self.players[1].count_combos())
        if ordered_list != None:
            return ordered_list
        # If equal, first the one with less moves
        ordered_list = self._sort_less_count(self.players[0].count_movements(),
                                            self.players[1].count_movements())
        if ordered_list != None:
            return ordered_list
        # If equal, first the one with less attacks
        ordered_list = self._sort_less_count(self.players[0].count_attacks(),
                                            self.players[1].count_attacks())
        if ordered_list != None:
            return ordered_list
        # If equal, first player1
        return [self.players[0], self.players[1]]


    def run(self):
        players_in_round_order = self.get_sorted_player_list()
        for player in players_in_round_order:
            print(player.name)


