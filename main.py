# Starting dictionary
contact_book = {'name': 'Jen Boyle', 'email':'jen1981@gmail.com', 'phone': '07567895343'}

# Function to add or update dictionary
def contact_add_update(dictionary, name, email, phone):
  if name in dictionary:
    dictionary[name].update({'Email': email, 'Phone': phone})
  else:
    dictionary[name] = {'Email': email, 'Phone': phone}
    return dictionary

# Add to contact book
contact_add_update(contact_book, 'Steff Boyle', 'steff0109@gmail.com', '07742627852')
contact_add_update(contact_book, 'John Boyle', '07547672565', 'john.hazukisan@gmail.com')
contact_add_update(contact_book, 'Steff Boyle', 'rinoatakako@gmail.com', '07742627852')

# Check and print details from contact book
def contact_book_check(dictionary, name):
  if name in dictionary:
    # f added makes a string literal possible 
    print(f'The contact is {name}', dictionary[name])
  else:
    print('Contact is not in contact book')
    return dictionary

contact_book_check(contact_book, 'Steff Boyle')

