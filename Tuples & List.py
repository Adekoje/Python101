#Tuples
Tuple1 = ("disco",10,1.2)
print(Tuple1[0])
#result = disco
print(Tuple1[1])
#result = 10
print(Tuple1[2])
#result = 1.2
print(len(Tuple1))
#result = 3
print(Tuple1[0:2])
#reult = ('disco', 10)

Ratings = (10, 7, 8, 4, 6, 9, 5, 1, 2, 3)
print(sorted(Ratings))
#result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Nesting
NT = (1,2,('pop','rock'),(3,4),('disco',(1,2)))
print(NT[2])
#result = ('pop','rock')
print(NT[2][1])
#result = rock
print(NT[2][1][0])
#esult = r

#List
L = [1,2,['pop','rock'],[3,4],('disco',(1,2))]
print(L[0])
# The index conventions For list and Tuples are similar
L.extend(['jazz',10])
print(L)
#result = [1, 2, ['pop', 'rock'], [3, 4], ('disco', (1, 2)), 'jazz', 10]
L.append('folk')
print(L)
#result = [1, 2, ['pop', 'rock'], [3, 4], ('disco', (1, 2)), 'jazz', 10, 'folk']
L[1] = 3
print (L)
#result[1, 3, ['pop', 'rock'], [3, 4], ('disco', (1, 2)), 'jazz', 10, 'folk']
del(L[2])
print(L)
#reult = [1, 3, [3, 4], ('disco', (1, 2)), 'jazz', 10, 'folk']

A = 'hard work pays'
C = A.split(' ')
print (C)
#result = ['hard', 'work', 'pays']

B=["a","b","c"]
print(B[1:])
#result=['b', 'c']
