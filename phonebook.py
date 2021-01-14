phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

eliz_num = phonebook_dict['Elizabeth']
print(eliz_num)

phonebook_dict['Kareem'] = '938-489-1234'
print(phonebook_dict['Kareem'])

del(phonebook_dict['Elizabeth'])
print(phonebook_dict)

phonebook_dict['Bob'] = '968-345-2345'
print(phonebook_dict)

for name in phonebook_dict:
    print(phonebook_dict[name])