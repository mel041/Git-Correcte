def agregar_contacto(agenda):
    # Ask the user to input the contact's name
    nombre = input("Enter the contact's name: ")
    # Ask the user to input the contact's phone number
    telefono = input("Enter the contact's phone number: ")
    # Add the contact to the phonebook
    agenda[nombre] = telefono
    # Print a success message
    print("Contact added successfully.")

def ver_contactos(agenda):
    # Check if the phonebook is empty
    if len(agenda) == 0:
        print("The phonebook is empty.")
    else:
        # Print the list of contacts
        print("Contact list:")
        # Loop through the items in the phonebook and print each contact's name and phone number
        for nombre, telefono in agenda.items():
              # For each tuple pair, print the contact's name and phone number. 
              # 'nombre' is the variable representing the contact's name and 'telefono' is the variable representing the contact's phone number.
            print("Name:", nombre, "\tPhone number:", telefono)
