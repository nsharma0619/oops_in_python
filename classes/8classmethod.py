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
        self.pay = int(self.pay * self.raise_amount)  # we have to use variables using either classes or instances
        # self.pay = int(self.pay * Employee.raise_amount)

    @classmethod # also called alternative constructor
    def from_string(cls, string):
        fname, lname, pay = string.split("-")
        return cls(fname, lname, pay)


# emp_1 = Employee("Neeraj", "Sharma", 54000)
# emp_2 = Employee("Test", "User",  45000)

# print(Employee.num_of_emp)

emp_1 = Employee.from_string("Neeraj-sharma-50000")

print(emp_1.getFullName())