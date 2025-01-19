
def contact_add(contact_book, name, email, phone):
  if name in contact_book:
    contact_book[name].update({'Email': email, 'Phone': phone})
  else:
    contact_book[name] = {'Email': email, 'Phone': phone}
    return contact_book

contact_book = {'Jen Boyle', 'jen1981@gmail.com', '076859473'}

contact_add(contact_book, 'Steff Boyle', 'steff0109@gmail.com', '07742627852')
print(contact_book)