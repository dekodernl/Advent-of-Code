import operator

def race(reindeer, stop):
    names = [r[0] for r in reindeer]
    timeline = {}
    distance = {}
    score = {}
    for name, speed, duration, pause in reindeer:
        timeline[name] = []
        distance[name] = 0
        score[name] = 0
        while len(timeline[name]) < stop:
            for d in range(0, duration):
                distance[name] += speed
                timeline[name].append(distance[name])
            for p in range(0, pause):
                timeline[name].append(distance[name])

    for t in range(0, stop):
        current = []
        for n in names:
            current.append(dict(name=n, pos=timeline[n][t]))
        
        leader = sorted(current, key=lambda k: k['pos'], reverse=True)[0]
        score[leader.get('name')] += 1

    winnar = max(score, key=score.get)
    return (winnar, score[winnar])

stop = 2503

reindeer_enrolled = [
    ("Rudolph", 22, 8, 165),
    ("Cupid", 8, 17, 114),
    ("Prancer", 18, 6, 103),
    ("Donner", 25, 6, 145),
    ("Dasher", 11, 12, 125),
    ("Comet", 21, 6, 121),
    ("Blitzen", 18, 3, 50),
    ("Vixen", 20, 4, 75),
    ("Dancer", 7, 20, 119)
]

result = race(reindeer_enrolled, stop)
print("The winnar is: %s with %d points!!!" % (result[0], result[1]))
