from itertools import permutations as perms
from beepy import beep

def make_combos(containers, combo):
    high = 150
    working_combos = []
    container = [containers[n] for n in combo]
    sum_container = sum(container)
    if sum_container == high:
        working_combos.append(combo)
        print(container)
    elif sum_container < high:
        sub_combos = []
        for i in range(0, len(containers)):
            if i not in combo:
                _combo = combo[:]
                _combo.append(i)
                sub_combos = make_combos(containers, _combo)
                for sc in sub_combos:
                    working_combos.append(sc)
    return working_combos

def solution():
    containers = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40]
    #containers = [20,15,10,5,5] 
    working_combos = make_combos(containers, [])
    valid_combos = []
    for wc in working_combos:
        if sorted(wc) not in valid_combos:
            valid_combos.append(sorted(wc))

    for vc in valid_combos:
        print([containers[i] for i in vc])

    print(len(valid_combos))
    beep(sound=5)

solution()
