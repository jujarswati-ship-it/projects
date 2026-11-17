class Animal:
    def sound(self):
         print("Animal makes sound")        

class Dog(Animal):
     def sound(self):
          print("Dog roars")

class  Cat(Animal):
     def sound(self):
          print("Cat barks")

d=Dog()
c=Cat()        
d.sound()
c.sound()                                                                       