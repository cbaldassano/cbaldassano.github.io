students = 'Brian Li Chris Qiu Daniel Wang ' + \
           'Raymond Xiong Prathmann Arora'

names = students.split()
for i in range(0,len(names),2):
    print(names[i][0] + names[i+1][0])
