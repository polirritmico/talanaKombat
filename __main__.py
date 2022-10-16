#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Eduardo Bray (ejbray@uc.cl)

import sys
import traceback
from src.talanaKombat import TalanaKombat

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Check usage: ./talanaKombat.py FILENAME")
        sys.exit()
    filename = sys.argv[1]
    try:
        talanaKombat = TalanaKombat()
        talanaKombat.load_pressed_keys_json(filename)
        talanaKombat.run()
        sys.exit()
    except Exception:
        print("Catched exception: \n  {}".format(traceback.format_exc()))
        print("Closing TalanaKombat...")
        sys.exit()

