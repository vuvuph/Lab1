import random

coinSide = ['H', 'T']
consecutiveFlips = []
count = 0

while True:
    flip = random.choice(coinSide)
    count += 1
    print(flip, end = " ")

    consecutiveFlips.append(flip)
    if len(consecutiveFlips) > 3:
        consecutiveFlips.pop(0)

    if len(consecutiveFlips) == 3 and consecutiveFlips[0] == consecutiveFlips[1] == consecutiveFlips[2]:
        print(f"({count} flips)")
        break