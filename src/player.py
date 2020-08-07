# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, room, inventory = []):
        self.room = room
        self.inventory = inventory
    def print_inventory(self):
        print('Inventory:\n')
        for item in self.inventory:
            print(item.name)
        