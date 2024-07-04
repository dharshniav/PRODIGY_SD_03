from contact_mgr import ContactManager
from contact import Contact

def display_menu():
    print("Contact Manager")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")

def get_contact_info():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    return name, phone, email

def main():
    manager = ContactManager()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name, phone, email = get_contact_info()
            manager.add_contact(Contact(name, phone, email))
            print("Contact added successfully!")
        elif choice == '2':
            contacts = manager.view_contacts()
            if not contacts:
                print("No contacts found.")
            else:
                for contact in contacts:
                    print(contact)
        elif choice == '3':
            old_name = input("Enter the name of the contact to edit: ")
            new_name, new_phone, new_email = get_contact_info()
            if manager.edit_contact(old_name, new_name, new_phone, new_email):
                print("Contact edited successfully!")
            else:
                print("Contact not found.")
        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            if manager.delete_contact(name):
                print("Contact deleted successfully!")
            else:
                print("Contact not found.")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
