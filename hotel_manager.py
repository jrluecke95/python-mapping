hotel = {
    '1' : {
        '101' : [],
    },
    '2' : {
        '237' : ['Jack Torrance', 'Wendy Torrance'],
    },
    '3' : {
        '333' : ['Neo', 'Trinity', 'Morpheus']
    }
}

floor_list = []
for floor in hotel:
    floor_list.append(floor)  #gives me list of floor 1, 2, 3

room_list = []
for floor in floor_list:
    room_list.append(hotel[floor].keys()) #gives me a room list

def check_in():
    while True:
        floor_num = input("What floor is your room on? ")
        try:
            if floor_num in floor_list:
                print(hotel[floor_num].keys())
                break
            else:
                raise TypeError
        except TypeError:
            print("sorry that wasn't a valid selection.")
    while True:
        try:
            room_num = input("What room is yours? ")
            if room_num in hotel[floor_num]:
                try:
                    if len(hotel[floor_num][room_num]) == 0:
                        print("great! lets get you checked in.")
                        num_guests = int(input("how many guests will be staying with you? "))
                        break
                    else:
                        raise TypeError
                except TypeError:
                    print("sorry that wasn't a valid choice, please enter a number bigger than 0")
                guest_names = []
                for guest in range(num_guests):
                    name = input(f"What is guests number {guest + 1} name?")
                    guest_names.append(name)
                    hotel[floor_num][room_num] = guest_names
            else:
                raise TypeError
        except TypeError:
            print("sorry that wasn't a valid selection")
    return hotel

def check_out():
    floor_num = input("What floor is your room on? ")
    if floor_num in floor_list:
        print(hotel[floor_num].keys())
    else:
        print("sorry that aint it")
    room_num = input("What room is yours? ")
    if room_num in hotel[floor_num]:
        if len(hotel[floor_num][room_num]) > 0:
            del hotel[floor_num][room_num]
        else:
            print("looks like this room is already empty!")
    else:
        print("sorry that isnt a valid selection")
    return hotel

def hotel_func():
    desk = int(input("Hello would you like to check-in(1) or check-out(2)? "))
    if desk == 1:
        check_in()
    if desk == 2:
        check_out()

print(hotel_func())
            
# guest_list = []
# for floor in floor_list:
#     for room in hotel[floor]:
#         guest_list.append((hotel[floor][room])) #gives me list of guests in rooms