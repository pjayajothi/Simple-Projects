#Your Task:
#Combine the functions:
  #display_menu: Displays the menu options for the user.
  #add_contact: Adds a new contact to the Contact Book.
  #view_contact: Displays details for a specific contact.
  #edit_contact: Updates an existing contact’s information.
  #delete_contact: Removes a contact from the Contact Book.
  #list_all_contacts: Displays all the contacts in the Contact Book.
#Create a dictionary called contact_book to store the contacts.
#Write a loop that:
  #Displays the menu using display_menu.
  #Accepts user input for the menu choice.
  #Calls the appropriate function based on the user’s choice.
  #Continues until the user selects the option to exit the program.
#Expected Behavior:
  #When you run the program, it should:
  #Show a menu of options for the user to choose from.
  #Allow the user to interact with the Contact Book by calling the appropriate function.
  #Exit the program cleanly when the user selects the "Exit" option.
                      
def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")
#function that takes one argument: contact_book (a dictionary). The function should:
  #Get input for the contact's name, phone, email, and address.
  #Check if the name already exists in the dictionary. If it does, print: "Contact already exists!".
  #If not, save the contact, then print: "Contact added successfully!"
def add_contact(contact_book):
    name = input()
    phone = input()
    email = input()
    address = input()
    if name in contact_book:
        print("Contact already exists!")
    else:
        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact added successfully!")
#function named view_contact that displays details of a specific contact. The function should:
  #Take a contact book dictionary as input
  #Ask the user to enter a contact name
  #Display the contact's details if found
  #Print "Contact not found!" if the contact doesn't exist
def view_contact(contact_book):
    name = input()
    if name in contact_book:
        print(f"Name: {name}")
        print(f"Phone: {contact_book[name]['phone']}")
        print(f"Email: {contact_book[name]['email']}")
        print(f"Address: {contact_book[name]['address']}")
    else:
        print("Contact not found!")
#function named edit_contact that allow users to update the details of an existing contact. The function should:
  #Get input for the contact's name that the user wants to edit.
  #Check if the name exists in the contact_book:
    #If it exists, prompt the user to input new values for the contact's phone, email, and address (in that order!).
    #If the user provides no input (presses Enter), keep the current value for that field (in this case the input will be an empty string, '').
    #Update the contact's information in the dictionary.
    #Print: "Contact updated successfully!".
  #If the contact does not exist, print: "Contact not found!".
def edit_contact(contact_book):
    name = input()
    if name in contact_book:
        contact_book[name]['phone'] = input()
        contact_book[name]['email'] = input()
        contact_book[name]['address'] = input()
        print("Contact updated successfully!")
    else:
        print("Contact not found!")
#Create a function named delete_contact that will allow users to remove a specific contact. The function should:
#Get input for the contact's name that the user wants to delete.
#Check if the name exists in the contact_book:
  #If it exists, remove the contact from the dictionary.
    #Print: "Contact deleted successfully!".
  #If the contact does not exist, print: "Contact not found!".
def delete_contact(contact_book):
    name = input()
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")
#Create a function named list_all_contacts that will allow users to view all the contacts stored. The function should:
#Check if the contact_book is empty:
  #If it is empty, print: "No contacts available.".
  #If it is not empty:
    #Loop through each contact in the dictionary and print their name, phone, email, and address in a readable format.
    #If it is empty, print: "No contacts available.".
def list_all_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
    else:
        for name, details in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}\n")

def main():
    while True:
        display_menu()
        choice = input()
        if choice == '1':
            add_contact(contact_book)
        elif choice == '2':
            view_contact(contact_book)
        elif choice == '3':
            edit_contact(contact_book)
        elif choice == '4':
            delete_contact(contact_book)
        elif choice == '5':
            list_all_contacts(contact_book)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
contact_book = {}
main()
# Another way to run the program
#if __name__ == "__main__":
    #main()
