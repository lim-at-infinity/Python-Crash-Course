buffet = ("sushi","ribs","ham","bacon","hotdog")
#buffet.append('danks')... will not work due to trying to modify tuple
print("This was the old menu:")
for food in buffet:
    print(food)

#Instead of trying to modify the existing tuple, the tuple was re-written
print("\nThis is the new hotness:")
buffet = ("sushi","ribs","ham","bacon","hotdog","danks")
for food in buffet:
    print(food)
    