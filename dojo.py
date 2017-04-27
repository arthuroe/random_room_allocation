class Dojo(object):
    def __init__(self):
        self.rooms = {}
        self.people = {}

    def create_room(self, room_type, *room_name):
        l = list(room_name)
        if room_type == 'office':

            if 'office' in self.rooms:
                for i in l:
                    self.rooms['office'].append(i)
                    room_counter = len(l)
                    room_counter += 1
                    print (room_counter)
            else:
                self.rooms['office'] = l
            return self.rooms
        elif room_type == 'living_space':
            if 'living_space' in self.rooms:
                for i in l:
                    self.rooms['living_space'].append(i)
                    room_counter = len(l)
                    room_counter += 1
                    print (room_counter)
            else:
                self.rooms['living_space'] = l
            return self.rooms
        else:
            return 'Unknown room'

    def add_person(self, name, position, accomodation='N'):
        l = (name, accomodation)
        if position == 'fellow':
            if position in self.people:
                self.people[position].append(l)
            else:
                self.people[position] = []
                self.people[position].append(l)
            return self.people
        elif position == 'staff':
            if position in self.people:
                self.people[position].append(l)
            else:
                self.people[position] = []
                self.people[position].append(l)
            return self.people
        else:
            return 'Unknown position'


class Room(Dojo):
    def __init__(self):
        pass


class Office(room):
    max = 6

    def __init__(self):
        pass


class Living_space(room):
    max = 4

    def __init__(self):
        pass


class Person(room):
    def __init__(self):
        pass


class Fellow(room):
    def __init__(self):
        pass


class Staff(room):
    def __init__(self):
        pass


dojo = Dojo()
print (dojo.create_room('living_space', 'blue', 'black', 'yellow'))
print (dojo.create_room('living_space', 'lue', 'lack', 'ellow'))
print (dojo.add_person('seb', 'fellow', 'Y'))
print (dojo.add_person('ebs', 'fellow', 'Y'))
print (dojo.add_person('sbe', 'fellow', 'Y'))
print (dojo.add_person('bes', 'fellow', 'Y'))
