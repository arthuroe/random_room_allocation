class Room():
    def __init__(self, room_name, max_number):
        self.room_name = room_name
        self.max_number = max_number


class Office(Room):

    def __init__(self):
        super().__init__(room_name)
        self.max_number = 6


class Living_space(Room):

    def __init__(self):
        super().__init__(room_name)
        self.max_number = 4


class Person():
    def __init__(self, name, position):
        self.name = name
        self.position = position


class Fellow(Person):
    def __init__(self):
        super().__init__(name, position)


class Staff(Person):
    def __init__(self):
        super().__init__(name, position)
        self.accomodation = 'N'


class Dojo(object):
    #dojo_room = Room(room_name, max_number)
    #dojo_person = Person(name, position)

    def __init__(self):
        self.rooms = {}
        self.people = {}
        self.offices = {}
        self.living_space = {}

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

    def available_rooms(self, room_type, room_name):
        if len(self.rooms) <= 0:
            print ('No rooms available')
            return 'No rooms available'
        else:
            available_rooms = {}
            if len(room_type[room_name]) <= person.max_number:
                for room in self.rooms:
                    if room_type == 'office':
                        available_rooms['office'].append(room)
                    else:
                        available_rooms['living_space'].append(room)
                    return available_rooms
            else:
                return 'No rooms available'

    def allocate_room(self, position, accomodation):
        pass


dojo = Dojo()
