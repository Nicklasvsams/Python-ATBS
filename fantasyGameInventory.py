inventory = {'arrow' : 12, 'gold coin' : 42, 'rope' : 1, 'torch' : 6, 'dagger' : 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def displayInventory(items):
    print('Inventory:')
    itemTotal = 0
    for k, v in items.items():
        print(k + ': ' + str(v))
        itemTotal += v
    print('Total number of items: ' + str(itemTotal))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1


addToInventory(inventory, dragonLoot)
displayInventory(inventory)
