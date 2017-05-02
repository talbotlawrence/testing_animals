class Animal:
    def __init__(self, name, species):
        self.__name = name
        self.__species = species
        self.speed = 0
        self.legs = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if isinstance(val, str):
            self.__name = val

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, val):
        self.__species = val

    def walk(self):
        """Sets the speed of the animal"""
        if isinstance(self.legs, int) and self.legs > 0:
            self.speed = self.speed + (0.1 * self.legs)
        else:
            raise ValueError('Legs property must contain a number greater than 0')

    def set_legs(self, number_of_legs):
        """Sets the species of the animal"""
        self.legs = number_of_legs


    def __str__(self):
        return "{} is a {}".format(self.name, self.species)


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Dog")

    def walk(self):
        """Sets the speed of the dog"""
        self.speed = self.speed + (0.2 * self.legs)  