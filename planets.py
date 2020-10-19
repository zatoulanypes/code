class SpaceObject:
    def __init__(self, name=None):
        self.name = name


class Animal:
    def __init__(self, name=None, color=None, weight=None):
        self.name = name
        self.color = color
        self.weight = weight
       
    def __str__(self):
        return self.name

    def breed(self):
        pass


class Cat(Animal):
    def __init__(self, name=None):
        self.name = 'Cat' + name

    def meow(self):
        return f'{self.name}: Meow!'


class Dog(Animal):
    def __init__(self, name=None, color=None, weight=None):
        self.name = 'Dog' + name
        
    def bark(self):
        return f'{self.name}: Woof!'


class Crocodile(Animal):
    def __init__(self, name=None, color=None, weight=None):
        self.name = 'Crocodile' + name

    def eat(self, animal):
        del animal
        print(f'{self.name} has just eaten {animal.name}!')


class Planet(SpaceObject):

    def __init__(self, name=None, population=None):
        super().__init__(name)
        self.population = population or []

    def __str__(self):
        if self.name:
            return self.name
        return 'Nameless Planet'

    def inhabit(self, *inhabitants):
        for inhabitant in inhabitants:
            self.population.append(inhabitant)


earth = Planet(Earth)

cat1 = Cat('Sprinkles')
cat2 = Cat('Fluffy')
dog1 = Dog('Minny')
croc1 = Crocodile('Joe')

earth.inhabit(cat1, cat2, dog1, croc1)
