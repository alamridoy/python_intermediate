# lambda arguments: expression


# add = lambda x: x +10

# print(add(8))


# def addsum(x):
#     return x + 10

# print(addsum(5))




# mul = lambda x,y : x*y
# print(mul(10,4))

# point2d = [(1,2),(6,2),(-7,4),(9,2)]

# point2d_sorted = sorted(point2d, key = lambda x: x[0] +  x[1])

# print(point2d)
# print(point2d_sorted)

'''
 
 map  function
 map(fun, seq)
 
 
'''
# a= [1,2,3,4,5]
# m = map(lambda x: x*2, a) #map used
# print(list(m)) 

# c = [x*2 for x in a] # list comprehension
# print(c)

'''
 
filter function
filter(fun, seq)
 
 
'''

# a= [1,2,3,4,5]
# m = filter(lambda x: x%2==0, a) #map used
# print(list(m)) 

'''
 
reduce function
reduce(fun, seq)
 
 
'''

# from functools import reduce

# a = [1,2,3,4]

# pro = reduce(lambda x,y: x*y,a)
# print(pro)