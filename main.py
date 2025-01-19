# Starting dictionary
#contact_book = [{'name': 'Jen Boyle', 'email':'jen1981@gmail.com', 'phone': '07567895343'}, {'name': 'Steff Boyle', 'email': 'steff0109@gmail.com', 'phone': '07742627852'}, {'name': 'John Boyle', 'email': 'john.hazukisan@gmail.com', 'phone': '07547672565'}]

contact_book = {'name': 'Jen Boyle', 'email':'jen1981@gmail.com', 'phone': '07567895343'}

def contact_menu(dictionary):
  menu_input = input('Do you want to check or update your contact book? Check/Update ')
  if menu_input == 'Check':
    check_name = input('What is the contact you want to check? ')
    contact_book_check(dictionary, check_name)
  elif menu_input == 'Update':
    contact_name = input('What is the contact you want to add or update? ')
    contact_email = input('What is the email address of the contact? ')
    contact_phone = input('What is the phone number of the contact? ')

    contact_add_update(dictionary, contact_name, contact_email, contact_phone)
  else:
    print('Invalid Input. Please answer Check or Update')

    
    
# Function to add or update dictionary
def contact_add_update(dictionary, name, email, phone):
  if name in dictionary:
    print(f'The contact {name} is already in the contact book. ')
    confirm = input('Do you wish to update? Y/N ')
    if confirm == 'Y':
        dictionary[name].update({'Email': email, 'Phone': phone})
        print(f'The contact {name} has been updated')
    else: 
        print(f'The contact {name} has not been updated')
  else:
    dictionary[name] = {'Email': email, 'Phone': phone}
    print(f'The contact {name} has been added')


# Check and print details from contact book
def contact_book_check(dictionary, name):
  if name in dictionary:
    # f added makes a string literal possible 
    print(f'The contact is {name}', dictionary[name])
  else:
    print('Contact is not in contact book')
    
contact_menu(contact_book)

print(contact_book)


