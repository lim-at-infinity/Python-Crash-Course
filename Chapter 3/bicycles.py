bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) #printing the list w/o specifying the index prints the entire list, including brackes and apostophes
print(bicycles[0].title())
print(bicycles[3])
print(bicycles[3].title())
print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title() + "."

print(message)

#Try it yourself
cars = ['toyota', 'honda', 'ford', 'dodge']
message = "My first car was a " + cars[0].title() + " but I always wanted a " + cars[3].title() + "."

print("\n" + message)