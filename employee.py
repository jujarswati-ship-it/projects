class Employee:
    def __init__(self,Name,Salary,Department,Experience):
         self.Name=Name
         self.Salary=Salary
         self.Department=Department
         self.Experience=Experience
         
         
    def display(self):
        print("Name:",self.Name)


        print("Salary:",self.Salary)

        print("Department:",self.Department)

        print("Experience:",self.Experience)

s1=Employee("Swati",19000,"HR","5")

s2=Employee("Vaish",20000,"Sales","4")

s3=Employee("Mahi",25000,"SS","6")
s1.display()
s2.display()
s3.display()