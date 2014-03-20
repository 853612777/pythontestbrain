from gameobjects.vector2 import Vector2
import unit as u

class Ant(u.unit):
	def __init__(self,world,image):
		super(Ant,self).__init__(world,image)
		self.MAXAGE=10
		self.name='Ant'
		self.health=100
		self.strength=50
		self.speed=30
		self.range=120
