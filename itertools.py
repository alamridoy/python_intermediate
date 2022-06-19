# itertools: product , permutations, combinations, accumulate , groupby and infinate iterator

# from itertools import product #matrix type multiplications
# a = [1,2,3]
# b = [4,5,6]
# prod = product(a,b)
# print(list(prod))

# from itertools import permutations
# a = [4,5,6]
# perm = permutations(a,3)
# print(list(perm))

# from itertools import combinations , combinations_with_replacement
# a = [1,2,3,4]

# comb = combinations(a,2)
# print(list(comb))

# comb_rep = combinations_with_replacement(a,2)
# print(list(comb_rep))

# from itertools import accumulate
# import operator
# a = [1,2,6,3,4]
# acc = accumulate(a, func = operator.mul)
# print(a)
# print(list(acc))
 
 
# from itertools import groupby


# def smaller_than_3(x):
#     return x < 3 

# a = [1,2,3,4,5]

# grp_obj = groupby(a, key=lambda x:x <3)

# for key,value in grp_obj:
#     print(key,list(value))
    
    
from itertools import count , cycle,repeat

# for i in count(5): # starts 5 and infinite loops
#     print(i)
#     if i == 10:
#         break
# a = [1,2,3]
# # for i in cycle(a):
# #     print(i)

# for i in repeat(1):
#     print(i)