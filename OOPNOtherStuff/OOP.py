class Dog:
    species = "test" #class attribute (CA): applies to all instances of this class. can't be left empty. this is dynamic

    def __init__(self, name, age, phrase): #also applies to all instantiated objects but they can be empty and must be set during the instantiation
        self.name = name    #instance attribute (IA)
        self.age= age       #IA
        self.phrase = phrase

myDog = Dog("bob",10, "woof")
print(myDog.phrase) 
print(myDog.species)