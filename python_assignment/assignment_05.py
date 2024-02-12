# You are creating a fantasy video game.
# The data structure to model the player’s inventory will be a dictionary where the keys are string values
# describing the item in the inventory and the value is an integer value detailing how many of that item the player has.

# For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means
# the player has 1 rope, 6 torches, 42 gold coins, and so on.

# Write a function named displayInventory() that would take any possible “inventory” and display it like the following:
# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62

# Hint: You can use a for loop to loop through all the keys in a dictionary.

# # inventory.py
# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# def displayInventory(inventory):
#  print("Inventory:")
#  item_total = 0
#  for k, v in inventory.items():
#  # FILL THIS PART IN
#  print("Total number of items: " + str(item_total))
# displayInventory(stuff)

# inv = {'rope': 1, 'gold coin': 42}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def add_to_inventory(inventory, additems):
    for k in range(len(additems)):
        if additems[k] in inventory.keys():
            inventory[additems[k]] += 1
        else:
            inventory.setdefault(additems[k], 1)
    return inventory


def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))


inv = {'rope': 1, 'gold coin': 42}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)
