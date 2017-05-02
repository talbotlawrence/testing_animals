import unittest
from animals import *

class TestTheAnimals(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.animal = Animal('Buddy', 'Panda')
		self.angus = Dog('Angus')
		self.animal.name = "Goofball"
		print(self.animal.name)

	def test_animal_name_property_has_correct_value(self):
		self.assertEqual(self.animal.name, 'Buddy')

	def test_animal_species_property_has_correct_value(self):
		self.assertEqual(self.animal.species, 'Panda')

	def test_dog_species_property_has_correct_value(self):
		self.assertEqual(self.angus.species, 'Dog')

	def test_walk_method_sets_speed(self):
		legs = 4
		self.animal.set_legs(legs)
		self.animal.walk()

		self.angus.set_legs(legs)
		self.angus.walk()

		self.assertEqual(self.animal.speed, 0.4)
		self.assertEqual(self.angus.speed, 0.8)