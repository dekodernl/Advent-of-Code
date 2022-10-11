#!/usr/bin/python3
import time
def main():
    max_presents = 34000000
    house = 1
    while True:
        factors = set()
        for i in range( 1, ( int( house ** 0.5 ) + 1 ) ):
            if house % i == 0:
                factors.add(i)
                factors.add(house//i)
        presents = sum(factors) * 10
        if presents >= max_presents:
            print(f"Part 1: House {house} = {presents}")
            break
        house +=1

if __name__ == "__main__":
    print("Starting to solved day 20 - Part 1")
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
