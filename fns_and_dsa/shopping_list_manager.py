def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Start with an empty shopping list
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add item
            item = input("Enter the item to add: ").strip()
            if item:  # Ensure not empty
                shopping_list.append(item)
                print(f"✅ '{item}' has been added to the shopping list.")
            else:
                print("⚠️ Item name cannot be empty.")

        elif choice == '2':
            # Remove item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"❌ '{item}' has been removed from the shopping list.")
            else:
                print(f"⚠️ '{item}' was not found in the shopping list.")

        elif choice == '3':
            # View list
            if shopping_list:
                print("\n🛒 Your Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("🛒 Your shopping list is empty.")

        elif choice == '4':
            # Exit
            print("👋 Goodbye! Thanks for using Shopping List Manager.")
            break

        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
