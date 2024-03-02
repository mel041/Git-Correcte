def agregar_contacto(agenda):
    # Ask the user to input the contact's name
    nombre = input("Enter the contact's name: ")
    # Ask the user to input the contact's phone number
    telefono = input("Enter the contact's phone number: ")
    # Add the contact to the phonebook
    agenda[nombre] = telefono
    # Print a success message
    print("Contact added successfully.")
