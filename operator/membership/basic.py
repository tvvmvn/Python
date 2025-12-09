#  Membership Operators
# Membership operators are used to test if a sequence is presented in an object:


# Operator|Description|Example
# in |Returns True if a sequence with the specified value is present in the object|x in y|
# not in|Returns True if a sequence with the specified value is not present in the object|x not in y

# Check if "banana" is present in a list:
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("pineapple" not in fruits)