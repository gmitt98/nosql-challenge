import copy
one = 'abc'
two = one
print(two, one)
one = 'def'
print (two, one)
two = copy.deepcopy((one))
one = 'xyz'
print(two, one)
two = one
print(two, one)
one = 'kajsalkdsj'
print(two, one)