import unittest

from dojo import Dojo

class CreateRoomTestCase(unittest.TestCase):
	def setUp(self):
		self.dojo = Dojo()
	def test_create_room(self):
		self.assertEqual(self.dojo.rooms,[],msg='invalid')
	def test_create_nroom(self):
		self.dojo.create_room('blue')
		self.assertEqual(self.dojo.rooms,['blue'],msg='invalid')
	def test_create_room_successfully(self):
        	initial_room_count = len(self.dojo.all_rooms)
        	blue_office = self.dojo.create_room(“blue”, “office”)
        	self.assertTrue(blue_office)
        	new_room_count = len(self.dojo.all_rooms)
        	self.assertEqual(new_room_count - initial_room_count, 1)
	

if __name__ == '__main__':
    unittest.main()
