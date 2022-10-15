#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__version__ = "0.0"

import os
import json

from src.player import Player
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


    def get_ordered_player_list(self) -> list[Player]:
        # First player is the one with less <movements + hits>
        players = self.players
        p1_count = len(players[0].pressed_moves) + len(players[0].pressed_attacks)
        p2_count = len(players[1].pressed_moves) + len(players[1].pressed_attacks)
        if p1_count > p2_count:
            return [players[0], players[1]]
        if p1_count < p2_count:
            return [players[1], players[0]]

        # If equal, first the one with less moves
        p1_count = len(players[0].pressed_moves)
        p2_count = len(players[1].pressed_moves)
        if p1_count > p2_count:
            return [players[0], players[1]]
        if p1_count < p2_count:
            return [players[1], players[0]]

        # If equal, first the one with less attacks
        p1_count = len(players[0].pressed_attacks)
        p2_count = len(players[1].pressed_attacks)
        if p1_count > p2_count:
            return [players[0], players[1]]
        if p1_count < p2_count:
            return [players[1], players[0]]

        # If equal, first player1
        return [players[0], players[1]]


    def run(self):
        players_in_round_order = self.get_ordered_player_list()
        for player in players_in_round_order:
            print(player.name)


