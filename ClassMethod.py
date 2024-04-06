company = "Apple"
def show(self):
    print("The name is {self.name}and company is {self.company}")
@classmethod
def changeCompany(als,newCompany):
    cls.company = newCompany

e1=employee
e1.name = "sahil"
e1.show()
e1.changeCompany("yesi")
e1.show()
print(Employee.company)
