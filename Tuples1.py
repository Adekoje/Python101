tuple1 = ('disco', 10, 1.2)
tuple1
print(type(tuple1)) # <class 'tuple'>

#Each element in atuple can be accessed via am index
print(tuple1[1])
#result = 10
print(type(tuple1[0])) #<class 'str'>

#Negative indexing can also be used
print(type(tuple1[-3])) #<class 'str'>

#CONCATENATE TUPLES
tuple2 = tuple1 + ('hard rock', 10)
print(tuple2) # ('disco', 10, 1.2, 'hard rock', 10)

#SLICING TUPLES
tuple2[0:3]
print(tuple2[0:3]) # ('disco', 10, 1.2)
tuple2[3:5]
print(tuple2[3:5]) #('hard rock', 10)

#SORTING TUPLES
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
RatingsSorted = sorted(Ratings)
print(RatingsSorted) #[0, 2, 5, 6, 6, 8, 9, 9, 10

#NESTED TUPLES

NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
print("Element 2 of Tuple: ", NestedT[2]) #Element 2 of Tuple:  ('pop', 'rock')
print("Element 0 of Tuple: ", NestedT[0]) #Element 0 of Tuple:  1
print('Element 4,0 of Tuple:', NestedT[4][0]) #Element 4,0 of Tuple: disco
print(NestedT[4][1][0]) #1
print(NestedT.index((3,4))) #3

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", "R&B", "progressive rock", "disco")
print(len(genres_tuple)) #8
print(genres_tuple[3]) #hard rock
print(genres_tuple[3:6]) #('hard rock', 'soft rock', 'R&B')
print(genres_tuple[7][0])  #d
print(genres_tuple.index("disco")) #7

C_tuple=(-5, 1, -3)
C_Sorted = sorted(C_tuple)
print(C_Sorted)
