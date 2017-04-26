class Dojo(object):
    def __init__(self):
        self.rooms={}			

    def create_room(self,room_type, *room_name):
	l = list(room_name)
        if room_type == 'office':
		
		if 'office' in self.rooms:
			for i in l:
				self.rooms['office'].append(i)
		else:
			self.rooms['office'] = l
		return self.rooms
	elif room_type == 'living_space':
		if 'living_space' in self.rooms:
			for i in l:
				self.rooms['living_space'].append(i)
		else:
			self.rooms['living_space'] = l
		return self.rooms
        else: 
		return 'Unknown room'
class room(Dojo):
	def __init__(self):
		pass
class office(room):
	def __init__(self):
		pass
class living_space(room):
	def __init__(self):
		pass
class person(room):
	def __init__(self):
		pass
class fellow(room):
	def __init__(self):
		pass
class staff(room):
	def __init__(self):
		pass
