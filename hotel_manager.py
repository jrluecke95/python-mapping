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
                    if len(hotel[floor_num][room_num]) != 0:
                        raise TypeError
                    else:
                        print("great! lets get you checked in.")
                        num_guests = int(input("how many guests will be staying with you? "))
                    guest_names = []
                    for guest in range(num_guests):
                        name = input(f"What is guests number {guest + 1} name?")
                        guest_names.append(name)
                        hotel[floor_num][room_num] = guest_names
                except TypeError:
                    print("sorry that room is occupied")
                    check_in()
            else:
                raise TypeError
        except TypeError:
            print("sorry that wasn't a valid selection")
        break
    return hotel

def check_out():
    while True:
        try:
            floor_num = input("What floor is your room on? ")
            if floor_num in floor_list:
                print(hotel[floor_num].keys())
                break
            else:
                raise TypeError
        except TypeError:
            print("sorry that wasn't a valid selection")
    while True:
        try:
            room_num = input("What room is yours? ")
            if room_num in hotel[floor_num]:
                while True:
                    try:
                        if len(hotel[floor_num][room_num]) > 0:
                            del hotel[floor_num][room_num]
                            break
                        else:
                            raise TypeError
                    except TypeError:
                        print("sorry it looks like that room is already empty")
            else:
                raise TypeError
        except:
            print("sorry that wasn't a vaild room selection")
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