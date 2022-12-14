# This program was created by Max Folger for inventory management applications
# ln 4-9 displays user options and takes user input for selection

def main_menu():
    print("Welcome to your inventory management dashboard!\n")
    print(" 1. Inventory Report\n", "2. Usage & Cost Report\n", "3. Add Item\n", "4. Update Product Usage")
    print(" 5. Update product cost\n","6. Update On-Hand Quantity\n")
    print("** Enter 555 to Exit **")
    command = input("What would you like to do?: ")
    menu_choice(command)

def menu_choice(command):   #ln 12-29 are the corresponding actions/functions to the user selection
    if command == "1":
        view_action()   # displays item, quantity on-hand, usage, and unit cost
    elif command == "2":
        usage_reports() # displays item, usage cost, on-hand item value, and unit cost
    elif command == "3":
        add_items()     # allows for addition of new items and data to inventory.txt
    elif command == "4":
        modify_usage()  # allows for update to usage
    elif command == "5":
        modify_cost()   # allows updating cost
    elif command == "6":
        modify_onhand() # allows updating on-hand inventory
    elif command == "555":
        print("Goodbye!")
        quit()          # closes program
    else:
        main_menu()     # any other response resets the main menu


def view_action():
    inventoryfile = open('Inventory.txt', 'r')  # opens inventory text file as is in a read-only state
    item_description = inventoryfile.readline() # begins readline for loop
    print('\nCurrent Inventory')
    print('-----------------')
    while item_description != '':
        item_quantity = inventoryfile.readline()    #ln 38-40 read the rest of the items line
        inventory_usage = inventoryfile.readline()
        inventory_cost = inventoryfile.readline()
        item_description = item_description.rstrip('\n')    # ln 41-44 strips the newline character from the end
        item_quantity = item_quantity.rstrip('\n')
        item_usage = inventory_usage.rstrip('\n')
        item_cost = inventory_cost.rstrip('\n')
        print(f"{'Item:': <15} {item_description: ^10}")    # ln 45-48 displays the data for the item while using f to format
        print(f"{'On-hand:': <15} {item_quantity: ^10}")
        print(f"{'Usage:': <15} {item_usage: ^10}")
        print(f"{'Unit cost: $': <15} {item_cost: ^10}")
        print('----------')
        item_description = inventoryfile.readline()
    inventoryfile.close()   # closes file, next line returns user to main menu
    main = input("Enter any key to return to the main menu")
    main_menu()

def usage_reports():
    inventoryfile = open('Inventory.txt', 'r')  # opens inventory as read-only for basic math operations
    item_description = inventoryfile.readline()     
    print('Usage reports & other important informtion')
    print('-------------------------------------------')
    while item_description:
        item_quantity = inventoryfile.readline()
        inventory_usage = inventoryfile.readline()
        inventory_cost = inventoryfile.readline()   # ln 64-67 strips the newline character from the end
        item_quantity = item_quantity.rstrip('\n')
        item_usage = inventory_usage.rstrip('\n')
        item_cost = inventory_cost.rstrip('\n')
        item_description = item_description.rstrip('\n')
        item_quantity = int(item_quantity)      # ln 68-70 retrieves data points as integers for math operations below
        item_usage = int(inventory_usage)
        item_cost = float(inventory_cost)
        print(f"{'Item:': <15} {item_description: ^10}")        # ln 71-75 displays basic inventory cost/usage reports that may be needed.
        print(f"{'On-hand value: $': <15} {item_quantity * item_cost: ^10}")
        print(f"{'Used value: $': <15} {item_usage * item_cost * -1: ^10}")
        print(f"{'Unit cost: $': <15} {item_cost: ^10}")
        print('----------')
        item_description = inventoryfile.readline() 
    inventoryfile.close()
    main = input("Enter any key to return to the main menu")
    main_menu()        
    
