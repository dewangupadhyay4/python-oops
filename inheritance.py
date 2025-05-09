class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Dog Barks")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows")

dog=Dog()
dog.make_sound()

cat=Cat()
cat.make_sound()