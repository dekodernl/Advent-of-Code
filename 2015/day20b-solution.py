#!/usr/bin/python3
import time
def main():
    elves = {}
    max_presents = 34000000
    house = 1
    while True:
        presents = 0
        factors = set()
        for i in range( 1, ( int( house ** 0.5 ) + 1 ) ):
            if house % i == 0:
                factors.add(i)
                factors.add(house//i)
        for elf in factors:
            if elf not in elves:
                elves[elf] = 0

            if elves[elf] <= 50:
                elves[elf] += 1
                presents += (elf * 11)

        if presents >= max_presents:
            print(f"Part 2: House {house} = {presents}")
            break
        house +=1

        # 720720 too low

if __name__ == "__main__":
    print("Starting to solve day 20 - Part 2")
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
