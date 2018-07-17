#for loop to build a list
print("v.1 - 3 lines")
squares = []

for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

#same loop but combines 4th and 5th lines of code
print("\nv.2 - 2 lines")
squares = []

for value in range(1,11):
    squares.append(value**2)
print(squares)

#using list comprehensions to conduct the same loop using only one line
print("\nv.3 - 1 line")
squares = [value**2 for value in range(1,11)]
print(squares)

#using min(), max(), and sum() to easily find data
print("\nThe min, max, and sum of the squares:")
print(min(squares))
print(max(squares))
print(sum(squares))

