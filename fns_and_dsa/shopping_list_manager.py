def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            user_input = input("enter your input: ")
            shopping_list.append(user_input)
            print( f"you add {user_input} in the shopping_list variable successfully")
            
        elif choice == '2':
            # Prompt for and remove an item
          
            user_input = input("enter your input that you want to delete: ").strip().lower()
            if user_input in shopping_list:
                shopping_list.remove(user_input)
                print(f"you remove {user_input} from shopping_list variable successfully")
            else:
                print(f"{user_input} is not found in the list")
            
        elif choice == '3':
            # Display the shopping list

            print (shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
