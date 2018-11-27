import random

def main():
    pick_total = int(input("How many quick picks? "))
    for i in range(pick_total):
        picks = []
        for j in range(6):
            pick = random.randrange(46)
            while pick in picks:
                pick = random.randrange(46)
            picks.append(pick)
            if j == 5:
                picks.sort()
                print(picks)




main()