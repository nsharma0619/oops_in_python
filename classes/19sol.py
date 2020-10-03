class Employee:

    num_of_emp = 0
    raise_amount = 1.04  # class variables

    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.pay = pay
        Employee.num_of_emp+=1


    def getFullName(self):
        return "{} {}".format(self.fname, self.lname)

    def email(self):
        return "{}.{}@gmail.com".format(self.fname, self.lname)


emp_1 = Employee("Neeraj", "Sharma", 50000)
emp_1.fname = "Pankaj"
print(emp_1.email()) #now it become a method
print(emp_1.getFullName())