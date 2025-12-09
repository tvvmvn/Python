# Identity operators are used to compare the objects, 
# not if they are equal, but if they are actually the same object, 
# with the same memory location:

# Operator|Description|Example|Try it
# is |Returns True if both variables are the same object|x is y|
# is not|Returns True if both variables are not the same object|x is not y


# The is operator returns True if both variables point to the same object:
# The is not operator returns True if both variables do not point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # True
print(x is y) # False
print(x == y) # True

# Difference Between is and ==

# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal