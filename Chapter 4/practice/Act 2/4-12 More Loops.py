#4-11 but using for loops to output za's(in Progress)
pizzaList = ['pineapple','pepporinno','hotdog','ham']
my_pizza = [pizza for pizza in pizzaList[:2]]
fren_pizza = [pizza for pizza in pizzaList[-2:]]


my_pizza.append('sausage')
fren_pizza.append('anchovi')

print("My favorite za's are: " + str(my_pizza) + "...")
print("My friend's trashy pizza taste is " + str(fren_pizza))

for pizza in pizzaList:
    print(pizza)

