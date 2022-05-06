import files

def menu():
    choice = input('\nMenu\n\n1-Add or update item\n2-Display items\n3-Exit\n\nChoose an option: ')
    if choice == '1':
        add_item()
    elif choice == '2':
        del_item()
    else:
        print('\nExiting..\n')

def add_item():
    print('\nCURRENT INVENTORY\n' + str(files.inventory))
    key = input('\nEnter an item name: ')
    quantity = int(input('\nEnter inventory changes: '))
    print('\nNEW INVENTORY\n' + str(files.add_inventory(key, quantity)))
    choice = input('\nWould you like to continue?\n\n1-Menu\n2-Exit\n\nChoose an option: ')
    if choice == '1':
        menu()
    else:
        print('\nExiting..\n')

def del_item():
    print('\nCURRENT INVENTORY\n' + str(files.inventory))
    choice = input('\nWould you like to continue?\n\n1-Menu\n2-Exit\n\nChoose an option: ')
    if choice == '1':
        menu()
    else:
        print('\nExiting..\n')

menu()