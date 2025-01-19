contact_book = {}

def contact_add(dictionary, name, email, phone):
  if name in dictionary:
    dictionary[name].update({'Email': email, 'Phone': phone})
  else:
    dictionary[name] = {'Email': email, 'Phone': phone}
    return dictionary


contact_add(contact_book, 'Steff Boyle', 'steff0109@gmail.com', '07742627852')
contact_add(contact_book, 'John Boyle', '07547672565', 'john.hazukisan@gmail.com')
contact_add(contact_book, 'Steff Boyle', 'rinoatakako@gmail.com', '07742627852')
print(contact_book)