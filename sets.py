def union(a, b):
    return a[:] + [ j for j in b if j not in a ]

def intersection(a, b):
    return [ i for i in a if i in b ]

def set_difference(a, b):
    return [ i for i in a if i not in b ]

def symmetric_difference(a, b):
    return set_difference(union(a, b), intersection(a, b))

def cartesian_product(a, b):
    return [(i, j) for i in a for j in b ]

a = range(1, 11)
b = range(3, 27, 2)
print "a:   " + str(a)
print "b:   " + str(b)

print "----------------------------------------"

print "union:  " + str(union(a, b))
print "intersection:  " + str(intersection(a, b))
print "set difference:  " + str(set_difference(a, b))
print "symmetric difference:  " + str(symmetric_difference(a, b))
print "cartesian product:  " + str(cartesian_product(a, b))
