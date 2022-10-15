#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Eduardo Bray (ejbray@uc.cl)

import sys
from src.talanaKombat import TalanaKombat

if __name__ == "__main__":
    talanaKombat = TalanaKombat()
    filename = sys.argv[1] if len(sys.argv[1:]) == 1 else "test/fight_case1.json"
    try:
        talanaKombat.load_pressed_keys_json(filename)
        sys.exit(talanaKombat.run())
    except Exception as err:
        print("Catched exception: \n  {}\nClosing TalanaKombat".format(err))
        sys.exit()