def add_items():        # allows user to append new items and their data points to inventory.txt
    InventoryFile = open('Inventory.txt', 'a')
    print("Adding Inventory")
    print("================")
    item_description = input("Enter the item name: ").title()       # ln 85-87 take input on the new item
    item_quantity = input("Enter the on-hand quantity of the item: ")
    item_cost = input("Enter the unit cost of the item: ")
    InventoryFile.write(item_description + '\n')    # ln 88-91 writes that data to the file, notice that usage is not there.
    InventoryFile.write(item_quantity + '\n')       # this is because it is initialy 0
    InventoryFile.write("0" + '\n')
    InventoryFile.write(item_cost + '\n')
    InventoryFile.close()
    print(item_description, "has been successfuly added!")  # confirmation that the item was added
    main = input("Enter any key to return to the main menu")
    main_menu()

def modify_usage():     # currently only allows for the adjustment of the usage characterstic
    with open("Inventory.txt","r+") as f:
        item_list = f.read().split()    # splits the data sheet into a list, could be an issue when working with big files
        for word in item_list:  # displays only the item names so the user has a list to choose from
            if word.isalpha():
                print(word)
        user_search = input("What item do you want to update? ").title()    # this search finds the index of an exact match
        index_offset = item_list.index(user_search) + 2     # this offsets that index by 2 so that it is on the usage data
        accumulator = int(item_list[index_offset])  # temporary accumulator for the existing usage data
        use = int(input("How much inventory have you used? ")) # it is then updated
        accumulator -= use
        item_list[index_offset] = str(accumulator)                  # converted back to a string to be written back to the file
        index_offset = item_list.index(user_search) + 1 # Reduces on-hand quantity
        quantity_to_reduce = int(item_list[index_offset])   # current + next 2 lines convert to int for math, then convert back from writing
        quantity_to_reduce -= use
        item_list[index_offset] = str(quantity_to_reduce)
        print(item_list[index_offset])
        f.seek(0)                       # seek is set to file start, the loop then goes to overwrite the entire file with new data
        for word in item_list:
            f.write(word + "\n")
        f.close()
    main = input("Enter any key to return to the main menu")
    main_menu()

def modify_cost():     # currently only allows for the adjustment of the usage characterstic
    with open("Inventory.txt","r+") as f:
        item_list = f.read().split()    # splits the data sheet into a list, could be an issue when working with big files
        for word in item_list:  # displays only the item names so the user has a list to choose from
            if word.isalpha():
                print(word)
        user_search = input("What item do you want to update? ").title()    # this search finds the index of an exact match
        index_offset = item_list.index(user_search) + 3     # this offsets that index by 3 to modify the cost section
        new_price = (input("What is the new price? (do not add $ symbol): ")) # it is then updated
        item_list[index_offset] = str(new_price)                  # and overwritten
        print(item_list[index_offset])
        f.seek(0)                       # seek is set to file start, the loop then goes to overwrite the entire file with new data
        for word in item_list:
            f.write(word + "\n")
        f.close()
    main = input("Enter any key to return to the main menu")
    main_menu()

def modify_onhand():     # currently only allows for the adjustment of the usage characterstic
    with open("Inventory.txt","r+") as f:
        item_list = f.read().split()    # splits the data sheet into a list, could be an issue when working with big files
        for word in item_list:  # displays only the item names so the user has a list to choose from
            if word.isalpha():
                print(word)
        user_search = input("What item do you want to update? ").title()    # this search finds the index of an exact match
        index_offset = item_list.index(user_search) + 1     # this offsets that index by 1 to modify the on-hand quantity
        new_onhand = (input("Enter the actual quantity on-hand: ")) # it is then updated
        item_list[index_offset] = str(new_onhand)                  # and overwritten
        print(item_list[index_offset])
        f.seek(0)                       # seek is set to file start, the loop then goes to overwrite the entire file with new data
        for word in item_list:
            f.write(word + "\n")
        f.close()
    main = input("Enter any key to return to the main menu")
    main_menu()

        
main_menu()
