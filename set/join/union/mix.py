# The union() method allows you to join a set with other data types, like lists or tuples.
# The result will be a set.


# Join a set with a tuple:

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)

print(z)