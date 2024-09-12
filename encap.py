class Employee:
    # def __init__(self):   #non parametrized constructor/
    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.__salary=salary #private
    def get_salary(self):
        return self.__salary
    def Empdisplay(self):
        print(self.name,self.role)

class Company(Employee):
    def __init__(self,cname,loc):
        self.cname=cname
        self.loc=loc
    def Comdisplay(self):
        print(self.cname,self.loc)
    def _hiring(self):
        print('hiring for the manager role')
    
# obj=Employee()
# obj.display()
# obj.get__salary()
cobj=Company('wipro','gachibowli')
obj=Employee('pravs','developer',20000000)
obj.Empdisplay()
print(cobj._hiring())
