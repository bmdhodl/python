import random

numberOfStreaks = 0
y = 0
for experimentNumber in range(10000):
    tOf = ['T', 'F']
    x = random.choice(tOf)

    if x[0] == x[-1]:
        y += 1
        if y > 6:
            numberOfStreaks += 1
            y = 0

    

print('Chance of streaks: %s%%' % (numberOfStreaks / 100))