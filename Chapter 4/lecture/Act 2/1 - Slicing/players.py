##Slicing
#Slicing allows for the output for multiple values in a list
players = ['charle','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
#w/o the first index, Python automically starts slice at beginning of list
print(players[:4])
#prints names starting at "michael", this is at index 2
print(players[2:])
#prints last 3 players, essentially does same thing as the previous line
print(players[-3:])

##Looping 
print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())
