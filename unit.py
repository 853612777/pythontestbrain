from gameobjects.vector2 import Vector2


class unit(object):
	def __init__(self,world,image):
		self.world=world
		self.name=None
		self.id=None
		self.brain=None
		self.age=0
		self.health=100
		self.strength=100
		self.hunger=0
		self.speed=100
		self.location=None
		self.destination=None
		self.image=image
		self.range=100
		self.MAXAGE=100
	
	def render(self,surface):
		x,y=self.location
		w,h=self.image.get_size()
		surface.blit(self.image,(x-w/2,y-h/2))

	def check_die(self):
		if self.age>self.MAXAGE or self.health<=0:
			return True
		else:
			return False

	def change_location(self):
		if self.speed>0 and self.location!=self.destination:
			vec=self.destination-self.location
			distance_to_destination=vec.get_length()
			heading = vec.get_normalized()
			travel_distance = min(distance_to_destination,time_passed*self.speed)
			self.location += travel_distance*heading
		
	def process(self,time_passed):
		if check_die():
			return False
		if self.brain:
			self.brain.think()
		change_location()
		return True


			
		
	