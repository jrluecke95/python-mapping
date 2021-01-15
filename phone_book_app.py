phonebook = {
    "steve": "111-111-1111", 
    "fred": "222-222-2222", 
    "sara": "333-333-3333"}


def look_up():
    while True:
        try:
            name = input("Who's number do you want to look up? ").lower()
            print(phonebook[name])
            break
        except KeyError:
            print("sorry, we couldn't find that name, please try again!")
        
def set_entry():
    while True:
        try:
            name = input("what do you want this persons name to be? ").lower()
            number = input("what do you want their number to be? - please include dashes ")
            if (len(name) > 0) and (len(number) == 12):
                phonebook[name] = number
                break
            else:
                raise Exception("invaild name or number")
        except:
            print("Please enter a valid name and number")

def delete_entry():
    while True:
        try:
            name = input("who's number do you want to delete? ").lower()
            del phonebook[name]
            break
        except KeyError:
            print("sorry, we couldn't find that name")

def list_entries():
    for name in phonebook:
        print(name, phonebook[name])

def phonebook_app():
    print("""
    Electronic Phone Book:

    =====================
    
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit""")
    while True:
        try:
            answer = int(input("which action would you like to peform?"))
            if answer < 1 or answer > 5:
                raise Exception
            else:
                break
        except:
            print("sorry that is not a valid selection, please try again")
    if answer < 5:
        if answer == 1:
            look_up()
        elif answer == 2:
            set_entry()
        elif answer == 3:
            delete_entry()
        elif answer == 4:
            list_entries()
        phonebook_app()

phonebook_app()