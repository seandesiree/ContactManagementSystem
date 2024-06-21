def add_contact(dict_contacts):
    dict_contacts = {}
    name = input("What is the name of the new contact? ")
    number = input("What is the number of the new contact? ")
    email = input("What is the email of the new contact? ")
    try:
        dict_contacts[name] = (number, email)
    except:
        dict_contacts[name] = None
            
    return dict_contacts


def edit_contact(dict_contacts):
    name = input("What is the name of the new contact? ")

    if name not in dict_contacts:
        print("This name does not exist. ")
    else:
        number = input("What is the number of the new contact? ")
        email = input("What is the email of the new contact? ")
        dict_contacts[name] = (number, email)
            
    return dict_contacts


def delete_contact(dict_contacts):
    name = input("What is the name of the new contact? ")

    if name not in dict_contacts:
        print("This name does not exist. ")
    else:
        dict_contacts[name].pop
            
    return dict_contacts



def search_contact(dict_contacts):
    name = input("What is the name of the contact? ")
    number = input("What is the number of the contact? ")
    email = input("What is the email? of the contact? ")
    if name in dict_contacts:
        contact = dict_contacts[name]
        print(f"{name}, {contact[0]}, {contact[1]}\n")
    elif number in dict_contacts:
        contact = dict_contacts[name]
        print(f"{name}, {contact[0]}, {contact[1]}\n")
    elif email in dict_contacts:
        contact = dict_contacts[name]
        print(f"{name}, {contact[0]}, {contact[1]}\n")
    


def display_contact(dict_contacts):
    for name, values in dict_contacts.items():
        number, email = values
        print(f"{name}: {number}, {email}")
    
    sort = input("Would you like to sort contacts? If yes, type by 'name', 'number' or 'email'. If no, press any key to continue. ")
    if sort == "name".lower():
        sorted_name = dict(sorted(dict_contacts.items()))
        print(sorted_name)
    elif sort == "number".lower():
        sorted_number = dict(sorted(dict_contacts.items(), key = lambda x:x[0]))
        print(sorted_number)
    elif sort == "email".lower():
        sorted_email = dict(sorted(dict_contacts.items(), key = lambda x:x[1]))
        print(sorted_email)
    else:
        return "Continue"

        


def export_contacts(dict_contacts, filename):
    try:
        with open(filename, "w") as file:
            for key in dict_contacts:
                name = key
                number = dict_contacts[key][0]
                email = dict_contacts[key][1]
                file.write(f"{name}, {number}, {email}")
            return dict_contacts
    except FileNotFoundError:
        []



def import_contacts(filename):
    try:
        with open(filename, "r") as file:
            dict_contacts = {}
            for line in file:
                name, number, email = line.strip().split(",")
                dict_contacts[name] = (number, email)
            return dict_contacts
    except FileNotFoundError:
        []



def main():
    dict_contacts = {}

    while True:
        try:
            print(dict_contacts)
            menu = input("""              
            Welcome to the Contact Management System!
            Menu:        
            1. Add a new contact
            2. Edit an existing contact
            3. Delete a contact
            4. Search for a contact
            5. Display all contacts
            6. Export contacts to a text file
            7. Import contacts from a text file
            8. Quit """)
            if menu == "1":
                dict_contacts.update(add_contact(dict_contacts))
            elif menu == "2":
                dict_contacts.update(edit_contact(dict_contacts))
            elif menu == "3":
                dict_contacts.update(delete_contact(dict_contacts))
            elif menu == "4":
                search_contact(dict_contacts)
            elif menu == "5":
                display_contact(dict_contacts)
            elif menu == "6":
                export_contacts(dict_contacts, "contactlist.txt")
            elif menu == "7":  
                dict_contacts.update(import_contacts("contactlist.txt"))
            elif menu == "8":
                break
        except ValueError:
            print("Please enter a number between 1 - 5. ")

main()
