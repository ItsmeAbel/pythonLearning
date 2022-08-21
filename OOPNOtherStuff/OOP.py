import random
from unicodedata import name


class Dog:
    species = "test" #class attribute (CA): applies to all instances of this class. can't be left empty. this is dynamic

    def __init__(self, name, age): #also applies to all instantiated objects but they can be empty and must be set during the instantiation
        self.name = name    #instance attribute (IA)
        self.age= age       #IA
        #self.phrase = phrase
        #self.breed = breed
    
    def __str__(self):    #gets called with just print(myDog)
        return f"Name: {self.name}, Age: {self.age}."
#Methods that start with 2 underscores are called dunder methods. They don't need to be called. They auto run

    def goodDogBadDog(self): #the self parameter needs to be included
        choice = random.randint(0,1) #returns random int between the given range
        if choice == 1:
            return f"{self.name} is a good dog"
        else:
            return f"{self.name} is a bad dog"
    
    def speak(self, sound):
        return f"{self.name} barks {sound}"

myDog = Dog("bob",10)
print(myDog.species)
print(myDog) #runs the dunder method __str__()
print(myDog.goodDogBadDog())
print(myDog.speak("Ice Cream"))

#-----------Inheriting classes---------------------
#a class can extend or override attributes from another class. A "child" class can extend or override a "parent" class
#extend - Inherit the attributes from the parent class and extend it, aka add its own attributes, EX-inherit english lnguage from birth parents but you learn spanish
#Override - Inherit the attributes from the parent but change the attributes. EX-Inherit blonde hair from birth parents but you dye it black

class Goldenretriever(Dog): #a child class that inherits the Dog parent class
    pass
class Rottweiler(Dog): #we can override a parent class attribute like this
    def speak(self, sound="wuff"):
        return f"{self.name} barks {sound}"

bob = Goldenretriever("bob", 4)
print(type(bob)) #returns the inhering class
print(isinstance(bob, Dog)) #isinstance is a built in function that checks if an object is an instance of a class

deric = Rottweiler("deric", 8)
print(deric.speak())
print(deric.speak("sike"))