from items import Item
# Inherits the Item class from items.py file

class Main:

    """
    TO DO:
    - video
    - github
    """

    def __init__(self):
        # defines class wide variables and calls the update function
        self.inventory = []
        self.system_active = True
        self.update()


    def update(self):
        if self.system_active == False:
            # terminates the program when system_active is false
            quit()

        while self.system_active:
            # displays text menu for user to enter an option, calls get_input, and gives warnings until the user exits the system
            print("-------------------------")
            print()
            print("Welcome, please enter the corresponding number of the action you would like to perform: ")
            print("[1] View Inventory")
            print("[2] Add New Item")
            print("[3] Delete Item")
            print("[4] Update Item Quantity")
            print("[5] Change Item Name")
            print("[6] Exit System")
            print()
            print("-------------------------")
            self.get_input()
            self.give_warnings()


    
    def get_input(self):
        # This function retreives input from the user and calls a function based upon the option they entered.

        while True:
            # This while loop validates that the user entered an integer
            try:
                action = int(input("Input: "))
            except ValueError:
                print("")
                print("ERROR: Your input was invalid, please enter a valid option.")
            else:
                break

        # Calls function based on corresponding number that the user inputted
        if action == 1:
            self.print_list()
        elif action == 2:
            self.add_item()
        elif action == 3:
            self.delete_item()
        elif action == 4:
            self.update_quantity()
        elif action == 5:
            self.change_name()
        elif action == 6:
            self.system_active = False


    def print_list(self):
        # this function prints the current self.inventory list of items and how many are in stock. If no items are in the list, it prints a warning statement.
        
        i = 1
        print("-------------------------")

        if not self.inventory:
            # prints if self.inventory list is empty
            print("Inventory contains no items.")

        for item in self.inventory:
            # iterates through self.inventory and returns each item in the list with it's name and quantity
            print(f"{i} - {item.get_name()} : {item.get_stock()} in stock")
            i += 1


    def add_item(self):
        # this function adds a new item to the list
        print("-------------------------")
        # gets item name
        name = input("What is the name of the item? (type '-c' to cancel): ")
        if name == "-c":
            return

        while True:
            # checks for valid input for item quantity
            try:
                quantity = int(input("How many are in stock? (type a negative integer to cancel): "))
            except ValueError:
                print("")
                print("ERROR: Your input was invalid, please enter a valid option.")

            if quantity < 0:
                return
            else:
                break
        
        # calls item class to create new item object with the provided name and quantity
        self.inventory.append(Item(name, quantity))
        print("")
        print(f"Item with name {name} and quantity {quantity} has been added to the inventory.")


    def delete_item(self):
        # this function removes an item from self.inventory
        print("-------------------------")

        while True:
            # checks for valid index given by the user
            try:
                remove_item_index = int(input("What is the index of the item you would like to delete? (type 0 to cancel): ")) - 1
            except ValueError:
                print("")
                print("ERROR: Your input was invalid, please enter a valid option.")

            if remove_item_index < 0:
                return
            if self.check_valid_index(remove_item_index) == False:
                print("")
                print("ERROR: The index does not exist, please try again.")
            else:
                break
        
        # pops item from the list by user given index
        print(f"Item '{self.inventory[remove_item_index].get_name()}' has been deleted.")
        self.inventory.pop(remove_item_index)


    def update_quantity(self):
        # this function allows the user to update the quantity of an item in the inventory
        print("-------------------------")

        while True:
            # checks for valid index given by the user
            try:
                item_index = int(input("What is the index of the item you would like to change the quantity of? (type 0 to cancel): ")) - 1
            except ValueError:
                print("")
                print("ERROR: Your input was invalid, please enter a valid option.")

            if item_index < 0:
                return
            if self.check_valid_index(item_index) == False:
                print("")
                print("ERROR: The index does not exist, please try again.")
            else:
                break

        while True:
            # checks for valid quantity
            try:
                quantity = int(input("What is the new quantity of the item? (type a negative integer to cancel): "))
            except ValueError:
                print("")
                print("ERROR: Your input was invalid, please enter a valid option.")
            
            if quantity < 0:
                return
            else:
                break

        # system prints item with old quantity, then updates quantity, and prints item with new quantity
        print(f"{self.inventory[item_index].get_name()} - OLD QUANTITY: {self.inventory[item_index].get_stock()}")
        self.inventory[item_index].update_stock(quantity)
        print(f"{self.inventory[item_index].get_name()} - NEW QUANTITY: {self.inventory[item_index].get_stock()}")



    def change_name(self):
        # this function allows the user to change the name of an item in the inventory

        print("-------------------------")

        while True:
            # checks for valid index given by the user
            try:
                item_index = int(input("What is the index of the item you would like to change the name of? (type 0 to cancel): ")) - 1
            except ValueError:
                print("")
                print("ERROR: Your input was invalid, please enter a valid option.")

            if item_index < 0:
                return
            if self.check_valid_index(item_index) == False:
                print("")
                print("ERROR: The index does not exist, please try again.")
            else:
                break

        # gets new item name, any input is valid
        new_name = input("What is the new name of the item? (type '-c' to cancel): ")
        if new_name == "-c":
            return

        # system prints item with old name, then updates name, and prints item with new name
        print(f"OLD NAME: {self.inventory[item_index].get_name()} - QUANTITY: {self.inventory[item_index].get_stock()}")
        self.inventory[item_index].update_name(new_name)
        print(f"NEW NAME: {self.inventory[item_index].get_name()} - QUANTITY: {self.inventory[item_index].get_stock()}")


    def give_warnings(self):
        # this function automatically prints warnings to the user if an item is out of stock or if it's quantity is 5 or less
        print("")
        for item in self.inventory:
            if item.get_stock() == 0:
                print(f"{item.get_name()} is out of stock!")
                print(f"{item.get_name()} : {item.get_stock()} in stock")
            elif item.get_stock() <= 5:
                print(f"{item.get_name()} has a low inventory!")
                print(f"{item.get_name()} : {item.get_stock()} in stock")


    def check_valid_index(self, index):
        # this function checks if an index exists within the self.inventory list
        if index >= 0 and index < len(self.inventory):
            return True
        else:
            return False

# calls Main() class to start the program
Main()
