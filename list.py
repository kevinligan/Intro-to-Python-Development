friends = []

# Prompt the user to enter the names of friends
while True:
    friend_name = input("Type the name of a friend: ")
    
    # Check if the user entered "end" to stop entering names
    if friend_name.lower() == "end":
        break
    
    # Add the friend to the list
    friends.append(friend_name)

# Print the list of friends
print("Your friends are:")
for friend in friends:
    print(friend)