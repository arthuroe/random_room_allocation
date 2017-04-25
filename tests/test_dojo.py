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

if __name__ == '__main__':
    unittest.main()
