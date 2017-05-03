class Animal:
    def __init__(self, name, species, legs):      #why doesn't speed and legs go in here?
        self.__name = name
        self.__species = species
        self.speed = 0
        self.legs = 0

    #NAME and SPECIES getters and setters############################################
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, val):
        self.__species = val

    #################################################################################

    #Animal Methods##################################################################

    def walk(self):
        """Sets the speed"""
        try:
            if self.legs > 0:
                self.speed = self.speed + (0.1 * self.legs)
        except ValueError:
            print('Legs property must contain a number greater than 0')

    def set_legs(self, number_of_legs):
        """Sets the number of legs"""
        self.legs = number_of_legs

    def __str__(self):
        return "{} is a {}".format(self.name, self.species)

    #################################################################################

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Dog", 4)     #I don't like having 4 in two different places
        self.__name = name
        #self.speed = 0.2
        self.legs = 4                             #This is the line that is working, not line 48

    def walk(self):
        """Sets the speed of the dog"""
        self.speed = self.speed + (0.2 * self.legs)  

charlie = Dog('charlie')
print("My dog is named {} and he has {} legs".format(charlie.name.title(), charlie.legs))
plato = Dog('plato')
print("My dog is named {} and this is his speed: {}".format(plato.name.title(), plato.walk()))
print(plato.legs)