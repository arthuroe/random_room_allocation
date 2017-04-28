import unittest
import sys
sys.path.append('..')
from dojo import Dojo


class CreateRoomTestCase(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def test_initial_room_check(self):
        self.assertEqual(self.dojo.rooms, {}, msg='invalid')

    def test_create_room_successfully(self):
        initial_room_count = len(self.dojo.rooms)
        blue_office = self.dojo.create_room('office', 'blue')
        self.assertTrue(blue_office)
        new_room_count = len(self.dojo.rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_multiple_rooms(self):
        self.dojo.create_room('office', 'blue', 'black')
        self.assertEqual(self.dojo.rooms, {'office': [
                         'blue', 'black']}, msg='Multiple rooms cannot be entered')

    def test_create_single_rooms(self):
        self.dojo.create_room('living_space', 'dom')
        self.assertEqual(self.dojo.rooms, {'living_space': [
                         'dom']}, msg='Unable to add room when provided with single room')

    def test_create_unknown_room_type(self):
        self.assertEqual(self.dojo.create_room('kitchen', 'dom'),
                         'Unknown room', msg='Unknown room')

    def test_add_unknown_person_position(self):
        self.dojo.add_person('john deer', 'facilitator', 'Y')
        self.assertEqual(self.dojo.people, {'fellow': [('blue', 'Y')]}, msg='Unknown position')

    def test_add_unknown_person_position(self):
        self.assertEqual(self.dojo.add_person('john deer', 'facilitator', 'Y'),
                         'Unknown position', msg='Unknown position')

    def test_add_person_fellow(self):
        self.dojo.add_person('john deer', 'fellow', 'Y')
        self.assertEqual(self.dojo.people[position], {'fellow': [
                         ('blue', 'Y')]}, msg='Unable to add fellow')

    def test_add_person_staff(self):
        self.dojo.add_person('john deer', 'staff')
        self.assertEqual(self.dojo.people['staff'], {'staff': [
                         ('blue', 'N')]}, msg='Unable to add staff')
