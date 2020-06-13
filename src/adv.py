from room import Room
from player import Player

# Declare all the s
# dictionaries of s
outside =  Room("Outside Cave Entrance", "North of you, the cave mount beckons")

foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""")

overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")



# Link s together
# can remove [] for easier way to read

outside.n_to = foyer
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow

# Main

# Make a new player object that is currently in the 'outside' .
player = Player('Dulfy the Great')
player.current_room = outside
print(player.name)

# Write a loop that:
while True:
# * Prints the current room name
    print(player.current_room.name)
# * Prints the current description (the textwrap module might be useful here).
    print(f'{player.current_room.description}')
# * Waits for user input and decides what to do.
    player_input = input('Choose a direction :' + '\n')
# If the user enters a cardinal direction, attempt to move to the  there.
    
    if player_input == 'n':
        # check if the current room has a n_to attribute
        if player.current_room.n_to is not None:
            player.current_room = player.current_room.n_to

    elif player_input == 's':
        if player.current_room.s_to is not None:
            player.current_room = player.current_room.s_to

    elif player_input == 'e':
        if player.current_room.e_to is not None:
            player.current_room = player.current_room.e_to

    elif player_input == 'w':
        if player.current_room.w_to is not None:
            player.current_room = player.current_room.w_to

    # If the user enters "q", quit the game.
    elif player_input == 'q':
        break

    # Print an error message if the movement isn't allowed.
    else: # player_input not in ('n', 's', 'w', 'e'):
        print('Incorrect input, try another direction')
