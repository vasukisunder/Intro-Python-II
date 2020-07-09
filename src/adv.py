from room import Room
from player import Player
from item import Item

# Declare all the rooms
item = {
    'SWORD': Item('SWORD', ''),
    'COINS': Item('COINS', ''),
    'SHIELD': Item('SHIELD', ''),
    'BOOK': Item('BOOK', '')
}
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['SWORD']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item['BOOK']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item['SHIELD'], item['COINS']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

print('\nWelcome to your game!')


player = Player(room['outside'])


def print_room(player): 
    print("\nYou are currently in the " + player.room.name)
    print(f'{player.room.desc}\n')

    if player.room.items == []:
        print('No items in this room.\n')
    else:
        print('Items in this room:')
        for item in player.room.items:
            print(f'{item.name}\n')





action = input("Press ENTER to continue...\n")

while action!='Q':
    print_room(player)
    action = input("[N] North [S] South [E] East [W] West\n[I] Inventory\n[Q] Quit\n").upper()

    if action == 'N' or action == 'S' or action == 'E' or action == 'W':
        if action == 'N' and player.room.n_to != None:
            player.room = player.room.n_to
        elif action == 'S' and player.room.s_to != None:
            player.room = player.room.s_to
        elif action == 'E' and player.room.e_to != None:
            player.room = player.room.e_to
        elif action == 'W' and player.room.w_to != None:
            player.room = player.room.w_to
        else: 
            print('\nThere is no room in that direction.\n')
    elif action == 'I':
        player.print_inventory()
    elif action.split()[0] == 'GET' or action.split()[0] == 'TAKE':
        if item[action.split()[1]] in player.room.items:
            pickedItem = item[action.split(' ')[1]]
            player.room.items.remove(pickedItem)
            player.inventory.append(pickedItem)
            pickedItem.on_take()
        else:
            print('No such item in this room.')
    elif action.split()[0] == 'DROP':
        if item[action.split()[1]] in player.inventory:
            droppedItem = item[action.split()[1]]
            player.inventory.remove(droppedItem)
            player.room.items.append(droppedItem)
            droppedItem.on_drop()
        else:
            print('No such item in your inventory.')
    elif action != 'Q': 
        print('Invalid command.\n')
    else:
        print('\nGoodbye!\n')
    






