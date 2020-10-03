class Employee:

    num_of_emp = 0
    raise_amount = 1.04  # class variables

    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.email = first+last+"@gmail.com"
        self.pay = pay
        Employee.num_of_emp+=1


    def getFullName(self):
        return "{} {}".format(self.fname, self.lname)


    # def __repr__(self):
    #     return "Employee('{}' '{}' '{}')".format(self.fname, self.lname, self.pay)
    
    def __str__(self):
        return "'{} {}' - {}".format(self.fname, self.lname, self.pay)

dev_1 = Employee("neeraj", "sharma", 50000)

print(dev_1)