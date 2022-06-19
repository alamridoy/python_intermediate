# collections : Counter, namedTuple , OrderedDict , defaultdict, deque.

# from collections import Counter 

# str = "aaaabbbbcc"
# my_counter = Counter(str)
# print(my_counter.items())

# from collections import namedtuple  #nameTuple easy to create lightweight object type
# point = namedtuple('Point','x,y')
# pt = point(1,-4)
# print(pt) 
# from collections import OrderedDict
# ordered_dict = {}
# ordered_dict['a'] = 1
# ordered_dict['b'] = 2
# ordered_dict['c'] = 3
# ordered_dict['d'] = 4
# ordered_dict['e'] = 5
# print(ordered_dict)

# from collections import defaultdict

# d = defaultdict(int)
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3

# print(d['a'],d['b'])

# from collections import deque

# d = deque()
# d.append(1)
# d.append(2)
# d.append(3)

# print(d)

# d.appendleft(5)
# print(d)

# d.popleft()
# print(d)

# d.extendleft([6,7,8])
# print(d)

# d.rotate(-1)
# print(d)
