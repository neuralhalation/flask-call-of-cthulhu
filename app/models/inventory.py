import app.functions.add_remove as ar


def inventory_item(name, description):
    """Creates an inventory item.

    Args:
        name (str): The name of the inventory item.
        description (str): The description of the inventory item.

    Return:
        dict: An inventory item.
    """
    return ar.new("item", name=name, description=description)


def add_inventory_item(item, item_list=[]):
    """Adds an item to an inventory.

    Args:
        item (dict): An inventory item.
        item_list (list): The list of items in the character's possession.

    Return:
        list: A list of inventory items.
    """
    return ar.add_to_list(item, item_list)


def remove_inventory_item(name, item_list):
    """Removes an item from the inventory.

    Args:
        name (str): The name of the inventory item to be removed.
        item_list (list): The character's inventory.

    Return:
        list: A list of inventory items.
    """
    return ar.remove_by_obj_key_and_val_key("item", "name", name, item_list)
