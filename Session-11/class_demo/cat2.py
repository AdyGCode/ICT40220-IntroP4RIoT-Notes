class Cat:
    def __init__(self, name, age, coat_colour):
        # constructor (initializer)
        self.name = name
        self.age = age
        self.coat_colour = coat_colour

    def meow(self):
        print(f"{self.name} says 'Meow!'")

    def purr(self):
        print(f"{self.name} purrrrrrs")

    def hiss(self, other):
        print(f'{self.name} hisses at {other.name}')

    def meet(self, other):
        if isinstance(other, Cat) or isinstance(other, Dog):
            self.hiss(other)
        if isinstance(other, Person) and other.name == "Raf":
            self.purr()


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} barks")

    def wag(self):
        print(f"{self.name} wags their tail")

    def meet(self, other):
        if isinstance(other, Cat):
            self.bark()
        if isinstance(other, Dog):
            self.wag()


class Person:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"{self.name} say 'Hello there!'")


cat = Cat("Cat", 1, "hairless")

tabby = Cat("Whiskers", 2, 'tabby')
black = Cat("Dark", 7, 'black')
spaniel = Dog("Woof", 4)
pug = Dog('Rover', 2)

tabby.meow()
black.purr()

black.meet(tabby)
tabby.meet(spaniel)

spaniel.meet(tabby)
spaniel.meet(pug)

the_man = Person("Raf")
the_man.welcome()

tabby.meet(the_man)
