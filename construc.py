class Student:
    def __init__(self,name,roll,branch,address,email):
        self.name=name
        self.roll=roll
        self.branch=branch
        self.address=address
        self.email=email
    def display(self):
        print('name is:',self.name)
        print('roll is:',self.roll)
        print('branch is:',self.branch)
        print('address is:',self.address)
        print('email is:',self.email)
s1=Student('prvs',101,'cse','hyd','pra@gmail.com')
s1.display()