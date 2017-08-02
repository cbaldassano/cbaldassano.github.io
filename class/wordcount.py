textfile = open('MobyDick.txt')
wordcounts = dict()

for textline in textfile:
    linewords = textline.split()
    for word in linewords:
        if word in wordcounts:
            wordcounts[word] += 1
        else:
            wordcounts[word] = 1
