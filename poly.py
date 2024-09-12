class Person:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def __str__(self):
        return f'{self.name},{self.age}'
class Student(Person):
    def __init__(self,name,age,roll,branch):
        super().__init__(name,age)    #using super contructor
        self.roll=roll
        self.branch=branch
    def __str__(self):
        res=super().__str__()
        return f'{res},{self.roll},{self.branch}'
class AnnualDay(Student):
    def __init__(self,name,age,roll,branch,program):
        super().__init__(name,age,roll,branch)
        self.program=program
    def __str__(self):
        studdetails=super().__str__()
        return f'{studdetails},{self.program}'
aobj=AnnualDay('prvhhh',34,155,'cse','dance')
print(aobj)
obj=Student('pravs',25,101,'cse')
print(obj)