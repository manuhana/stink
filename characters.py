# character creation class
class Character:
	def __init__(self, name, hp, attack):
		self.name = name
		self.max_hp = hp
		self.hp = hp
		self.attack = attack
		
	def attacks(self, target):
		target.hp -= self.attack
		if target.hp < 0:
			target.hp = 0
		print(f"{self.name} deals {self.attack} damage to {target.name}")
		print(f"{target.name} took {self.attack} points of damage. {target.name}'s HP down to {target.hp}")
		
	def heal(self, x):
		self.hp += x
		if self.hp > self.max_hp:
			self.hp = self.max_hp # making sure that healing value won't excess max hp value
		
	@property
	def alive(self):
		return self.hp > 0

# enemies list, also available on the main file
enemy1 = Character("Wolf", 14, 3)
enemy2 = Character("Coyote", 15, 2)
enemy3 = Character("Lion", 18, 4)
enemy4 = Character("Hyena", 18, 2)
enemy5 = Character("Cheetah", 16, 4)