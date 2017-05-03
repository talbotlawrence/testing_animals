import unittest
from animals import *

class TestTheAnimals(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """
        This method instantiates an Animal/Panda and a Dog
        These objects are available for the test methods below
        """

        self.animal = Animal('Buddy', 'Panda', 4)
        self.angus = Dog('Angus')
        print(self.animal.name)

    def test_animal_name_property_has_correct_value(self):
        """the line below implies that the Animal Class will have a NAME getter and setter"""
        self.assertEqual(self.animal.name, 'Buddy')   

    def test_animal_species_property_has_correct_value(self):
        """the line below implies that the Animal Class will have a SPECIES getter and setter"""
        self.assertEqual(self.animal.species, 'Panda')

    def test_dog_species_property_has_correct_value(self):
        """the line below implies that there will be a Dog Class"""
        self.assertEqual(self.angus.species, 'Dog')

    def test_walk_method_sets_speed(self):
        """
        This test method will set the number of legs to 4.
        It implies that there will be a set_legs() method in the Animal Class.
        It also implies that there will be a walk() method in the Animal Class.
        The Animal class __init__ method will set the speed.
        The Dog class will modify the speed.
        """

        legs = 4
        self.animal.set_legs(legs)
        self.animal.walk()

        self.angus.set_legs(legs)
        self.angus.walk()

        self.assertEqual(self.animal.speed, 0.4)
        self.assertEqual(self.angus.speed, 0.8)