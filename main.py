import re
import os
import json

contacts = {"Jeffrey Hulter": {"Phone number": "8313350949",
                               "Email": "jeff.hulter@gmail.com",
                               "Address": "6621 Cooper Street, Felton, CA 95018"}
            }

def add_contacts(contacts):
    print("Add a new contact")
    phone_pat = r'[\d]{3}-[\d]{3}-[\d]{4}'
    email_pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    add_name = input("What's the name of the contact would you like to add? ")
    add_phone = input("What's the phone number of the contact? ")
    add_email = input("What's the email address of the contact? ")
    add_address = input("What's the home address of the contact? ")
    if add_name not in contacts:
        if re.match(email_pat, add_email) and re.match(phone_pat, add_phone):
            contacts[add_name] = {"Phone number: ": add_phone, "Email: ": add_email, "Address: ": add_address}
            print("Contact added!")
        else:
            print("Invalid format")
    else:
        print("This contact is already in your contact list!")

def edit_contacts():
    select_contact = input("What contact would you like to edit? ")
    edit_phone = input("What phone number would you like to change it to? ")
    edit_email = input("What email would you like to change it to? ")
    edit_address = input("What address would you like to change it to? ")
    contacts.update({select_contact: {"Phone: ": edit_phone, "Email: ": edit_email, "Address: ": edit_address}})


def delete_contacts():
    print("Delete a task")
    delete_contact = input("What contact would you like to remove? ")
    if delete_contact in contacts:
        del contacts[delete_contact]
        print(f"{delete_contact} has been removed...")
    else:
        print(f"{delete_contact} was not found in your task list...")

def search_contacts():
    search_contact = input("What contact are you trying to find? ")
    print(contacts.get(search_contact))

def view_contacts():
    for name, info in contacts.items():
        print(f"{name} \n{info}")


def export_contacts():
    file = input("Enter a name for the file to create: ")
    with open(file, 'w') as f:
        f.write(json.dumps(contacts))

def import_contacts():
    pass

def main_menu():
    while True:
            print("Welcome to the To-Do List App!")
            print("\nMenu:")
            print("1. Add a new contact")
            print("2. Edit an existing contact")
            print("3. Delete a contact")
            print("4. Search for a contact")
            print("5. Display all contacts")
            print("6. Export contacts to a text file")
            #print("7. Import contacts from a text file")
            print("7. Quit")
            choice = input("Enter a menu choice: ")
            if choice == "1":
                add_contacts(contacts)
            elif choice == "2":
                edit_contacts()
            elif choice == "3":
                delete_contacts()
            elif choice == "4":
                search_contacts()
            elif choice == "5":
                view_contacts()
            elif choice == "6":
                export_contacts()
            #elif choice == "7":
             #   import_contacts()
            elif choice == "7":
                print("Quitting Contact List")
                break
            else:
                print("Invalid entry")
try:
    main_menu()
except Exception as e:
    print("An unexpected error occurred")
finally:
    print("That was so much fun!")


