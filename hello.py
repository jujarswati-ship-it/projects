class student:
    def __init__(self,name,age):
       self.name=name
       self.age=age

    def display(self):
        print(f'name:{self.name}, age:{self.age} ')
    def study(self,subject):
        print(f'{self.name} is studying{subject}')
s1=student("swati",11)
s2=student("san",12)
s1.display()


class Swati:
    def display(self):
        print("name:Swati")
        print("age:19")
        print("course:python")
s1=Swati()
s1.display()

class student:
    def __init__(self,name,age,course):
         self.name=name
         self.age=age
         self.course=course


    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("course:",self.course)
s1=student("swati",19,"python")
s2=student("vaish",19,"Java")
s3=student("Mahi",19,"Adv Java")
s1.display()
s2.display()
s3.display()