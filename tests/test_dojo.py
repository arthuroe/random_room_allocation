import unittest

from dojo import Dojo

class CreateRoomTestCase(unittest.TestCase):
	def setUp(self):
		self.dojo = Dojo()
	def test_initial_room_check(self):
		self.assertEqual(self.dojo.rooms,[],msg='invalid')
	def test_create_room(self):
		self.dojo.create_room('blue')
		self.assertEqual(self.dojo.rooms,['blue'],msg='invalid')
	def test_create_room_successfully(self):
        	initial_room_count = len(self.dojo.all_rooms)
        	blue_office = self.dojo.create_room(“blue”, “office”)
        	self.assertTrue(blue_office)
        	new_room_count = len(self.dojo.all_rooms)
        	self.assertEqual(new_room_count - initial_room_count, 1)
	def test_add_person(self):
		self.dojo.create_room('office','blue','black')
		self.assertEqual(self.dojo.rooms,{'office':['blue','black']},msg='invalid')
	def test_add_person(self):
		self.dojo.add_person('living_space','dom')
		self.assertEqual(self.dojo.rooms,{'living_space':['dom']},msg='invalid')
	def test_add_person(self):
		self.dojo.add_person('john deer','fellow','Y')
		self.assertEqual(self.dojo.people,{'fellow':[('blue','Y')]},msg='invalid')
	def test_add_person(self):
		self.dojo.add_person('john deer','staff')
		self.assertEqual(self.dojo.people,{'fellow':[('blue','N')]},msg='invalid')
	
