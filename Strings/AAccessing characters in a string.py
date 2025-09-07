# Strings are indexed sequences. Positive indices start at 0 from the left; negative indices start at -1 from the right.
s = "Hello, World!"
print(s[0])    
print(s[4])

# Negative indexing
print(s[-1])
print(s[-5])

# String slicing
print(s[0:5])
print(s[7:11])

# String iteration
for char in s:
    print(char)


# Attempting to change the first character will raise an error
s = "Hello" + s[1:]
print(s)

# Deleting a string
del s

# Updating a string
s = "Hello, World!"
s = "J" + s[1:]
print(s)