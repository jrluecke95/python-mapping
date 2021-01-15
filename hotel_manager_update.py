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

def find_floor():
    while True:
        floor_num = input("What floor is your room on? ")
        try:
            if floor_num in floor_list:
                print(hotel[floor_num].keys())
            else:
                raise TypeError
        except TypeError:
            print("sorry that wasn't a valid selection.")
    find_room(floor_num)

def find_room(floor):
    floor_num = floor
    while True:
        try:
            room_num = input(room_list + "What room is yours? ")
            if room_num in hotel[floor_num]:
                room_check(room_num)
                break
            else:
                raise TypeError
        except:
            print("sorry that wasn't a valid selection")
    room_check(room_num)
 
def room_check(room):
    room_num = room
    floor_num = room[0]
    while True:
        try:
            if len(hotel[floor_num][room_num]) != 0:
                raise TypeError
            else:
                print("great! lets get your guests checked in")
                num_guests()
                break
        except TypeError:
            print("sorry that room is occupied")
    num_guests(room_num)


def num_guests(room):
    room_num = room
    # floor_num = room[0]
    while True:
        try:
            num_guests = int(input("how many guests will be staying with you?"))
            if num_guests > 0:
                guest_assign(room_num, num_guests)
                break
            else:
                raise TypeError
        except TypeError:
            print("sorry you have to have at least 1 guest")
    guest_assign(room_num, num_guests)

def guest_assign(room, guests):
    guest_names = []
    room_num = room
    floor_num = room[0]
    guest = 0
    while guest < range(num_guests):
        try:
            name = input(f"What is guest number {guest + 1} name? ")
            if len(name) > 0:
                guest_names.append(name)
                guest += 1
            else:
                raise TypeError
        except TypeError:
            print("sorry we need a valid name for the room")
    hotel[floor_num][room_num] = guest_names
    return hotel

find_floor()








# guest_names = []
# for guest in range(num_guests):
#     name = input(f"What is guests number {guest + 1} name?")
#     guest_names.append(name)
#     hotel[floor_num][room_num] = guest_names

print(find_room('2'))