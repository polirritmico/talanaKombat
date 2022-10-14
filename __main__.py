#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Eduardo Bray (ejbray@uc.cl)

import sys
from src.talanaKombat import TalanaKombat

if __name__ == "__main__":
    talanaKombat = TalanaKombat()
    try:
        #talanaKombat.load_fight_file()
        sys.exit(talanaKombat.run(sys.argv[1:]))
    except Exception as err:
        print("Catched exception: \n  {}\nClosing TalanaKombat".format(err))
        sys.exit()

