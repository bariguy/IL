import random
trials = 100000

ls = []

for i in range(trials):
    randomlist = random.sample(range(1, 9), 5)

    count = 0
    a = randomlist[0]
    b = randomlist[1]
    c = randomlist[2]
    d = randomlist[3]
    e = randomlist[4]

    answer = []

    if a*(b**4)*(c**6)*(d**4)*e == 9953280000:
        if [randomlist] not in ls:
              ls.append([randomlist])
        count +=1
        print(ls)








