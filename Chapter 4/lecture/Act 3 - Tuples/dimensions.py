#tuples are immutable, meaning the program cannot alter the value
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#However, tuples cannot be modified, a new value can be assigned
print("\nOriginal:")
dimensions = (200,50)
for value in dimensions:
    print(value)

print("\nNew:")
dimensions = (400,10)
for value in dimensions:
    print(value)
