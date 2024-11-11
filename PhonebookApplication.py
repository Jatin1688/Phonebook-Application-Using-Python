
phonebook = {}


def add_contact():
    name = input("Enter contact name: ").strip()
    if name in phonebook:
        print("Contact already exists.")
    else:
        phone_number = input("Enter phone number: ").strip()
        if phone_number.isdigit():
            phonebook[name] = phone_number
            print(f"Contact {name} added successfully.")
        else:
            print("Invalid phone number. Please use digits only.")


def search_contact():
    name = input("Enter contact name to search: ").strip()
    if name in phonebook:
        print(f"Contact found - {name}: {phonebook[name]}")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter contact name to delete: ").strip()
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")


def list_contacts():
    if phonebook:
        print("Phonebook Contacts:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    else:
        print("No contacts found in the phonebook.")

# User Interface - Main loop
def main():
    while True:
        print("\nPhonebook Application")
        print("1. Add a New Contact")
        print("2. Search for a Contact")
        print("3. Delete a Contact")
        print("4. List All Contacts")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            list_contacts()
        elif choice == '5':
            print("Exiting Phonebook Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
