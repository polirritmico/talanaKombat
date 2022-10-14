#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__version__ = "0.0"

import os
import json

from src.player import Player

class TalanaKombat(object):
    players = []

    def __init__(self):
        player1_name = "Tonyn Stallone"
        player2_name = "Arnaldor Shuatseneguer"
        self.players = [Player(player1_name),
                        Player(player2_name, on_left_side=False)]


    def load_fight_json(self, filename: str):
        with open(filename, "r") as stream:
            try:
                fight_file = json.load(stream)
            except json.JSONDecodeError as err:
                print("ERROR: Bad JSON file: ")
                raise err

        # Parse the json data
        self.players[0].movements = fight_file.get("player1").get("movimientos")
        self.players[1].movements = fight_file.get("player2").get("movimientos")
        self.players[0].hits = fight_file.get("player1").get("golpes")
        self.players[1].hits = fight_file.get("player2").get("golpes")

    
    def run(self, input):
        pass

