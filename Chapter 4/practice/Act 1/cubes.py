print("Using comprehension:")
cubes = [value**3 for value in range(1,11)]
print(cubes)

print("\nNormal way:")
cubes = list(range(1,11))

for values in cubes:
    print(values**3)