# You can loop through a dictionary by using a for loop.

# When looping through a dictionary, 
# the return value are the keys of the dictionary, 
# but there are methods to return the values as well.


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)


# Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])