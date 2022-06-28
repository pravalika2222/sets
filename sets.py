#        "sets" 
# a={}      
# print(a,type(a))     # it is a dict set (which is empty set)

# p={1,4.5,'hello',('hi',3)}
# print(p,type(p))       # it is a set

# n={10,20,30}
# print(n[1])    # 'set' object is not subscription

    #    "frozen set"
#     'we cannot add or remove the element in frozenset'
# d={1,4,6}   
# e=frozenset(d)
# print(e[0])    # frozenset object is not subscription

#           "methods of sets"
# a={1,4,7,8}   # it is a add type
# b='prava',1,6   # we r adding a in to b 
# a.add(b)
# print(a)    #  {1, 4, ('prava', 1, 6), 7, 8}

# c={1,7,9}  #  it is a clear set 
# c.clear()
# print(c)   # set()

# a={1,3,5} ; b={3,4,3,5}; c={10,40,5} ; d={1,73,10}   # it is a intersection type
# # print(a.intersection(b))    #  {3,5} 
# # print(b.intersection(c))    #  {5}
# # print(c.intersection(d))    #   {10,5}
# print(b.intersection(d))      #  (it is empty bcoz b intersection d it doesn't have common elements so, it is a set())

# a={1,2,'prava',5}  # it is a union set
# b={5,8,'hi'}
# print(a.union(b))  # {1, 2, 'prava', 'hi', 5, 8} union means  the same answer will come
# print(b.union(a))   #  {1, 2, 'prava', 'hi', 5, 8}

# a={1,2,3}; b={4,3,5};c={4,3,7}   # it is a update set
# # a.update(b)       # {1, 2, 3, 4, 5}
# # a.update(c)         # {1, 2, 3, 4, 7}
# print(a)

# a={20,30,10}   # it is adifference set 
# b={10,35,20}
# # print(a.difference(b))    #   {30}   the difference value be come in o/p
# # print(b.difference(a))      #  {35}
# # print(a-b)    # {30}
# print(b-a)      # {35}

# p={1,2,3,7,8} # it is a discard set
# # p.discard(3)    # {1, 2, 7, 8}  when we give the input value as discard then the value discard
# p.discard(5)     # {1, 2, 3, 7, 8} when we not give input value as discard then the same input may come
# print(p)

# v={4,5,6,7}  # it is a pop set
# v.pop()
# print(v)   # {5, 6, 7} it remove the value a random item in the given input set

# a={1,2,3,4};b={3,4,6};c={5,2,8}  # it is a isdisjoint set
# # print(a.isdisjoint(b))   # false (bcoz the two sets are have same elements)
# # print(b.isdisjoint(c))  # true  (bcoz if two sets are different elements then it is true)
# print(a.isdisjoint(c))    # false 

# a={1,2,3};b={1,2,3,4,5};c={1,2,4,5}   # it is a issubset
# # print(a.issubset(b))  # true  
# # print(b.issubset(c))   # false 
# print(c.issubset(a))    #  false


