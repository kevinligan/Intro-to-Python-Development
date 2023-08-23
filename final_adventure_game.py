'''
Author: Kevin Ligan
Purpose: Project final- Adventure Game
'''

print()
# Text-based adventure game
# with three levels of choices

print('Welcome to the Adventure Game!')

print('\nYou are in a forest and find a path that forks in two directions.')
#Added a third option for creativity, all scenarios has also third options that the gamer can choose for creativity
print('\nDo you want to go LEFT, RIGHT, or take a THIRD option?')

user_input = input().lower()

if user_input == 'left':
    # Second scenario
    print('\nYou see a river blocking your path.')
    print('\nDo you want to SWIM across, FOLLOW the river, or use a BOAT?')
    
    user_input = input().lower()
    
    if user_input == 'swim':
        # Third scenario
        print('\nYou made it across the river safely but now you are soaking wet.')
        print('\nDo you want to make a FIRE, keep moving to try and DRY OFF, or SHAKE like a dog?')
        
        user_input = input().lower()
        
        if user_input == 'fire':
            print('\nYou successfully made a fire and dried off. Congratulations, you won the game!')
        elif user_input == 'dry off':
            print('\nYou walked around trying to dry off but eventually caught a cold and lost the game.')
        elif user_input == 'shake':
            print('\nYou shook like a dog, splashing water everywhere and surprisingly drying off quickly. Congratulations, you won the game!')
        else:
            print('\nInvalid choice. You lost the game.')
    elif user_input == 'follow':
        # Third scenario
        print('\nYou followed the river and found a bridge. However, there is a troll guarding it.')
        print('\nDo you want to FIGHT the troll, try to SNEAK past it, or BRIBE the troll?')
        
        user_input = input().lower()
        
        if user_input == 'fight':
            print('\nYou fought the troll and won! Congratulations, you won the game!')
        elif user_input == 'sneak':
            print('\nYou successfully snuck past the troll and crossed the bridge. Congratulations, you won the game!')
        elif user_input == 'bribe':
            print('\nYou offered the troll a shiny gem, and it happily let you pass. Congratulations, you won the game!')
        else:
            print("\nInvalid choice. You lost the game.")
    elif user_input == 'boat':
        # Third scenario
        print('\nYou found a hidden boat nearby and sailed across the river. Congratulations, you won the game!')
    else:
        print('\nInvalid choice. You lost the game.')
        
elif user_input == 'right':
    # Second scenario
    print('\nYou see a cave in front of you.')
    print('\nDo you want to ENTER the cave, keep WALKING on the path, or CLIMB a nearby tree?')
    
    user_input = input().lower()
    
    if user_input == 'enter':
        # Third scenario
        print('\nYou entered the cave and found a treasure chest. However, there is a trap.')
        print('\nDo you want to OPEN the chest, try to DISARM the trap, or IGNORE the chest?')
        
        user_input = input().lower()
        
        if user_input == 'open':
            print('\nYou opened the chest and found a diamond! Congratulations, you won the game!')
        elif user_input == 'disarm':
            print('\nYou successfully disarmed the trap and opened the chest. Congratulations, you won the game!')
        elif user_input == 'ignore':
            print('\nYou decided to ignore the chest and continued your journey. Congratulations, you won the game!')
        else:
            print('\nInvalid choice. You lost the game.')
    else:
        print('\nInvalid choice. You lost the game.')
        
else:
    print('\nInvalid choice. You lost the game.')

    print()