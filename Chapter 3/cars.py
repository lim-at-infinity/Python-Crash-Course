cars = ['bmw','audi','toyota','subaru']

#Permanently sort lists
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
cars.sort()
print(cars)

print("\nHere is the sorted list in reverse")
cars.sort(reverse=True)
print(cars)

#Temporarily sort lists
print("\nLets reset")
cars = ['bmw','audi','toyota','subaru']
print(cars)

print("\nHere's that sorted list again")
print(sorted(cars))

print("\nAnd here's the original list.. again!")
print(cars)

#Finding the length of a lists
#Note: Have to add str() to carCout in order to avoid type error
carCount = len(cars)
print("\nThere are " + str(carCount) + " cars in our list")
