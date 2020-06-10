# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
      self.name = name
      self.current_room = current_room
      self.move_room = []

    def __str__(self):
      return f'Welcome {self.name}! You are currently in the {self.current_room}'

player1 = Player('Dulfy the Great', 'Foyer')

print(player1)

