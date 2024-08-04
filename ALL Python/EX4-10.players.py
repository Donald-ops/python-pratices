players = ['charles','martina','michael','florence','eli']

print("The first three items in the list are:")
for player in players[:3]:
    print(player)
    
print("\nThe three items from the middle of the list are:")
for player in players[1:4]:
    print(player)

print("\nThe last three items in the list are:")
for player in players[-3:]:
    print(player)

