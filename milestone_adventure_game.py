'''
Author: Kevin Ligan
Purpose: Project Milestone - Adventure Game
'''

print()
# Text-based adventure game
# with three levels of choices

print('Welcome to the Adventure Game!')

# First scenario
print('\nYou are in a forest and find a path that forks in two directions.')
print('\nDo you want to go LEFT or RIGHT?')

user_input = input().lower()

if user_input == 'left':
    # Second scenario
    print('\nYou see a river blocking your path.')
    print('\nDo you want to SWIM across or FOLLOW the river to find a BRIDGE?')
    
    user_input = input().lower()
    
    if user_input == 'swim':
        # Third scenario
        print('\nYou made it across the river safely but now you are soaking wet.')
        print('\nDo you want to make a FIRE or keep moving to try and DRY OFF?')
        
        user_input = input().lower()
        
        if user_input == 'fire':
            print('\nYou successfully made a fire and dried off. Congratulations, you won the game!')
        elif user_input == 'dry off':
            print('\nYou walked around trying to dry off but eventually caught a cold and lost the game.')
        else:
            print('\nInvalid choice. You lost the game.')
    elif user_input == 'follow':
        # Third scenario
        print('\nYou followed the river and found a bridge. However, there is a troll guarding it.')
        print('\nDo you want to FIGHT the troll or try to SNEAK past it?')
        
        user_input = input().lower()
        
        if user_input == 'fight':
            print('\n\You fought the troll and won! Congratulations, you won the game!')
        elif user_input == 'sneak':
            print('\nYou successfully snuck past the troll and crossed the bridge. Congratulations, you won the game!')
        else:
            print("\nInvalid choice. You lost the game.")
    else:
        print('\nInvalid choice. You lost the game.')
print()