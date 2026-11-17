
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