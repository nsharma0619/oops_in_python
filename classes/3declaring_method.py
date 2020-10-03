class Employee():
    def __init__(self, first, last, email, pay):
        self.fname = first
        self.lname = last
        self.email = email
        self.pay = pay


    def getFullName(self):
        return "{} {}".format(self.fname, self.lname)


emp_1 = Employee("Neeraj", "Sharma", "Neeraj.Sharma@company.com", 54000)
emp_2 = Employee("Test", "User", "Test.User@company.com", 45000)



print(emp_1.getFullName())

print(Employee.getFullName(emp_1)) # another way to type
