"""._.                        .__.__                  ._.
   | |    ____________   ____ |__|  |   ___________   | |
   | |   /  ___/\____ \ /  _ \|  |  | _/ __ \_  __ \  | |
    \|   \___ \ |  |_> >  <_> )  |  |_\  ___/|  | \/   \|
    __  /____  >|   __/ \____/|__|____/\___  >__|     ___
    \/       \/ |__|                       \/         """

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from day_02_puzzle_input import puzzle_input

puzzle_input[1] = 12
puzzle_input[2] = 2
puzzle_inputlen = len(puzzle_input)
opdex = 0

while puzzle_input[opdex] != 99:
    if puzzle_input[opdex] == 1:
        a = puzzle_input[puzzle_input[(opdex + 1)]]
        b = puzzle_input[puzzle_input[(opdex + 2)]]
        opdex_write = puzzle_input[opdex + 3]
        if opdex_write > puzzle_inputlen:
            opdex_write = 0
        puzzle_input[opdex_write] = a + b
    elif puzzle_input[opdex] == 2:
        a = puzzle_input[puzzle_input[(opdex + 1)]]
        b = puzzle_input[puzzle_input[(opdex + 2)]]
        opdex_write = puzzle_input[opdex + 3]
        if opdex_write > puzzle_inputlen:
            opdex_write = 0
        puzzle_input[opdex_write] = a * b
    opdex += 4

print(puzzle_input[0])
