

# Declare all the s
# dictionaries of s
# can get rid of the dict  = {} and make each into variables
'outside' =  ("Outside Cave Entrance", "North of you, the cave mount beckons")

'foyer' = ("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""")

'overlook' = ("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

'narrow' = ("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

'treasure' = ("Treasure Chamber", """You've found the long-lost treasure
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

#
# Main
#

# Make a new player object that is currently in the 'outside' .
player = Player('Dulfy the Great',)
player.current_ = outside
print(player.current_)
# Write a loop that:
while True:
# * Prints the current  name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the  there.
    if variable == 'n':
        # check if the current  has a n_to attribute
        if hasattr(player.current_, f'{variable}_to'):
        # or can do 4 if statements if player.current_.n_to is not None:
        # 2-4 ifs need to be elif
        # add other if statements to handle wrong directions
            # move player to 
            player.current_ = getattr(player.current_ f'{variable}_to')
            # or can do 4 statements of player.current_ = player.current_.n_to
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
