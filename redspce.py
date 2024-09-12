class Student:
    #static data
    branch='cse'
    def __init__(self,name,roll,address,email):
        self.name=name
        self.roll=roll
        self.address=address
        self.email=email
    # def display(self):
    #     print('name is:',self.name)
    #     print('roll is:',self.roll)
    #     print('branch is:',Student.branch)
    #     print('address is:',self.address)
    #     print('email is:',self.email)

    #another method is below one

    def __str__(self):
       # return f'{self.name} {self.roll} {self.address} {self.email}'
        return f'(self.name) (self.roll) (self.address) (self.email)'
s1=Student('prvs',101,'hyd','pra@gmail.com')
#s1.display()
print(s1)
s2=Student('vaish',105,'bnglr','vaish@gmail.com')
#s2.display()
print(s2)