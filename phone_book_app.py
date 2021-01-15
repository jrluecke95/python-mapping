phonebook = {
    "steve": "111-111-1111", 
    "fred": "222-222-2222", 
    "sara": "333-333-3333"}


def look_up(answer):
    if answer == 1:
        while True:
            try:
                name = input("Who's number do you want to look up? ").lower()
                print(phonebook[name])
                break
            except KeyError:
                print("sorry, we couldn't find that name, please try again!")
        
def set_entry(answer):
    if answer == 2:
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

def delte_entry(answer):
    if answer == 3:
        while True:
            try:
                name = input("who's number do you want to delete? ").lower()
                del phonebook[name]
                break
            except KeyError:
                print("sorry, we couldn't find that name")

def list_entries(answer):
    if answer == 4:
        for name in phonebook:
            print(name, phonebook[name])

def quit(answer):
    if answer == 5:
        return None

def phonebook_app(answer):
    print("""
    Electronic Phone Book:

    =====================
    
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit""")