"""._.                        .__.__                  ._.
   | |    ____________   ____ |__|  |   ___________   | |
   | |   /  ___/\____ \ /  _ \|  |  | _/ __ \_  __ \  | |
    \|   \___ \ |  |_> >  <_> )  |  |_\  ___/|  | \/   \|
    __  /____  >|   __/ \____/|__|____/\___  >__|     ___
    \/       \/ |__|                       \/         """

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from day_01_puzzle_input import puzzle_input

print(sum([int((int(mass) / 3)) - 2 for mass in puzzle_input]))
