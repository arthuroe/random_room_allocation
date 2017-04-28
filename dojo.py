class Dojo(object):
    def __init__(self):
        self.rooms = {}
        self.people = {}

    def create_room(self, room_type, *room_names):
        room_name = list(room_names)
        if room_type == 'office':

            if 'office' in self.rooms:
                for room in room_name:
                    self.rooms['office'].append(room)
                    room_counter = len(room_name)
                    room_counter += 1
                    print (room_counter)
            else:
                self.rooms['office'] = room_name
            return self.rooms
        elif room_type == 'living_space':
            if 'living_space' in self.rooms:
                for room in room_name:
                    self.rooms['living_space'].append(rooms)
                    room_counter = len(l)
                    room_counter += 1
                    print (room_counter)
            else:
                self.rooms['living_space'] = room_name
            return self.rooms
        else:
            return 'Unknown room'

    def add_person(self, name, position, accomodation='N'):
        info = (name, accomodation)
        if position == 'fellow':
            if position in self.people:
                self.people[position].append(info)
            else:
                self.people[position] = []
                self.people[position].append(info)
            return self.people
        elif position == 'staff':
            if position in self.people:
                self.people[position].append(info)
            else:
                self.people[position] = []
                self.people[position].append(info)
            return self.people
        else:
            return 'Unknown position'

    def available_rooms(self, room_type):
        if len(self.rooms) <= 0:
            return "No rooms available!"
        else:
            available_rooms = {}

            for room in self.rooms:
                if room.occupants < room.capacity:
                    available_rooms[room_type].append(room)

            return available_rooms

    def assign_room(self, position, person_object, accomodation):
        if len(self.rooms) <= 0:

            print("No Rooms available")
            return "No Rooms available"

        else:
            if len(self.offices) <= 0:
                print("No Office Space available")
                return "No Office Space available"
            else:
                if person_object.office == "":
                    available_offices = self.get_available_rooms("office")
                    if len(available_offices) >= 1:

                        office_to_assign = random.choice(available_offices)
                        person_object.office = office_to_assign.name

                        office_to_assign.occupants += 1
                        self.assignedRooms.append(office_to_assign)

                        return self
                    else:
                        print("No available offices found")
                else:
                    print("Already has office")


class Room():
    def __init__(self):
        self.name = name
        self.max_number = max_number


class Office(Room):

    def __init__(self):
        super().__init__(name)
        self.max_number = 6


class Living_space(Room):
    max_number = 4

    def __init__(self):
        super().__init__(name)


class Person():
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def allocate():
        pass


class Fellow(Person):
    def __init__(self):
        super().__init__(name, position)


class Staff(Person):
    def __init__(self):
        super().__init__(name, position)


dojo = Dojo()
