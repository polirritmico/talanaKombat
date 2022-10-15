#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__version__ = "0.0"

import os
import json

from config import Players_combo_collection
from src.player import Player

class TalanaKombat(object):
    players = []

    def __init__(self):
        # Set players data
        self.players = [Player("Tonyn Stallone"),
                        Player("Arnaldor Shuatseneguer", on_left_side=False)]
        self.players[0].combos_collection = Players_combo_collection[0]
        self.players[1].combos_collection = Players_combo_collection[1]


    def load_pressed_keys_json(self, filename: str):
        with open(filename, "r") as stream:
            try:
                fight_file = json.load(stream)
            except json.JSONDecodeError as err:
                print("ERROR: Bad JSON file: ")
                raise err
        # Parse the json data
        self.players[0].pressed_moves = fight_file.get("player1").get("movimientos")
        self.players[1].pressed_moves = fight_file.get("player2").get("movimientos")
        self.players[0].pressed_attacks = fight_file.get("player1").get("golpes")
        self.players[1].pressed_attacks = fight_file.get("player2").get("golpes")

    
    def run(self, input):
        pass

