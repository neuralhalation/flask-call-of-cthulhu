def inventory_item(name, description, quantity):
    return {"item": {"name": name, "description": description, "quantity": quantity}}


def update_quantity(name, amt, item_list):
    return [i["item"]["quantity"] + amt for i in item_list if i["item"]["name"] == name]


def add_inventory_item(item, amt=1, item_list=[]):
    new_inventory = []
    if item not in item_list:
        new_inventory = item_list.__add__([item])
    return new_inventory


def remove_inventory_item(name, item_list):
    return [i for i in item_list if i["item"]["name"] != name]
