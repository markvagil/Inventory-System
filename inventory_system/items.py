
class Item():

    def __init__(self, name, count):
        # Item class; instantiaites a new item with a name and quantity
        self.item_name = name
        self.total_stock = count

    def update_stock(self, new_count):
        # changes the quantity of the item to the provided number
        self.total_stock = new_count

    def update_name(self, new_name):
        # updates name of the item to the parameter that was provided
        self.item_name = new_name

    def get_name(self):
        # returns name of the item
        return self.item_name

    def get_stock(self):
        # returns quantity of the item
        return self.total_stock
