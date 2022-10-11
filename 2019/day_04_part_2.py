"""._.                        .__.__                  ._.
   | |    ____________   ____ |__|  |   ___________   | |
   | |   /  ___/\____ \ /  _ \|  |  | _/ __ \_  __ \  | |
    \|   \___ \ |  |_> >  <_> )  |  |_\  ___/|  | \/   \|
    __  /____  >|   __/ \____/|__|____/\___  >__|     ___
    \/       \/ |__|                       \/         """

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections

password_count = 0
for num in range(138307, 654505):
    str_num = str(num)
    count_double = collections.Counter(str_num)
    contains_double = (
        len({x: count_double[x] for x in count_double if count_double[x] == 1}) > 0
    )
    increasing = True
    cursor = 0
    lnum = [int(x) for x in str(num)]
    while cursor < len(lnum) - 1 and increasing is True:
        if lnum[cursor] > lnum[cursor + 1]:
            increasing = False
        cursor += 1
    if increasing and contains_double:
        password_count += 1

print(password_count)
