guests = ['Stan Lee', 'George Washington', 'Jimmy Hendrix']
print(guests)
print("Welcome, " + guests[0] + ", " + guests[1] + ", and " + guests[2] + "! You are all invited to dinner.")

flake = guests.pop(1)
replaceGuest_1 = 'Alex Jones'
guests.insert(1, replaceGuest_1)
print("\nIt looks like " + flake + " can't make it. Too bad!")
print("Guess I'll just invite " + guests[1] + ".")
print(guests)

newGuest_1 = "Kara Danvers"
newGuest_2 = "Flash Thompson"
newGuest_3 = "Dick Grayson"

guests.insert(0, newGuest_1)
guests.insert(2, newGuest_2)
guests.append(newGuest_3)
print(guests)
print("\nDear " + newGuest_1 + ", you are invited to our super exclusive dinner. Please come, I am deathly lonely.")
print("Dear " + newGuest_2 + ", you are invited to our super exclusive dinner. Please come, I am deathly lonely.")
print("Dear " + newGuest_3 + ", you are invited to our super exclusive dinner. Please come, I am deathly lonely.")
print("\n")

kickedOut = guests.pop()
print("Hey " + kickedOut + ", sorry but looks like there's not going to be enough room. You are uninvited :^)")
kickedOut = guests.pop()
print("Hey " + kickedOut + ", sorry but looks like there's not going to be enough room. You are uninvited :^)")
kickedOut = guests.pop()
print("Hey " + kickedOut + ", sorry but looks like there's not going to be enough room. You are uninvited :^)")
kickedOut = guests.pop()
print("Hey " + kickedOut + ", sorry but looks like there's not going to be enough room. You are uninvited :^)")

print(guests[0] + " and " + guests[1] + " are still invited tho...")
del guests[1]
del guests[0]
print(guests)