import random

trials = 1000000

result = 0

def done(x):
    if x.count("g") > 1:
        return 1
    if x.count("r") > 1:
        return 1


for i in range(trials):
    ls =["r", "r", "r", "r", "g", "g", "g"]
    
    table = []

    while not done(table):
        table.append(random.sample(ls, k=1)[0])
    
    if (table.count("g") >= 1 and table.count("r") >= 1):
        result += 1
    

print(result/trials)
