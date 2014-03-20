
class World(object):
	def __init__(self):
		self.units={}
		self.unit_id=0

	def add_unit(self,unit):
		self.units[self.unit_id]=unit
		unit.id=self.unit_id
		self.unit_id +=1

	def remove_unit(self,unit):
		del self.units[unit.id]

	def get(self,unit_id):
		if unit_id in self.units:
			return self.units[unit_id]
		else:
			return None

	def process(self,time_passed):
		time_passed_seconds=time_passed /1000.0
		for unit in self.units.itervalues():
			ret=unit.process(time_passed_seconds)
			if False==ret:
				remove_unit(unit)

	def render(self,surface):
		for unit in self.units.values():
			unit.render(surface)

	def get_close_unit(self,name,location):
		location=Vector2(*location)
		for unit in self.units.values():
			if unit.name == name:
				distance = location.get_distance_to(unit.location)
				if distance <= unit.range:
					return unit
		return None