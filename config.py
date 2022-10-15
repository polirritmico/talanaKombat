#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.combo import Combo

# --- Set Players Combos -----------------------------------------------------
Player1_combo_collection = [
            Combo("Taladoken", 3, ("DSD", "P")),
            Combo("Remeyuken", 2, ("SD", "K")),
            Combo("Puño", 1, ("", "P")),
            Combo("Patada", 1, ("", "K"))
        ]

Player2_combo_collection = [
            Combo("Remuyuken", 3, ("SA", "K")),
            Combo("Taladoken", 2, ("ASA", "P")),
            Combo("Puño", 1, ("", "P")),
            Combo("Patada", 1, ("", "K")),
        ]

Players_combo_collection = [Player1_combo_collection,
                            Player2_combo_collection]
