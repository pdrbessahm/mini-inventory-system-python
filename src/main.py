from src import crud

# creating the menu to running in the terminal
def menu():

    # runs just until the user insert 5
    while True:
        print("=======Store Inventory System=======")
        print("1. Create a Product")
        print("2. List Products")
        print("3. Update a Product")
        print("4. Delete a Product")
        print("5. Exit")
        print("------------------------------------")
        choice = input("Choose an option: ")
        
        if choice == 1:
            # ask the user to input the right parameters in order to create a new product
            p_id = int(input("ID: "))
            name = input("Name: ")
            price = float(input("Price: "))
            # add the product and its parameters to the crud file/fake database
            crud.create_product(p_id, name, price)
        
        elif choice == 2:
            # create a loop to return a list of all products within our database
            for product in crud.create_product():
                print(product)
        
        elif choice == 3:
            # asks for the ID to update and the new parameters 
            p_id = int(input("ID to update: "))
            name = input("New name: ")
            price = float(input("New price: "))
            # create a new variable to operate this update into our fake database
            updated = crud.update_product(p_id, name, price)
            print("Updated:", updated)
        
        elif choice == 4:
            # asks for the ID to delete 
            p_id = int(input("ID to delete: "))
            # run the operation within our fake database
            crud.delete_product(p_id)
        
        elif choice == 5:
            # break the code to stop running
            break

if __name__ == "__main__":
    menu()