class Animal :
    def __init__ (self , name ):
        self.name = name
    def speak (self) :
        print ( "animal made a song")

class Dog(Animal):
    def __init__ (self , name ) :
        super().__init__( name)

    def speak(self):
        print ("woof !")
class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def speak(self):
        print("Meow !")

dog = Dog("Lucy")
cat = Cat("Milo")

dog.speak()
cat.speak()