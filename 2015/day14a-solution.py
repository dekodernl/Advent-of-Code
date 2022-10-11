#!/usr/bin/python
def reindeer(name, speed, duration, rest, stop):
    distance = 0
    time = 0
    _d = 0
    _r = 0
    while time < stop:
        while _d < duration and time < stop:
            distance += speed
            time += 1
            _d += 1
        _d = 0
        while _r < rest and time < stop:
            _r += 1
            time += 1
        _r = 0

    return dict(reindeer=name, distance=distance)

stop = 2503

reindeer_enrolled = [
    ("Rudolph", 22, 8, 165, stop),
    ("Cupid", 8, 17, 114, stop),
    ("Prancer", 18, 6, 103, stop),
    ("Donner", 25, 6, 145, stop),
    ("Dasher", 11, 12, 125, stop),
    ("Comet", 21, 6, 121, stop),
    ("Blitzen", 18, 3, 50, stop),
    ("Vixen", 20, 4, 75, stop),
    ("Dancer", 7, 20, 119, stop)
]

results = []
furthest = ()
for enrollee in reindeer_enrolled:
    result = reindeer(*enrollee)
    results.append(result)


print("The results are in:")
sorted_results = sorted(results, key=lambda k: k['distance'], reverse=True)
for i, r in enumerate(sorted_results):
    print("#%s - %s (%sm)" % (i, r['reindeer'], r['distance']) )
print()
print("The winnar is: %s !!!" % sorted_results[0]['reindeer'])
