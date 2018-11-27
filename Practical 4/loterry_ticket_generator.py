import random

def main():
    pick = int(input("How many quick picks? "))
    for i in range(pick):
        picks = []
        for j in range(6):
            picks.append(random.randrange(46))
            if j == 5:
                while(picks[0] == picks[1] or picks[0] == picks[2] or picks[0] == picks[3] or picks[0] == picks[4] or picks[0] == picks[5]):
                    picks[0] = random.randrange(46)
                while(picks[1] == picks[2] or picks[1] == picks[3] or picks[1] == picks[4] or picks[1] == picks[5]):
                    picks[1] = random.randrange(46)
                while(picks[2] == picks[3] or picks[2] == picks[4] or picks[2] == picks[5]):
                    picks[2] = random.randrange(46)
                while (picks[3] == picks[4] or picks[3] == picks[5]):
                    picks[3] = random.randrange(46)
                while (picks[4] == picks[5]):
                    picks[3] = random.randrange(46)
                picks.sort()
                print(picks)




main()