import random
f = open('MobyDick.txt','r')
follow_words = dict()

for line in f:
    linewords = line.split()
    for i in range(len(linewords)-1):
        if linewords[i] in follow_words:
            follow_words[linewords[i]].append(linewords[i+1])
        else:
            follow_words[linewords[i]] = [linewords[i+1]]


lastword = random.choice(list(follow_words))
for i in range(200):
    print(lastword, end=' ')
    if lastword in follow_words:
        lastword = random.choice(follow_words[lastword])
    else:
        lastword = random.choice(list(follow_words))
