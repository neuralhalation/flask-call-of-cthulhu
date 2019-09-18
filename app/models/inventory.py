def inventory_item(name, description):
    """Creates an inventory item.

    Args:
        name (str): The name of the inventory item.
        description (str): The description of the inventory item.

    Return:
        dict: An inventory item.
    """
    return {"item": {"name": name, "description": description}}


def add_inventory_item(item, item_list=[]):
    """Adds an item to an inventory.

    Args:
        item (dict): An inventory item.
        item_list (list): The list of items in the character's possession.

    Return:
        list: A list of inventory items.
    """
    new_inventory = []
    if item not in item_list:
        new_inventory = item_list.__add__([item])
    return new_inventory


def remove_inventory_item(name, item_list):
    """Removes an item from the inventory.

    Args:
        name (str): The name of the inventory item to be removed.
        item_list (list): The character's inventory.

    Return:
        list: A list of inventory items.
    """
    return [i for i in item_list if i["item"]["name"] != name]
