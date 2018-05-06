class employee:
    man = 'yes'
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = int(age)
    def display(self):
        print('employee_name: %s %s'%(self.first,self.last))
        print('employee_age: %d'%(self.age))
    #creating constructor
    @classmethod
    def from_string(cls,emp_str):
        first,last,age=emp_str.split()
        return cls(first,last,age)



e=employee.from_string('saba naaz 15')
e.display()
'''
basic verfication

e= employee('sha' , 'at',22)
f=employee('benazeer','firdous',20)
e.display()
print(e.man)
print(e.__dict__)
e.man = 'True'
employee.man = 'no'
print(e.__dict__)
print(f.man)'''