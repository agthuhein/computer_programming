class Animal:
    def speak(self):
        print("I am an animal.")

    
class Dog(Animal):
    def speak(self):
        print("I am a dog.")

a1 = Animal()
a1.speak()

d1 = Dog()
d1.speak()