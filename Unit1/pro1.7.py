my_list = []

while True:
    print("\nMenu:")
    print("1. Add element")
    print("2. Display list")
    print("3. Delete element")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = input("Enter element to add: ")
        my_list.append(val)
    elif choice == 2:
        print("List:", my_list)
    elif choice == 3:
        val = input("Enter element to delete: ")
        if val in my_list:
            my_list.remove(val)
        else:
            print("Element not found!")
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
