# add in item class [x]
# item will have name and description - should be 1 word [x]
# ability to add items to room 
class Item:
  def __init__(self, name, description, in_room=None):
    self.name = name
    self.description = description
    # self.in_room = in_room ???

  def __str__(self):
    return f'{self.name}: {self.description}'

