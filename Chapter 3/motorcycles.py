motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print("\n")

#Replacing Elements on a List
print("###Replacing Elements on a List")
motorcycles[0] = 'ducati'
print(motorcycles)
print("\n")

###Addings Elements to a List - .append()
##Appending Eleemnts to the End of a List -- Appending is the simplest way to add a new element to a list
print("###Appending Elements")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati') #adds ducati to the end of the list w/o affecting the other elements
print(motorcycles)
print("\n")

#Appending to build an empty list - List are typically built this way, where each value input but the user is appended to an empty list
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)
print("\n")

##Inserting Elements into a List - .insert()
print("###Inserting Elements")
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati') #first argument indicates the index the second argument (the value) will be placed, shifting every other value to the right
print(motorcycles)
print("\n")

###Removing Elements from a List
##Removing Using the del Statement
print("###Element removal by del")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)
print("\n")

##Removing Using the pop() Method
#pop() removes the last item in a list, but it lets you work with that item after removing it 
print("###Element removal by .pop()")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print("The last motorcycle I owned was a " + popped_motorcycle.title() + ".")
#.pop() can also be used to pop from any position in the list
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle that I owned was a ' + first_owned.title() + '.')
print('\n')

##Removing item by value - .remove()
print("###Element removal by .remove()")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
print("\n")

#Using a .remove()'d element
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me")
#Note - .remove() only deletes the first occurance of the value if it occurs multiple times in a list
