# explain help function here


class Employee():

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


    def PayInc(self):
        self.pay = int(self.pay * Employee.raise_amount)

class developer(Employee):
    pass

# dev_1 = Employee("Neeraj", "Sharma", 50000)
dev_1 = developer("Neeraj", "Sharma", 50000)

print(dev_1.email)
# print(help(developer))