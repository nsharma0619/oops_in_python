class Employee():

    raise_amount = 1.04  # class variables

    def __init__(self, first, last, email, pay):
        self.fname = first
        self.lname = last
        self.email = email
        self.pay = pay


    def getFullName(self):
        return "{} {}".format(self.fname, self.lname)


    def PayInc(self):
        self.pay = int(self.pay * self.raise_amount)  # we have to use variables using either classes or instances
        # self.pay = int(self.pay * Employee.raise_amount)


emp_1 = Employee("Neeraj", "Sharma", "Neeraj.Sharma@company.com", 54000)
emp_2 = Employee("Test", "User", "Test.User@company.com", 45000)


# print(emp_1.pay)

# emp_1.PayInc()

# print(emp_1.pay)

print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employee.__dict__)