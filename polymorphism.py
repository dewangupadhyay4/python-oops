class Dog:
    def speak(self):
        return "Bark"
    
class Cat:
    def speak(self):
        return "Mewos"
    
def animal_sound(animal):
    print(animal.speak())

dog=Dog()
cat=Cat()

animal_sound(dog)
animal_sound(cat)