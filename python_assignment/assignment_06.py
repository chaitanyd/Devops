# Imagine that a vanquished dragon’s loot is represented as a list of strings like this:
#
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#
# Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary
# representing the player’s inventory (like in the previous project) and the addedItems parameter is a list like
# dragonLoot.

# The addToInventory() function should return a dictionary that represents the updated inventory.
# Note that the addedItems list can contain multiples of the same item. Your code could look something like this:

# def addToInventory(inventory, addedItems):
#  # your code goes here
# inv = {'gold coin': 42, 'rope': 1}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# inv = addToInventory(inv, dragonLoot)
# displayInventory(inv)

# The previous program (with your displayInventory() function from the previous project) would output the following:

# Inventory:
# 45 gold coin
# 1 rope
# 1 ruby
# 1 dagger
# Total number of items: 48

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