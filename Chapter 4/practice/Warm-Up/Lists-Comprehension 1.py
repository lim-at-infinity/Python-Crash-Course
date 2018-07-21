#List
bands = ['The Smiths','Arctic Monkeys','Green Day']
print("These are some of my favorite bands... ")
for value in bands:
    print(value)

#Numerical List
print("\nHere is a list of numbers:")
for value in range(1,11):
    print(value)

#Numerical List Squared
print("List squared:")
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

#Numerical List using comprehension
print("Using comprehension:")
squares = [value**2 for value in range(1,11)]

print (squares)

